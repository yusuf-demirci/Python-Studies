from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):  
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(background=THEME_COLOR, padx=30, pady=30)
        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, text="Questions", 
                                                     font=("Arial", 20, "italic"), 
                                                     fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        true_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.correct.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.wrong = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.wrong.grid(column=1, row=2)

        self.score_l = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR)
        self.score_l.config(fg="white", font=("Courier", 16, "normal"))
        self.score_l.grid(column=1, row=0)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_l.config(text=f"Score: {self.quiz.score}")
            q_next = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_next)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the questions.")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

