import tkinter as tk
from tkinter import messagebox
import sqlite3
import time


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("600x400")
        self.root.config(bg="#f0f8ff")

        self.questions_conn = sqlite3.connect('questions.db')  # Connect to questions database
        self.results_conn = sqlite3.connect('results.db')  # Connect to results database

        self.username = ""
        self.question_index = 0
        self.score = 0
        self.questions = self.fetch_questions()

        self.create_home_screen()

    def fetch_questions(self):
        cursor = self.questions_conn.cursor()
        cursor.execute("SELECT * FROM questions")
        return cursor.fetchall()

    def create_home_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Welcome to the Quiz App", font=("Arial", 20, "bold"), bg="#f0f8ff").pack(pady=20)
        tk.Label(self.root, text="Enter your name:", font=("Arial", 14), bg="#f0f8ff").pack()
        self.name_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.name_entry.pack(pady=10)
        tk.Button(
            self.root, text="Start Quiz", font=("Arial", 14), bg="#4682b4", fg="white", command=self.start_quiz
        ).pack(pady=20)

    def start_quiz(self):
        self.username = self.name_entry.get()
        if not self.username:
            messagebox.showerror("Error", "Please enter your name")
            return

        self.question_index = 0
        self.score = 0
        self.create_question_screen()

    def create_question_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]

            tk.Label(
                self.root, text=f"Question {self.question_index + 1}/{len(self.questions)}",
                font=("Arial", 16, "bold"), bg="#f0f8ff"
            ).pack(pady=10)

            tk.Label(
                self.root, text=question_data[1], font=("Arial", 14), wraplength=500, bg="#f0f8ff"
            ).pack(pady=20)

            self.selected_option = tk.IntVar()

            options = question_data[2:6]
            for idx, option in enumerate(options, start=1):
                tk.Radiobutton(
                    self.root, text=option, variable=self.selected_option, value=idx, font=("Arial", 12), bg="#f0f8ff"
                ).pack(anchor="w", pady=5)

            tk.Button(
                self.root, text="Next", font=("Arial", 14), bg="#4682b4", fg="white", command=self.check_answer
            ).pack(pady=20)
        else:
            self.end_quiz()

    def check_answer(self):
        selected = self.selected_option.get()
        if selected == 0:
            messagebox.showerror("Error", "Please select an option")
            return

        correct_option = self.questions[self.question_index][6]
        if selected == correct_option:
            self.score += 1

        self.question_index += 1

        # Check if it's the last question
        if self.question_index < len(self.questions):
            self.show_animation()  # Show animation if there are more questions
        else:
            self.end_quiz()  # Directly end the quiz for the last question

    def show_animation(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create a canvas for the animation
        canvas = tk.Canvas(self.root, width=600, height=400, bg="#f0f8ff", highlightthickness=0)
        canvas.pack()

        # Animated text
        text_id = canvas.create_text(
            300, 200, text="Get Ready for the Next Question!", font=("Arial", 18, "bold"), fill="#4682b4"
        )

        # Fade-in animation
        for i in range(10):
            color = f"#{hex(100 + i * 15)[2:]}82b4"  # Gradual color change for fade-in effect
            canvas.itemconfig(text_id, fill=color)
            self.root.update_idletasks()
            time.sleep(0.1)

        # After a short delay, move to the next question
        self.root.after(500, self.create_question_screen)

    def end_quiz(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        cursor = self.results_conn.cursor()
        cursor.execute(
            "INSERT INTO scores (username, score) VALUES (?, ?)",
            (self.username, self.score)
        )
        self.results_conn.commit()

        tk.Label(self.root, text="Quiz Completed!", font=("Arial", 20, "bold"), bg="#f0f8ff").pack(pady=20)
        tk.Label(
            self.root, text=f"Your Score: {self.score}/{len(self.questions)}",
            font=("Arial", 16), bg="#f0f8ff"
        ).pack(pady=10)
        tk.Button(
            self.root, text="Restart", font=("Arial", 14), bg="#4682b4", fg="white", command=self.create_home_screen
        ).pack(pady=10)
        tk.Button(
            self.root, text="Quit", font=("Arial", 14), bg="#b22222", fg="white", command=self.root.quit
        ).pack(pady=5)

    def __del__(self):
        self.questions_conn.close()
        self.results_conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
