# 🪨 Rock Paper Scissors

A clean, modular, and object-oriented implementation of the classic **Rock Paper Scissors** game in Python.

This project was developed as part of my journey toward becoming a Machine Learning and AI Engineer. Although the game itself is simple, the primary objective of this project was to practice professional software development concepts such as object-oriented programming, modular project architecture, clean code principles, software design, and unit testing.

---

## 📖 Overview

This project recreates the traditional Rock Paper Scissors game where a human player competes against the computer.

Instead of writing everything in a single file, the project is designed using a modular architecture where each module has a single responsibility. This makes the code easier to understand, maintain, test, and extend.

The project emphasizes writing readable, reusable, and scalable Python code rather than simply making the game functional.

---

## ✨ Features

- 🎮 Interactive command-line interface
- 👤 Human vs Computer gameplay
- 🎲 Random computer moves
- ✅ Input validation
- 🧩 Modular project architecture
- 🏗️ Object-Oriented Programming (OOP)
- 📦 Python Enums for game states
- 📝 Centralized message management
- ⚖️ Separated game logic from user interface
- 🧪 Unit testing using pytest
- 📖 Well-structured and documented code
- 🔧 Easily extensible architecture

---

## 🧠 Software Engineering Concepts

This project demonstrates the following programming concepts:

- Object-Oriented Programming (OOP)
- Classes and Objects
- Inheritance
- Polymorphism
- Method Overriding
- Enumerations (Enum)
- Dictionaries
- Type Hinting
- Docstrings
- Modular Programming
- Separation of Concerns
- Single Responsibility Principle (SRP)
- Single Source of Truth (SSOT)
- Clean Code
- Refactoring
- Unit Testing
- Project Organization

---

## 📂 Project Structure

```
rock-paper-scissors/
│
├── main.py                 # Application entry point
├── game.py                 # Game controller
├── player.py               # Player classes
├── rules.py                # Game logic
├── constants.py            # Enums and constants
├── messages.py             # User interface messages
├── utils.py                # Utility functions
├── requirements.txt
├── README.md
│
├── tests/
│   └── test_rules.py
│
└── .gitignore
```

---

## ⚙️ How It Works

The project is organized into several independent modules.

### main.py

The application's entry point.

Creates the game object and starts the program.

---

### game.py

Acts as the game controller.

Responsible for:

- Displaying menus
- Managing the game loop
- Getting player moves
- Calling the game rules
- Displaying results

---

### player.py

Contains the player classes.

- Base Player class
- HumanPlayer
- ComputerPlayer

Each player implements its own strategy for choosing a move.

---

### rules.py

Contains all game logic.

Determines:

- Win
- Lose
- Tie

The game rules are completely separated from the user interface.

---

### constants.py

Stores shared constants and enums such as:

- Move
- Result

Using enums improves readability and avoids magic numbers.

---

### messages.py

Stores every message displayed to the user.

Keeping all interface text in one location makes future modifications and localization much easier.

---

### tests/

Contains automated unit tests for the game logic.

The tests verify that every possible combination of moves produces the expected result.

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/AradCharon/RockPaperScissors.git
```

Move into the project directory:

```bash
cd RockPaperScissors
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

```bash
python main.py
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📝 Example

```
==============================
ROCK PAPER SCISSORS
==============================
1. Play Game
2. Exit
==============================

Select option: 1

Choose your move:

1. Rock
2. Paper
3. Scissors
0. Back

You chose: Rock
Computer chose: Scissors

You win!
```

---

## 📚 Technologies Used

- Python 3
- pytest
- Git
- GitHub

---

## 🚀 Future Improvements

This project is intentionally designed to be extensible.

Possible future improvements include:

- Score tracking
- Best of 3 / Best of 5 mode
- Difficulty levels
- AI-based computer strategy
- Multiplayer mode
- Save match history
- Graphical User Interface (Tkinter or PyQt)
- Rock Paper Scissors Lizard Spock
- Statistics dashboard
- Configuration file support
- Colored terminal output
- Continuous Integration (GitHub Actions)

---

## 🎯 Learning Goals

The primary goal of this project was to practice writing professional Python code rather than simply implementing a game.

Through this project I practiced:

- Designing modular applications
- Applying object-oriented programming principles
- Separating business logic from presentation
- Writing reusable code
- Refactoring
- Creating maintainable software architecture
- Writing automated tests
- Organizing a professional GitHub repository

---

## 👨‍💻 Author

**Arad Charon**

Mathematics & Computer Science Student

Interested in:

- Artificial Intelligence
- Machine Learning
- Data Mining
- Software Engineering
- Algorithms

GitHub:
https://github.com/AradCharon

---

## ⭐ Repository

If you found this project helpful or interesting, consider giving it a ⭐ on GitHub.