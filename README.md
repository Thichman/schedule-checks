# Website Monitoring Program

This program allows you to monitor websites for visual changes by taking periodic screenshots, comparing them, and notifying you of any changes. You can interact with the program in real-time through various command-line commands while the monitoring is running in the background.

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [How to Run the Program](#how-to-run-the-program)
- [Available Commands](#available-commands)
- [Examples](#examples)
- [Packaging and Distribution](#packaging-and-distribution)
- [Notes](#notes)

---

## Features

- **Monitor Web Pages**: Continuously monitor web pages for changes.
- **Command-Line Interaction**: Add, list, and remove URLs in real-time while the program runs.
- **Automatic Screenshots**: Automatically takes screenshots every hour.
- **Manual URL Checking**: Optionally check any website for changes manually.
- **View URLs**: Open a URL in your browser directly from the command line.
- **Readme Access**: Open the README file anytime for quick reference to commands.

---

## Setup

### Prerequisites

1. **Python 3.x** installed on your machine.
2. **Google Chrome** browser installed.

### Installation Steps

1. **Clone the repository** (or download the program files):
   ```bash
   git clone https://your-repository-url.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd website-check-program
   ```

3. **Create a virtual environment (optional but recommended)**:
   ```bash
   python3 -m venv website_monitor_env
   ```

4. **Activate the virtual environment**:
   - On **macOS/Linux**:
     ```bash
     source website_monitor_env/bin/activate
     ```
   - On **Windows**:
     ```bash
     website_monitor_env\Scripts\activate
     ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   The following packages will be installed:
   - `selenium`: To interact with web pages and take screenshots.
   - `webdriver-manager`: Automatically manages the appropriate ChromeDriver for your browser.
   - `Pillow`: For image comparison between screenshots.
   - `schedule`: For scheduling periodic checks of websites.

---

## How to Run the Program

Once you've completed the setup, you can start the program:

1. **Run the program**:
   ```bash
   python main.py
   ```

2. You will see a command prompt where you can start interacting with the program. For example:
   ```bash
   > help
   ```

The program will start monitoring websites that you add, but you can also run commands in real-time while the program is running.

You can also start the program by providing an initial URL to monitor:
   ```bash
   python main.py https://example.com
   ```

---

## Available Commands

The following commands can be used to interact with the program:

1. **`add-url <URL>`**  
   Adds a URL to the list of active URLs being monitored.
   ```bash
   > add-url https://example.com
   ```

2. **`list-urls`**  
   Lists all active URLs currently being monitored.
   ```bash
   > list-urls
   ```

3. **`run-check`**  
   Manually run a check for changes on all active URLs.
   ```bash
   > run-check
   ```

4. **`open-url <URL>`**  
   Opens the specified URL in your default browser.
   ```bash
   > open-url https://example.com
   ```

5. **`open-readme`**  
   Opens this README file in your default browser for reference.
   ```bash
   > open-readme
   ```

6. **`help`**  
   Displays a list of all available commands and their descriptions.
   ```bash
   > help
   ```

---

## Examples

1. **Add a URL to Monitor**:
   ```bash
   > add-url https://example.com
   ```

2. **List All Active URLs**:
   ```bash
   > list-urls
   ```

3. **Manually Run a Check**:
   ```bash
   > run-check
   ```

4. **Open a URL in Browser**:
   ```bash
   > open-url https://example.com
   ```

5. **Open the README File**:
   ```bash
   > open-readme
   ```

6. **Help**:
   ```bash
   > help
   ```

---

## Packaging and Distribution

### Packaging the Project for Sharing

If you want to share this project with someone else, follow these steps:

1. **Create a `requirements.txt` file**:
   ```bash
   pip freeze > requirements.txt
   ```

2. **Zip the project folder**:
   After ensuring all the necessary files (`main.py`, `requirements.txt`, `README.md`) are in the project directory, zip the project:
   ```bash
   zip -r website-monitor.zip .
   ```

3. **Send the zip file** to the recipient. They can unzip it and follow the instructions in this README to set up and run the program.

### Option: Create a Standalone Executable with PyInstaller

To make it even easier for someone to run the program without needing Python installed, you can create a standalone executable using **PyInstaller**.

#### Steps to create an executable:

1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```

2. **Create the executable**:
   ```bash
   pyinstaller --onefile main.py
   ```

   This will generate a `dist/` folder containing a single executable file. You can send this file to others, and they can run it without needing Python or any dependencies installed.

---

## How the Program Works

1. **Initial Setup**:
   - After running the program, you can begin adding URLs via the `add-url` command.
   - URLs are stored in memory (not persistently), so URLs need to be added again if the program is restarted.

2. **Automated Monitoring**:
   - Once you’ve added URLs, the program will automatically check for changes every hour.
   - Screenshots are stored in the same directory as the program.
   - When changes are detected, the program notifies you via the command-line interface.

3. **Manual URL Checking**:
   - You can also run a manual check at any time using the `run-check` command to immediately compare the current version of the page to the last saved screenshot.

4. **Opening URLs**:
   - The `open-url` command opens any monitored URL in your default web browser.

---

## Notes

- **Service Workers Warning**: When viewing screenshots, you may encounter a message about "Service Workers." This warning is harmless and related to the webpage's background scripts, which are irrelevant to static screenshots.
  
- **Screenshot Naming**: Screenshots are saved with filenames based on the URL (non-URL-friendly characters are replaced with underscores).

---

## License

This project is licensed under the MIT License.

---

Feel free to modify the program as needed or contact the developer for more details.
```

### Changes Added:
- **Packaging and Distribution Section**: Instructions for packaging the project and creating a standalone executable using PyInstaller.
- **Clarified Installation and Running**: Added command for running the program with a URL directly from the command line.

