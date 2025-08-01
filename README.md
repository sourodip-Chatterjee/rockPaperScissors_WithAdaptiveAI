# rockPaperScissors\_WithAdaptiveAI 🤺🤻🤼

A command-line based Rock-Paper-Scissors game in Python, powered with adaptive AI, colorful output, persistent scoring, and future plans for GUI and analytics.

---

## 🌊 Description

This isn't your average Rock-Paper-Scissors game. Built from scratch using modular Python, this game tracks user behavior, adapts to their choices using simple prediction logic, and adds layers of professional features like:

* Score tracking with early termination logic
* AI that learns your common choices
* Stylish colored outputs using `colorama`
* Match logs saved in `.txt`
* Plans for `.json`, `.csv`, GUI, and charts

---

## 🎓 Learning Journey

This project was built step by step like a real-world software application. Each phase focused on clean structure, reusability, and new learning goals.

### ✅ Phase 1: Basic CLI Game

* One file with loop, user input, random computer choice

### ✅ Phase 2: Modular Code Structure

* Split into functions: input, computer choice, logic, output

### ✅ Phase 3: Multi-file Project Structure

* Separated files: `main.py`, `gameLogic.py`, `userInput.py`, etc.

### ✅ Phase 4: Enhancements

* **4.1:** Scoreboard
* **4.2:** Colored output with `colorama`
* **4.3:** Logging results to `.txt`
* **4.4:** Best-of-N Rounds with early termination

### ✅ Phase 5: Refactoring + Edge Case Handling

* Invalid inputs
* Quitting anytime
* Score-based early game end

### ✅ Phase 6: Adding AI

* **6.1:** AI Brain: tracks user history using `defaultdict`
* Chooses counter-move based on highest picked option
* Printed move distribution to inform users

---

## 🚀 Future Plans

### 📂 Phase 6.x - Data Features

* **6.2:** JSON Save/Load Scoreboard
* **6.3:** CSV Export of logs

### 🎨 Phase 7 - GUI Version

* Tkinter / PyQt-based version of the game

### 🌐 Phase 8 - Deployment

* Convert to `.exe` using `pyinstaller`
* Add CLI argument support (eg: `--rounds 5`)

### 📊 Phase 9 - Visual Analytics

* Graph wins/losses over time with `matplotlib`
* Win-ratio dashboard from `.log` file

### 🏆 Phase 10 - Polish and Publish

* Upload final version to GitHub with release tags
* Demo video/GIFs for README
* Write a Medium article or LinkedIn post

---

## 📚 Tech Stack

* Python 3.x
* `colorama` for colorized terminal output
* `random` and `collections.defaultdict` for AI logic
* `os`, `datetime` for file handling

---

## 🤖 How to Run

```bash
# Clone the repo
https://github.com/your-username/rockPaperScissors_WithAdaptiveAI.git
cd rockPaperScissors_WithAdaptiveAI

# Run the game
python main.py
```

---

## 📢 Credits

Made with excitement, late nights, and passion for learning real-world Python project building by **Souro Dip Chatterjee**.

Thanks to Google, ChatGPT as my coding buddy, code reviewer, and Guide. ✨

---

## 🌟 License

MIT License. Use it, modify it, show it off!
