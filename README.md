IN CODE EDITOR/ If you dowload only to test, feel free to use the .exe file in dist folder.

## Automated Gmail Email Sender

This script uses PyAutoGUI to automate the process of composing and sending emails through Gmail. Below are the steps to set up and run the script:

### Requirements

- Python 3.x
- PyAutoGUI: Install using `pip install pyautogui`
- Ensure Gmail is open and the compose window is visible

### Setup

1. **Capture Images**: Take screenshots of the Gmail compose button, attach button, and send button. Save them as `Compose.png`, `Attach.png`, and `Send.png` in the same directory as the script.

2. **Update File Path**: Replace `file.txt` in the script with the path to the file you want to attach.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using:
     ```bash
     python your_script_name.py
     ```

4. **Ensure Focus**: Make sure the Gmail window is in focus before running the script.

### Notes

- The script assumes that Gmail is already logged in and the compose window is visible.
- Adjust image paths and time delays if needed based on your system's performance.

Feel free to modify the script as per your needs and ensure you have the appropriate permissions to automate actions on your Gmail account.
