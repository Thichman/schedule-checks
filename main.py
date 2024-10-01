import os
import time
import schedule
import argparse
import webbrowser
import threading
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from PIL import ImageChops, Image

# List to store active URLs
active_urls = []


# Function to capture screenshot of a URL
def capture_screenshot(url, output_path):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(2)  # Wait for the page to fully load

    # Capture screenshot
    driver.save_screenshot(output_path)
    print(f"Screenshot saved to {output_path}")  # Debugging output

    driver.quit()


# Function to compare images
def images_are_different(img1_path, img2_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # Compare images
    diff = ImageChops.difference(img1, img2)
    if diff.getbbox():
        return True  # Images are different
    return False


# Function to check the webpage for changes
def check_for_updates(url, image_path):
    new_image_path = "new_image.png"

    # Capture new screenshot
    capture_screenshot(url, new_image_path)

    # Compare with previous screenshot
    if os.path.exists(image_path) and images_are_different(image_path, new_image_path):
        print(f"Webpage {url} has changed!")
        Image.open(new_image_path).save(image_path)
    else:
        print(f"No changes detected for {url}.")
        os.remove(new_image_path)


# Schedule the check every hour
def monitor_website():
    while True:
        schedule.run_pending()
        time.sleep(1)


# Function to schedule monitoring of a URL
def schedule_url(url):
    image_path = f"{url.replace('https://', '').replace('http://', '').replace('/', '_')}_screenshot.png"
    schedule.every(1).hours.do(check_for_updates, url, image_path)
    print(f"Scheduled monitoring for {url}")


# Command: Add URL to the list of active URLs and schedule it for monitoring
def add_url(url):
    active_urls.append(url)
    print(f"Added URL: {url}")

    # Capture the initial screenshot
    image_path = f"{url.replace('https://', '').replace('http://', '').replace('/', '_')}_screenshot.png"
    if not os.path.exists(image_path):
        capture_screenshot(url, image_path)
    else:
        print(f"Screenshot for {url} already exists.")

    # Schedule the URL for periodic monitoring
    schedule_url(url)


# Command: List active URLs
def list_urls():
    if not active_urls:
        print("No active URLs.")
    else:
        print("Active URLs:")
        for url in active_urls:
            print(url)


# Command: Run a check manually
def run_check():
    if not active_urls:
        print("No URLs to monitor. Add URLs first.")
    else:
        for url in active_urls:
            print(f"Checking for updates on {url}")
            image_path = f"{url.replace('https://', '').replace('http://', '').replace('/', '_')}_screenshot.png"
            if not os.path.exists(image_path):
                capture_screenshot(url, image_path)
            else:
                check_for_updates(url, image_path)


# Command: Open a URL in a browser
def open_url(url):
    webbrowser.open(url)
    print(f"Opened {url} in a browser.")


# Command: Open the README file
def open_readme():
    readme_path = "README.md"
    if os.path.exists(readme_path):
        webbrowser.open(readme_path)
        print(f"Opened {readme_path}.")
    else:
        print(f"{readme_path} not found.")


# Command: Display help
def display_help():
    print(
        """
Commands:
    add-url <URL>          - Add a URL to the active URLs list
    list-urls              - List all active URLs
    run-check              - Run the monitoring program manually
    open-url <URL>         - Open a URL in the browser
    open-readme            - Open the README file to see commands
    help                   - Display this help message
    """
    )


# Command-line interaction handler
def command_input():
    while True:
        command = input("> ").strip().split()
        if len(command) == 0:
            continue

        cmd = command[0]
        args = command[1:]

        if cmd == "add-url" and len(args) == 1:
            add_url(args[0])
        elif cmd == "list-urls":
            list_urls()
        elif cmd == "run-check":
            run_check()
        elif cmd == "open-url" and len(args) == 1:
            open_url(args[0])
        elif cmd == "open-readme":
            open_readme()
        elif cmd == "help":
            display_help()
        else:
            print("Invalid command. Use 'help' to see available commands.")


# Thread for monitoring websites
def start_monitoring():
    for url in active_urls:
        schedule_url(url)

    monitor_thread = threading.Thread(target=monitor_website)
    monitor_thread.daemon = True
    monitor_thread.start()


if __name__ == "__main__":
    print("Starting website monitoring...")
    print("Type 'help' for a list of commands.")

    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Website Monitoring Program")
    parser.add_argument("url", nargs="?", help="Initial URL to add and monitor")
    args = parser.parse_args()

    # If a URL is provided via command line, add it and start monitoring
    if args.url:
        add_url(args.url)

    # Start the monitoring in the background
    start_monitoring()

    # Start the command input handler
    command_input()
