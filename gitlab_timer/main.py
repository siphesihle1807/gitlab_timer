from tkinter import *
import math

# constants in the program
ORANGE = "#ff7f3e"
BEIGE = "#fff6e9"
RED = "#e7305b"
BLUE = "#80c4e9"
FONT_NAME = "Futura"
GIT_TIME = 10
BREAK = 5
reps = 0
timer = None

'This function resets the timer, cancels the running time, resets back to 00:00.'


def reset_timer():
    title_label = Label(text="Timer", fg=ORANGE, bg=BEIGE, font=(FONT_NAME, 35, "bold"))
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt, text="00:00")
    global reps
    reps = 0



'''This function starts the timer and calculates the time spent for work and break'''


def start_timer():
    global reps
    reps += 1
    git_time = GIT_TIME * 60
    break_time = BREAK * 60

    if reps % 2 == 0:
        count_down(break_time)
        title_label.config(text="Break", fg=RED)
    else:
        count_down(git_time)
        title_label.config(text="Time To Commit", fg=ORANGE)


'''This function updates the timer display every second.'''


def count_down(count):
    minute_count = math.floor(count / 60)
    second_count = count % 60

    if second_count < 10:
        second_count = f"0{second_count}"

    canvas.itemconfig(timer_txt, text=f"{minute_count}:{second_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # mark = ""
        # work_sessions = math.floor(reps / 2)
        # for _ in range(work_sessions):
        #     mark += "✔"
        # check.config(text=mark)


# UI SETUP
window = Tk()
window.title("Git Pomodoro")
window.config(padx=100, pady=50, bg=BEIGE)

title_label = Label(text="Timer", fg=ORANGE, bg=BEIGE, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# check = Label(fg=GREEN, bg=YELLOW)
# check.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=BEIGE, highlightthickness=0)
git = PhotoImage(file="gitlab.png")
canvas.create_image(100, 112, image=git)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,  row=1)


window.mainloop()