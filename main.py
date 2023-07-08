from tkinter import *
import math

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

# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if REPS == 0 or REPS == 2 or REPS == 4 or REPS == 6:
        count_down(work_sec)
        REPS += 1
    if REPS == 1 or REPS == 3 or REPS == 5:
        REPS += 1
        count_down(short_break_sec)
    if REPS == 8:
        REPS +=1
        count_down(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title - Timer
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"))
timer_label.config(fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

# Task Counter
task_label = Label(text="✔", font=(FONT_NAME, 25))
task_label.config(fg=GREEN, bg=YELLOW)
task_label.grid(column=1, row=3)

# Reset button
reset_button = Button(text="Reset", highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

canvas = Canvas(width=200, height=234, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
