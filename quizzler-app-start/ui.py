from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface :

    def __init__(self,quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text = "Score : 0",fg="white",bg = THEME_COLOR)
        self.score_label.grid(row = 0,column =1)

        self.canvas = Canvas(width = 300,height = 250,bg = "white")
        self.question_text = self.canvas.create_text(150,125,width = 280,text = "Some Question Text", fill = THEME_COLOR,font = ("Arial",20,'italic'))
        self.canvas.grid(row = 1,column = 0,columnspan = 2,pady = 50)

        true_image = PhotoImage(file = "images/true.png" )
        self.true_button = Button(image = true_image,highlightthickness = 0,command = self.true_pressed)
        self.true_button.grid(row = 2,column = 0)


        false_image = PhotoImage(file = "images/false.png")
        self.falsebutton = Button(image = false_image,highlightthickness = 0)
        self.falsebutton.grid(row = 2,column = 1)


        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        # 1. FIX THE COLOR: Always reset the canvas to white first
        self.canvas.config(bg="white")
        
        if self.quiz.still_has_questions():
            # 2. FIX THE SCORE: Update the label text with the current score
            self.score_label.config(text=f"Score: {self.quiz.score}")
            
            # Fetch the next question and display it
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            
        else:
            # End of the quiz behavior
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.falsebutton.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        # Change canvas color based on the answer
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

