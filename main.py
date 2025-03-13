import math
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
# Defining constants for colors, font, and time durations (in minutes)
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Global variables to track the number of repetitions and the timer instance
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets the timer and UI components to their initial state."""
    # Cancels the current timer if active
    window.after_cancel(timer)

    # Reset the timer text to 00:00
    canvas.itemconfig(timer_text, text="00:00")

    # Reset the main timer label and the checkmarks
    timer_label.config(text="Timer")
    tick.config(text="")

    # Reset the repetition counter
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts the Pomodoro timer and alternates between work and break sessions."""
    global reps

    # Time calculations (in seconds)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Increment the repetition counter
    reps += 1

    # If it's a work session (odd reps)
    if reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

    # If it's a long break (every 8th repetition)
    elif reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)

    # If it's a short break (even reps but not 8th)
    elif reps % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Handles the countdown timer and updates the UI every second."""

    # Calculate minutes and seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Ensure the seconds display in a two-digit format (e.g., 05 instead of 5)
    if count_sec == 0:
        count_sec = "00"
    elif count_sec in range(1, 10):
        count_sec = f"0{count_sec}"

    # Update the timer text on the canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # Continue the countdown if time remains
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # Start the next session after the current countdown ends
        start_timer()

        # Display checkmarks for each completed work session
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔️"
        tick.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Create a canvas for the tomato image and timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Load and display the tomato image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# Ensure the image is not garbage collected
canvas.image = tomato_img

# Add timer text to the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Create and position the main timer label
timer_label = Label(text="Timer", font=("Courier", 26, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

# Create and position the Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

# Create and position the Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

# Create and position the checkmark label
tick = Label(font=("courier", 12, "bold"), fg=GREEN, bg=YELLOW)
tick.grid(row=3, column=1, padx=5, pady=5)

# Start the Tkinter event loop
window.mainloop()