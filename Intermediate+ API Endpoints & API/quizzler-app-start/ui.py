from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, question: QuizBrain):
        self.question = question

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(bg=THEME_COLOR)

        self.label_score = Label(text=f"Score: {self.question.score}", fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.label_score.grid(pady=20, column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, fill=THEME_COLOR,
                                                     font=("Arial", 20, 'italic'))
        self.canvas.grid(padx=20, columnspan=2, row=1)

        image_true = PhotoImage(
            file="D:/Mine/Programming/Python/CourseUdemy/projects/Intermediate+ API Endpoints & API/quizzler-app-start/images/true.png")
        image_false = PhotoImage(
            file="D:/Mine/Programming/Python/CourseUdemy/projects/Intermediate+ API Endpoints & API/quizzler-app-start/images/false.png")
        self.true_b = Button(image=image_true, command=self.true_button, highlightthickness=0)
        self.false_b = Button(image=image_false, command=self.false_button, highlightthickness=0)
        self.true_b.grid(pady=20, column=0, row=2)
        self.false_b.grid(pady=20, column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.question.still_has_questions():
            t_quiz = self.question.next_question()
            self.canvas.itemconfig(self.question_text, text=t_quiz)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_b.config(state="disabled")
            self.false_b.config(state="disabled")

    def true_button(self):
        is_right = self.question.check_answer("True")
        self.label_score.config(text=f"Score: {self.question.score}")
        self.give_feedback(is_right)

    def false_button(self):
        is_right = self.question.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
