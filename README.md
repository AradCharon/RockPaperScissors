# 🪨 Rock Paper Scissors

A clean, modular, and object-oriented implementation of the classic **Rock Paper Scissors** game in Python.

This project was developed as part of my journey toward becoming a Machine Learning and AI Engineer. Although the game itself is simple, the primary goal was to practice professional software development concepts such as object-oriented programming, modular architecture, clean code principles, software design, and unit testing.

---

## 📖 Overview

This project recreates the traditional Rock Paper Scissors game where a human player competes against the computer.

Instead of implementing the entire game in a single file, the application is organized into multiple modules, each with a single responsibility. This modular architecture improves readability, maintainability, testability, and scalability.

The focus of this project is not the complexity of the game itself, but writing clean, reusable, and well-structured Python code.

---

## ✨ Features

- 🎮 Interactive command-line interface
- 👤 Human vs Computer gameplay
- 🎲 Random computer moves
- ✅ Input validation
- 🧩 Modular project architecture
- 🏗️ Object-Oriented Programming (OOP)
- 📦 Enum-based game states
- 📝 Centralized message management
- ⚖️ Separation of game logic and user interface
- 🧪 Unit testing with pytest
- 📖 Well-documented code
- 🔧 Easily extensible design

---

## 🧠 Software Engineering Concepts

This project demonstrates the following concepts:

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

```text
rock-paper-scissors/
│
├── main.py                 # Application entry point
├── game.py                 # Game controller
├── player.py               # Player classes
├── rules.py                # Game rules and winner determination
├── constants.py            # Enums and shared constants
├── messages.py             # User interface messages
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

The project is divided into independent modules, each responsible for a specific task.

### `main.py`

Application entry point.

- Creates the game object.
- Starts the application.

---

### `game.py`

Acts as the controller of the application.

Responsibilities:

- Display menus
- Manage the game loop
- Get player moves
- Call the game rules
- Display game results

---

### `player.py`

Contains the player classes.

- Player (base class)
- HumanPlayer
- ComputerPlayer

Each player implements its own strategy for selecting a move.

---

### `rules.py`

Contains all game rules.

Responsible for determining:

- Win
- Lose
- Tie

The game logic is completely separated from the user interface.

---

### `constants.py`

Stores shared enums and constants.

Examples include:

- Move
- Result

Using enums improves readability and eliminates magic numbers.

---

### `messages.py`

Stores all user-facing messages.

Keeping interface messages in a single location simplifies maintenance and future localization.

---

### `tests/`

Contains automated unit tests.

The tests verify that every possible combination of moves produces the expected outcome.

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

Install the required dependencies:

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

```text
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

## 🎯 What I Learned

Through this project, I practiced and improved my understanding of:

- Designing modular applications
- Applying object-oriented programming principles
- Separating business logic from presentation
- Writing reusable and maintainable code
- Refactoring existing code
- Building scalable software architecture
- Writing automated unit tests
- Organizing a professional GitHub repository

---

## 🚀 Future Improvements

Possible future enhancements include:

- Score tracking
- Best of 3 / Best of 5 game modes
- Difficulty levels
- Smarter AI opponent
- Multiplayer mode
- Save match history
- Graphical User Interface (Tkinter or PyQt)
- Rock Paper Scissors Lizard Spock
- Statistics dashboard
- Configuration file support
- Colored terminal output
- GitHub Actions for Continuous Integration

---

## 👨‍💻 Author

**Arad Shafiee**

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

If you found this project useful or interesting, consider giving it a ⭐ on GitHub.
