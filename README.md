
![511a34f1-0a56-4ac0-af82-97d9b1bbe5f5](https://github.com/user-attachments/assets/39d6d407-4aaa-42dd-ad62-38869f3320f4)

# ❓ Quiz Game

A fully functional command-line **True/False quiz game** built in Python using **Object-Oriented Programming**.  
This project allows users to answer a series of trivia questions and tracks their score in real time.

🧠 Designed to be clean, modular, and extendable — powered by custom classes like `Question`, `QuizBrain`, and a data-driven approach.

---

## 🚀 Features

- 🧩 Multiple modules for clean separation of logic (`question_model.py`, `quiz_brain.py`, `data.py`)
- 🔁 Dynamic question loop based on remaining questions
- ✅ Real-time answer validation and score tracking
- 👓 Final score display on game completion
- 🎨 ASCII art logo for a fun CLI experience
- 💡 Built using OOP principles: classes, instances, encapsulated logic

---

## 📁 Project Structure

1. main.py - Main game controller
2. question_model.py - Question class (blueprint for each quiz item)
3. quiz_brain.py - Core quiz logic (loop, scoring, validation)
4. data.py - Trivia data bank (text + answers)
5. art.py - ASCII logo


---

## 🧠 What I Learned

- How to structure multi-file Python projects
- Building and instantiating custom classes (`Question`, `QuizBrain`)
- Managing user input and validation through control flows
- Using lists and loops to iterate dynamic quiz logic
- Returning and comparing data cleanly using OOP methods

---

## 🛠 How to Run

1. Make sure Python is installed.
2. Place all files (main.py, quiz_brain.py, question_model.py, data.py, art.py) in the same directory.
3. Run the app: python main.py

---

## 📚 Course Credit

- Project from Day 17 of the 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu.

---

## 🔗 Connect With Me:

- 📍 LinkedIn: linkedin.com/in/mussa-tariq-0652712a0
- 🐍 Follow more of my Python journey and fun CLI apps on GitHub!
---

## 🖼️ Preview (CLI Output)

```bash
 _____  __  __  ____  ____         ___    __    __  __  ____   
(  _  )(  )(  )(_  _)(_   )       / __)  /__\  (  \/  )( ___)  
 )(_)(  )(__)(  _)(_  / /_       ( (_-. /(__)\  )    (  )__)   
(___/\\(______)(____)(____)       \___/(__)(__)(_/\/\_)(____)  

Q1: A slug's blood is green. (True/False): True
You've got it right!
The correct answer was: True
Your correct score is: 1/1

Q2: The loudest animal is the African Elephant. (True/False): False
You've got it right!
The correct answer was: False
Your correct score is: 2/2


...

Congrats! You have completed the quiz
Your final score was: 10/12


