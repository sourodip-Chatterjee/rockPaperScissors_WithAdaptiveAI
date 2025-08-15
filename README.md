# rockPaperScissors\_WithAdaptiveAI 🤺🤻🤼

A **Python-powered Rock-Paper-Scissors game** with both **Command-Line** and **Tkinter GUI** versions, featuring **adaptive AI**, colorful output, persistent scoring, and match history tracking.

---

## 🌊 Description

This isn't your average Rock-Paper-Scissors.
It’s a **learning, adapting AI opponent** built from scratch, evolving from a simple CLI game to a **full-featured GUI app**.

**Highlights:**

* CLI mode for speed and retro charm
* GUI mode with a clean Tkinter interface
* AI that tracks your habits and counters your most-used moves
* Match history viewable in-app (GUI)
* Screenshot feature for GUI game windows
* Persistent data storage (`.csv`) for analysis
* Modular, reusable code structure

---

## 🎓 Learning Journey

This project was developed in **phases**, just like real-world software.

### ✅ Phase 1 → 5: CLI Version

* Started as a single-file basic loop
* Modularized into multiple files: `main.py`, `gameLogic.py`, etc.
* Added:

  * Scoreboard with early termination
  * Colored terminal output via `colorama`
  * Match logs in `.txt`
  * Best-of-N rounds
  * AI brain (`aiBrain.py`) using `defaultdict`

### ✅ Phase 6: Adaptive AI

* Tracks your move history
* Predicts & counters your most frequent move
* Adjusts if losing streak detected

### ✅ Phase 7: GUI Version

* Built with Tkinter (`gui.py`)
* Clickable buttons for moves
* Live score updates and results display
* Integrated `aiBrain.py` logic
* **Extras**:

  * Menu bar with “Take Screenshot” option
  * Match History viewer (scrollable table from CSV)
  * Fully camelCase code style for GUI

---

## 🚀 Features

**CLI Version**

* Quick and lightweight
* Terminal colors
* Logs match results
* Same adaptive AI as GUI

**GUI Version**

* Interactive buttons for moves
* Score & result display in real time
* Match history window with scrollbar
* Screenshot saving of the game window
* AI adjusts strategy mid-game

---

## 📂 Project Structure

```
rockPaperScissors_WithAdaptiveAI/
│
├── aiBrain.py          # AI logic
├── choices.py          # Available moves
├── gui.py              # Tkinter GUI implementation
├── main.py             # Entry point (choose CLI or GUI)
├── utils/
│   └── colorUtils.py   # Color text for CLI
├── matchHistory.csv   # Saved results
└── README.md
```

---

## 📚 Tech Stack

* **Python 3.x**
* `tkinter` – GUI
* `colorama` – CLI colors
* `PIL` (Pillow) – Screenshots
* `csv` – Match history storage
* `collections.defaultdict` – AI tracking
* `random` – AI choice randomness (using it at start and when the user is loosing)

---

## 🤖 How to Run

### CLI Mode

```bash
python main.py cli
```

### GUI Mode

```bash
python main.py gui
```

**In GUI mode**:

* Use buttons to play
* View match history from menu
* Take screenshots directly from the menu

---

## 📊 Future Plans

* JSON save/load
* Graph analytics with `matplotlib`
* Deploy as `.exe` with `pyinstaller`
* Online multiplayer version

---

## 📢 Credits

Made with excitement, late nights, and passion for real-world Python project building by **Souro Dip Chatterjee**.

Special thanks to Google and ChatGPT — my coding buddy, reviewer, and guide. ✨

---

## 🌟 License

MIT License — use, modify, and share freely.


