# 💻 HOW TO CODE WITH ME ON YOUR OTHER DEVICE

Welcome to your portable coding setup! Everything you need to transition seamlessly between devices is stored right here in this GitHub repository:
👉 **`https://github.com/certifiedtechidiot/learning_coding.git`**

---

## 🚀 Step 1: Get the Code on Your Other Device

### Option A: If this is the first time on the new device:
Open your terminal (PowerShell, Command Prompt, or Terminal on macOS/Linux) and run:
```bash
git clone https://github.com/certifiedtechidiot/learning_coding.git
cd learning_coding
```

### Option B: If you already cloned it previously:
Just navigate to your folder and pull the latest progress:
```bash
cd learning_coding
git pull origin main
```

---

## 🐍 Step 2: Verify Python

Ensure Python is installed on the other device:
```bash
python --version
# or python3 --version
```
*(If not installed, download from [python.org](https://www.python.org/downloads/) and make sure to check "Add Python to PATH" during installation).*

---

## 🤖 Step 3: Resuming with Your AI Assistant

### If you are using **Antigravity** or **Cursor / Windsurf**:
The editor automatically reads **`AGENTS.md`** at the root of the project!  
All you need to type in the chat is:
> *"Bhai I'm on my new device. What's our next problem? Let's start!"*

The AI will automatically know:
- Your current rank (**Level 2.0 / 5 — Autonomous Problem Solver**)
- The strict rule: **Zero code dumps**, Socratic hints only
- No library shortcuts (`[::-1]`, `set()`, `sorted()`)
- The next problem: **Q04 — Array Rotation by `K` Steps**

### If you are using **ChatGPT / Claude / Web Chat**:
Copy and paste this quick prompt into the chat window:
```text
Hey! I am continuing my 7-Day Algorithmic Coding Sprint.
Repository context:
- Developer: Rehan (@certifiedtechidiot)
- Current Level: Level 2.0 / 5 (Autonomous Problem Solver)
- Pedagogy: Strictly Socratic method, zero code dumps, zero copy-paste solutions. Guide me line-by-line with hints and Hinglish. Do not give me code!
- Rules: Raw Python only. No [::-1], no set(), no sorted(), no sum()/len() shortcuts.
- Progress: Solved Q01 (List Reversal), Q02 (Deduplication), Q03 (Second Smallest).
- Next Challenge: Q04: Array Rotation by K Steps from THE_20_QUESTION_GAUNTLET.md.
Please present Q04 with example inputs, expected outputs, and constraints. Let's begin!
```

---

## 📂 Project Files Guide

| File | What it is |
| :--- | :--- |
| **[`THE_20_QUESTION_GAUNTLET.md`](THE_20_QUESTION_GAUNTLET.md)** | The full 20-problem algorithmic ladder (Tiers 1 to 4). Tracks checkboxes for each problem solved. |
| **[`LEVEL_OF_REHAN_IN_CODING.md`](LEVEL_OF_REHAN_IN_CODING.md)** | Your live progress log, calibrated level definitions, and real receipts of breakthroughs. |
| **[`AGENTS.md`](AGENTS.md)** | AI companion system prompt & coaching protocol (ensures the AI doesn't spoil answers). |
| **[`day1.py`](day1.py)** | Your working code repository containing your raw implementations for Day 1 problems. |
| **[`README.md`](README.md)** | Project dashboard and sprint roadmap. |

---

## 🔄 Step 4: Syncing Progress Back and Forth

Whenever you finish a problem or wrap up a coding session on any device, run:
```bash
git add .
git commit -m "Solved Q04: Array rotation with modulo mechanics"
git push origin main
```

Whenever you sit down at the other device, always start with:
```bash
git pull origin main
```

Happy coding, Rehan! You're 3 questions down, 17 to go on the Gauntlet. Let's conquer Tier 1! 🚀
