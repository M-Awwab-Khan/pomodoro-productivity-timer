from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    title_label.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    check_marks.config(text='')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        title_label.config(text='Break', fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        title_label.config(text='Break', fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        title_label.config(text='Work', fg=GREEN)
        count_down(WORK_MIN*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = str(count_sec).zfill(2)
    if count_min < 10:
        count_min = str(count_min).zfill(2)
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 2 != 0:
            check_marks.config(text=f"{((reps//2)+1)*'✔'}")
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


start_button = Button(text='Start', command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset',command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(None, 20, 'bold'))
check_marks.grid(column=1, row=3)


window.mainloop()