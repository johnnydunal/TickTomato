# TickTomato


## Introduction
### What it is
TickTomato is a pomodoro focus timer (25 minutes work, 5 minutes break) that has a daily task list, plays custom sound effects, and rewards users with a mini-game when a session finishes.
### Who it's for & Why it exists


## Installation






## Quick Start (For Users)

You do not need to install Python to run this application.

1. Go to the [Releases](https://github.com/johnnydunal/TickTomato/releases) page.
2. Download the latest `TickTomato.zip` file.
3. Extract (unzip) the file completely to a folder on your computer.
4. Open the extracted folder, find `TickTomato.exe`, and double-click it to run.

*Note: Do not move the main executable out of its folder, as it relies on the internal files around it to run properly. If you want a desktop shortcut, right-click the executable and select "Create Shortcut" (or "Pin to Taskbar/Start").*

## Development Setup

If you want to run the app from source or build it yourself, follow these steps.

### Prerequisites
- Python 3.x
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/johnnydunal/TickTomato.git
   cd TickTomato
   ```
2. Install dependencies:
   ```bash
   pip install pygame-ce
   ```
3. Run the app:
   ```bash
   python main.py
   ```

### Building the Bundle
To bundle the application into a distribution folder using PyInstaller:
```bash
pyinstaller --clean --onedir --noconsole --contents-directory "." --add-data "assets/images;assets/images" --add-data "assets/sounds;assets/sounds" --icon=assets\images\new_logo.ico --name="TickTomato" main.py
```
The standalone bundle will be generated in the `dist/` directory.

## Usage and Examples
Upon launching the app, you will be greeted with the timer. The three buttons control starting/resuming, resetting, and opening the task management system. The games are available on the break timer screen.

## License
This project is licensed under an MIT license. Feel free to use it however you want to but make sure to include the license notice!

## Why we made this!


## AI Declaration
No AI was used for writing the code itself. However, the AI tools Gemini and Copilot were used for learning various python concepts and implementation methods.
