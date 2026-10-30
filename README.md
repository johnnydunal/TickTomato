# TickTomato


## Introduction
### What it is
A pomodoro focus timer (25 minutes work, 5 minutes break) that has a daily task list, plays custom sound effects, and rewards users with a mini-game when a session finishes.
### Who it's for & Why it exists


## Installation
Navigate to the Releases tab and download the correct file for your operating system. Then, just open it an enjoy!

## .exe packaging
The following command is the one that packages the code into an exe!
`pyinstaller --clean --onedir --noconsole --contents-directory "." --add-data "assets/images;assets/images" --add-data "assets/sounds;assets/sounds" --icon=assets\images\new_logo.ico --name="TickTomato" main.py`
Took me a while to figure out but it works :)

## Usage and Examples
Upon launching the app, you will be greeted with the timer. The task management system can be accessed through its button, and the games are available on the break timer screen.

## License
This project is licensed under an MIT license. Feel free to use it however you want to but make sure to include the license notice!

## Why we made this!h
It can often be difficult for people to focus for a long period of time. TickTomato is made to help people work more productively and also gives them something to enjoy during the break.

## AI Declaration
No AI was used for writing the code itself. However, the AI tools Gemini and Copilot were used for learning various python concepts and implementation methods.
