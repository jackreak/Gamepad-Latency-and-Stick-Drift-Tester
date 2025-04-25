# Gamepad Latency and Stick Drift Tester 🎮

A Python tool that measures the performance of a connected game controller by logging button press latency and detecting analog stick drift. It uses Pygame to read controller inputs and Tkinter to display a live GUI for monitoring results in real-time.

## Features ✨

- **Button Input Latency Logging**: Measures and records the time between a physical button press and the software's detection of that event.
- **Analog Stick Drift Detection**: Monitors the neutral position of analog sticks and identifies any drift or offset when the stick is released.
- **Live Controller Feedback**: Provides real-time visual feedback in a Tkinter-based GUI, showing button presses and joystick positions.
- **Cross-Platform**: Runs on Windows, macOS, and Linux (with support for any controller recognized by Pygame).

## Installation 🛠️

1. **Python 3.x**: Ensure you have Python 3.6 or newer installed. Python 3.8+ is recommended for best compatibility.
2. **Tkinter**: Tkinter usually comes pre-installed with Python. On some Linux systems, you may need to install it separately (for example, `sudo apt-get install python3-tk` on Debian/Ubuntu).
3. **Pygame**: Install the Pygame library, which provides game controller support:

   ```bash
   pip install pygame

    Clone the Repository: Download or clone this repository to your local machine:

    git clone https://github.com/jackreak/Gamepad-Latency-and-Stick-Drift-Tester.git

Usage 🚀

    Connect Game Controller: Make sure your controller is connected to the computer before running the tool.

    Run the Application: Launch the main script from the command line:

    python main.py

    This will open a GUI window and start listening for controller input.

    Test Inputs:

        Latency Test: Press any gamepad button. The application will log the button name and measured latency (in milliseconds) in the console or GUI.

        Drift Test: Release the analog stick and check if any drift is detected. The app will report if the stick does not return exactly to center.

    Live Feedback: The GUI shows the current state of buttons and analog stick positions as you interact with the controller.


Usage Tips 💡

    Ensure the controller is properly recognized by your operating system before running the application.

    Close other applications that might capture gamepad input to avoid interference.

    For accurate latency measurements, run the tests multiple times and consider using a wired controller connection.

License 📜

This project is licensed under the MIT License. See the LICENSE file for details. """
