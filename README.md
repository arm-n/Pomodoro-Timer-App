# Pomodoro-Timer-App
This repository contains a Pomodoro Timer application built using Python and Tkinter. The Pomodoro Technique is a productivity method that alternates between focused work sessions and short breaks to enhance concentration and prevent burnout.

📌 Features
Work Session: 25-minute focused work period.
Short Break: 5-minute break after each work session.
Long Break: 20-minute break after every four work sessions.
Start and Reset Buttons: Easy control to begin or reset the timer.
Visual Checkmarks: Displays checkmarks to track completed work sessions.
🛠️ How to Run the Application
Ensure Python is installed on your system.
Clone the repository:
bash
Copy
Edit
git clone https://github.com/arm-n/pomodoro-timer-app.git
cd pomodoro-timer
Run the script:
bash
Copy
Edit
python main.py
Ensure tomato.png is in the same directory as the script.

📊 Usage Instructions
Click Start to begin the timer.
Follow the Work/Break cycles.
Use Reset to stop and reset the timer.
Feel free to customize the work and break durations by modifying the constants:
python
Copy
Edit
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

📌 Requirements
Python 3.x
Tkinter (comes pre-installed with Python)
