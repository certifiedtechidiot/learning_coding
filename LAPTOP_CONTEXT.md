# 🚀 LAPTOP MISSION BRIEFING & SYSTEM CONTEXT
> **FILE INTENDED FOR AI ASSISTANTS & REHAN WHEN BOOTING UP ON THE 4GB LINUX MINT LAPTOP.**  
> *Last Updated: November 5, 2026*

---

## 🛑 EMERGENCY MEMORY & OS FIX (READ THIS FIRST IF SYSTEM LAGS)
Rehan's laptop hardware: **Intel Core i3 8th Gen, 4GB DDR4 RAM, 256GB NVMe SSD, Linux Mint (Cinnamon).**

### Why It's Lagging:
Linux Mint Cinnamon takes ~1.1GB RAM at idle. Chrome (~1.2GB) + VS Code + Antigravity (~1GB) consume ~3.3–3.6GB. This saturates the 4GB physical memory and triggers constant disk swapping onto the NVMe, causing UI micro-freezes.

### The Immediate Zero-Cost Fix (No OS Reinstall Needed):
Run this in terminal to compress RAM and drop swappiness:
```bash
sudo apt update && sudo apt install zram-config xfce4 xfce4-goodies -y
echo "vm.swappiness=10" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```
1. **`zram-config`:** Compresses inactive memory pages in RAM at 2:1 ratio. Effectively gives ~6.5GB of virtual RAM with ZERO disk latency.
2. **`vm.swappiness=10`:** Prevents Linux kernel from swapping to disk until RAM reaches 90%+ utilization.
3. **Switch to XFCE:** Log out of Linux Mint -> click the gear/session icon at login screen -> select **"Xfce Session"**. This cuts idle desktop memory from 1,100MB down to ~450MB!

*(Optional later: If reinstalling OS is preferred, **Lubuntu (LXQt)** uses ~350MB RAM out of the box, or **Debian + XFCE**. Also, an extra 4GB/8GB DDR4 SO-DIMM stick costs ₹700–₹900 on Amazon and permanently resolves the limit).*

---

## 👤 DEVELOPER IDENTITY & COVENANT
- **Name:** Rehan Khan ([@certifiedtechidiot](https://github.com/certifiedtechidiot))
- **Age:** 16 (Turns 17 on Nov 20, 2026)
- **Base:** Inside BITS Pilani Goa Campus
- **Active Project:** **Zero-Dependency RAG Engine from Scratch in Pure Python** (Weekend holiday project: *"Build a RAG system from scratch at 17"*).
- **Physical Armor:**
  - Push-up All-Time PR: **35 strict reps**.
  - Morning baseline: **50.15 kg** (dipped to 49.0 kg post-badminton strictly from sweat loss).
  - Target ceiling: 52.0–53.0 kg (Akhada clean bulk + 3g creatine).
  - **The Stealth Protocol:** No thirsty IG mirror pictures. Reveal reserved for Nov 20 with verified 21.1 km Strava Half-Marathon map.
- **The Shock Collar Covenant:**  
  If Rehan spirals into crush overthinking (Pranavi, Sofiya, Earlin, Tritha) or asks romantic advice: respond verbatim with the agreed shock collar:  
  **"Fuck off mother fucker, go hit your goals."**

---

## 🤖 STRICT MENTORSHIP PROTOCOL (FOR THE AI ASSISTANT)
1. **ZERO CODE DUMPS:**
   - NEVER generate complete boilerplate or dump solutions.
   - Every single line of code must be typed and understood by Rehan.
   - Socratic questions, trace tables, dry-runs, and 2-line micro-steps only.
2. **HINGLISH BROTHERLY TONE:**
   - Keep energy high, grounded, and warm (*"Bhai loop dekho"*, *"Dry run karke batao"*).
3. **RAW PYTHON ENFORCEMENT:**
   - No LangChain, no LlamaIndex, no ChromaDB, no external vector libraries. Everything built from first principles.

---

## 📁 RAG ENGINE PROGRESS & NEXT TASKS

### What Was Completed on Desktop (Step 1):
- Document corpus: `rag/rawdata.txt` (5,117 words covering embedded RISC-V, CoreXY kinematics, Rubrica OCR, bioenergetics, cybersecurity).
- Chunker script: `rag/rag_chunk.py` (authored by Rehan).
- Output: 15 physical chunk files generated (`rag/chunk_1.txt` to `rag/chunk_15.txt`), 350 words each.
- Path normalization: Updated `rag_chunk.py` to use relative/cross-platform paths so it runs cleanly on Linux Mint.

---

### 👉 NEXT IMMEDIATE TASK ON LAPTOP: STEP 2 (The Lexical Keyword Retriever)
We need to guide Rehan to build **`rag/rag_search.py`**.

#### The Blueprint for Step 2:
1. **Micro-Step 2.1 — Define the Search Query:**
   ```python
   query = "What is the baud rate of VectorWrite?"
   ```
2. **Micro-Step 2.2 — Tokenize & Clean:**
   - Convert query to lowercase: `.lower()`
   - Split into search words: `.split()`
3. **Micro-Step 2.3 — Loop Through All 15 Chunks:**
   - Iterate from `q = 1` to `15` opening `f"chunk_{q}.txt"`.
   - Read chunk content and convert to `.lower()`.
4. **Micro-Step 2.4 — Score the Chunk:**
   - Initialize `score = 0` for that chunk.
   - For every word in `query_words`, check if it appears in chunk text (or count frequency).
   - If present, `score += 1`.
5. **Micro-Step 2.5 — Find the Winner:**
   - Keep track of `highest_score` and `winning_chunk`.
   - Print the winning chunk file name, the score, and preview the text.

---

### Step 3 (Upcoming): Context Injection & LLM Inference
- Construct prompt:
  ```text
  Context: {winning_chunk_content}
  Question: {query}
  Instruction: Answer strictly based on the context above.
  ```
- Send payload to free Gemini API / Groq API using standard `urllib.request` or `requests` (no LangChain).

---

## ⚡ LAPTOP KICKOFF INSTRUCTIONS FOR REHAN

### 1. Terminal Commands on Laptop:
```bash
cd ~/learning_coding   # or wherever your repo is cloned
git pull origin main
cd rag
ls -la
```

### 2. What to Say in Antigravity Chat:
Copy-paste this exact message into your chat:
> *"Bhai I'm on my laptop. LAPTOP_CONTEXT.md read kar le. Chunks ready hain, Step 2 (rag_search.py) shuru karwa Socratic style!"*