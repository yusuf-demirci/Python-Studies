from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN  = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    
    if reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)
    elif reps % 8 == 0:
        timer_label.config(text="Rest", fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        timer_label.config(text="Rest", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    
    
   

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count_min < 10:
        count_min = "0" + str(count_min)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:   
        global timer 
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 2 == 1:
            check_marks.config(text=(reps+1)//2*("✔"))
        if reps != 8:
            start_timer()
   


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=220, height=244, bg=YELLOW, highlightthickness= 0)
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(105, 135, text = "00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
check_marks.grid(column=1, row=3)

start_button = Button(text="Start", bg="white", font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="white", font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()