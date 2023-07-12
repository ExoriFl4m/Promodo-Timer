from tkinter import *
import math
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = NONE
PAUSE = False

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    global PAUSE
    window.after_cancel(TIMER)
    title_label.config(fg=GREEN, text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    task_label.config(text="")
    REPS = 0
    start_button.config(state="normal")
    pause_button.config(text="Pause")
    PAUSE = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    start_button.config(state="disabled")
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(fg=RED, text="Break")
    elif REPS % 2 == 0:
        title_label.config(fg=PINK, text="Break")
        count_down(short_break_sec)
    else:
        count_down(work_sec)
        title_label.config(fg=GREEN, text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        global PAUSE
        if PAUSE:
            TIMER = window.after(0, count_down, count)
        else:
            TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        playsound("short-success-sound-glockenspiel-treasure-video-game-6346.mp3")
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✔"
        task_label.config(text=marks)


def pause_cd():
    global PAUSE
    PAUSE = not PAUSE
    if PAUSE:
        pause_button.config(text="Resume")
    else:
        pause_button.config(text="Pause")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(width=False, height=False)

# Title Label
title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"))
title_label.config(fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

# Task Counter
task_label = Label(font=(FONT_NAME, 25))
task_label.config(fg=GREEN, bg=YELLOW)
task_label.grid(column=1, row=3)

# Reset button
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

# Pause button
pause_button = Button(text="Pause", highlightbackground=YELLOW, command=pause_cd)
pause_button.grid(column=1, row=4)

canvas = Canvas(width=200, height=234, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
