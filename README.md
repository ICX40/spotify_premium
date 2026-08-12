Spotify Auto Installer & Patcher
A clean, automated Python script designed to streamline the installation of the official Spotify desktop client, execute custom activation/patch scripts seamlessly, and direct users straight to your GitHub profile. Developed with a sleek command-line interface (CLI) styled for Eng.Eyad.

Features
Automated Download & Silent Installation: Fetches the latest official Spotify installer directly from Spotify's servers and installs it silently in the background.

Integrated Patcher Support: Automatically triggers your custom Install_Auto.bat script to handle the activation process right after installation.

GitHub Integration: Automatically opens your GitHub profile ([https://github.com/ICX40](https://github.com/ICX40)) upon completion.

Interactive CLI Menu: Built with a clean, color-coded terminal interface featuring ANSI escape codes and custom ASCII art banners.

Prerequisites
Python 3.x installed on your Windows machine.

The companion activation script named Install_Auto.bat placed in the exact same directory as this Python script.

File Structure
Make sure your project folder looks like this:

Plaintext
📂 Spotify-Automation/
├── 📜 spotify_installer.py    # The main Python automation script
└── 📜 Install_Auto.bat        # Your custom activation/patch script
How to Run
Open your terminal or Command Prompt (CMD) inside the project folder.

Run the script using Python:

Bash
python spotify_installer.py
Choose your desired option from the interactive menu:

[1] Install Spotify, run the patcher, and open GitHub.

[2] Run the activation script (Install_Auto.bat) only.

[3] Open the developer's GitHub profile.

[4] Exit.

Code Explanation
Here is a quick breakdown of how the Python script works under the hood:

Libraries Imported:

os: Used for terminal screen clearing (cls), path management, and retrieving environment variables (TEMP).

subprocess: Handles running shell commands synchronously (downloading via PowerShell, launching silent installers, and calling the .bat file).

sys: Controls clean application exits.

webbrowser: Handles launching the default web browser to open your GitHub URL.

time: Adds short delays to ensure smooth execution transitions.

print_banner() Function:

Clears the terminal and renders custom ASCII art styled with bright blue and cyan ANSI color codes (\033[1;34m), displaying Eng.Eyad front and center.

install_spotify() Function:

Targets the Windows %TEMP% directory and uses PowerShell's Invoke-WebRequest to securely download the official SpotifySetup.exe.

Executes the installer using the /s flag for a clean, silent background installation.

run_patcher() Function:

Checks if Install_Auto.bat exists in the current directory using os.path.exists(). If found, it executes it through the shell.

open_github() Function:

Uses Python's built-in webbrowser.open() module to navigate directly to https://github.com/ICX40.

main() Function:

Runs an infinite while loop keeping the interactive menu active until the user chooses to exit, handling user inputs safely with conditional checks.

Developed By
Eng.Eyad
