import tkinter as tk
from tkinter import messagebox
import random

# Expanded pool of 30 questions
quiz_questions = [
    {"question": "Which year was the first LEGO Technic set released?", "options": ["1977", "1984", "1990", "2001"], "answer": "1977"},
    {"question": "What is the primary difference between LEGO Technic and regular LEGO?", "options": ["Technic uses more colors", "Technic includes motors and gears", "Technic sets are smaller", "There is no difference"], "answer": "Technic includes motors and gears"},
    {"question": "Which part is commonly used in LEGO Technic to transfer rotational motion?", "options": ["Axle", "Gear", "Pin", "Beam"], "answer": "Gear"},
    {"question": "Which LEGO Technic set is known for its realistic gearbox and suspension system?", "options": ["Bugatti Chiron (42083)", "Race Kart (42048)", "Compact Crawler Crane (42097)", "Stunt Truck (42059)"], "answer": "Bugatti Chiron (42083)"},
    {"question": "What type of joint allows LEGO Technic models to have steering mechanisms?", "options": ["Ball joint", "Universal joint", "Pivot joint", "Fixed joint"], "answer": "Universal joint"},
    {"question": "Which LEGO Technic part helps convert rotary motion to linear motion?", "options": ["Linear actuator", "Gearbox", "Pulley", "Axle connector"], "answer": "Linear actuator"},
    {"question": "Which LEGO Technic set was the first to feature a working piston engine?", "options": ["Car Chassis (853)", "Forklift Truck (850)", "Off-Roader (8860)", "Power Truck (8285)"], "answer": "Off-Roader (8860)"},
    {"question": "What color are most LEGO Technic friction pins?", "options": ["Blue", "Red", "Black", "Grey"], "answer": "Black"},
    {"question": "What does 'RC' stand for in LEGO Technic RC vehicles?", "options": ["Remote Controlled", "Robot Car", "Rear Chassis", "Racing Construction"], "answer": "Remote Controlled"},
    {"question": "What LEGO Technic set recreated the Lamborghini Sián FKP 37?", "options": ["42115", "42096", "42110", "42125"], "answer": "42115"},
    {"question": "Which system powers many LEGO Technic pneumatic sets?", "options": ["Hydraulic system", "Air compressor", "Steam engine", "Water pump"], "answer": "Air compressor"},
    {"question": "Which mechanism allows LEGO Technic cranes to lift loads?", "options": ["Winch", "Differential", "Crankshaft", "Track"], "answer": "Winch"},
    {"question": "What type of LEGO Technic joint allows for angled connections?", "options": ["Ball joint", "Friction pin", "Linear joint", "Bevel gear"], "answer": "Ball joint"},
    {"question": "What is the function of a differential gear in LEGO Technic vehicles?", "options": ["To switch power between axles", "To drive the motor", "To balance wheel speed during turning", "To stop motion"], "answer": "To balance wheel speed during turning"},
    {"question": "What is a 'bevel gear' used for in LEGO Technic?", "options": ["Changing rotational direction", "Speeding up rotation", "Connecting beams", "Decoration"], "answer": "Changing rotational direction"}
]

leaderboard = []

class LegoQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LEGO Technic Quiz")
        self.root.geometry("600x500")
        self.score = 0
        self.current_q = 0
        self.selected_questions = []
        self.player_name = ""

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to the LEGO Technic Quiz!", font=("Arial", 18)).pack(pady=20)
        tk.Label(self.root, text="Enter your name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=10)
        tk.Button(self.root, text="Start Quiz", command=self.start_quiz).pack(pady=20)

    def start_quiz(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input required", "Please enter your name to start the quiz.")
            return
        self.player_name = name
        self.score = 0
        self.current_q = 0
        self.selected_questions = random.sample(quiz_questions, 10)
        self.show_question()

    def show_question(self):
        self.clear_screen()
        q = self.selected_questions[self.current_q]
        tk.Label(self.root, text=f"Question {self.current_q + 1}/10", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text=q['question'], wraplength=500, font=("Arial", 12)).pack(pady=10)

        self.answer_var = tk.StringVar()
        for opt in q['options']:
            tk.Radiobutton(self.root, text=opt, variable=self.answer_var, value=opt, font=("Arial", 11)).pack(anchor='w', padx=100)

        tk.Button(self.root, text="Submit", command=self.check_answer).pack(pady=20)

    def check_answer(self):
        selected = self.answer_var.get()
        if not selected:
            messagebox.showinfo("Select an answer", "Please choose an answer before continuing.")
            return

        correct = self.selected_questions[self.current_q]['answer']
        if selected == correct:
            self.score += 1
            messagebox.showinfo("Result", "✅ Correct!")
        else:
            messagebox.showinfo("Result", f"❌ Incorrect! The correct answer is: {correct}")

        self.current_q += 1
        if self.current_q < 10:
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.clear_screen()
        leaderboard.append((self.player_name, self.score))
        leaderboard.sort(key=lambda x: x[1], reverse=True)

        tk.Label(self.root, text="Quiz Complete!", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.root, text=f"{self.player_name}, your score is: {self.score}/10", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Leaderboard:", font=("Arial", 14, "bold")).pack(pady=10)
        for idx, (name, score) in enumerate(leaderboard[:5], start=1):
            tk.Label(self.root, text=f"{idx}. {name} - {score}/10", font=("Arial", 12)).pack()

        tk.Button(self.root, text="Play Again", command=self.create_welcome_screen).pack(pady=15)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = LegoQuizApp(root)
    root.mainloop()
