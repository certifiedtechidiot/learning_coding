# 🧠 ZERO-DEPENDENCY RAG ENGINE FROM SCRATCH
### *Architectural Blueprint, Development History & State Machine*
> **Author:** Rehan Khan ([@certifiedtechidiot](https://github.com/certifiedtechidiot))  
> **Classification:** Sovereign Technical Portfolio / Core Systems Sprint  
> **Target:** Pure Python (Zero LangChain, Zero LlamaIndex, Zero ChromaDB, Zero Heavy Dependencies)  
> **Status:** Phase 1 Complete (Chunker Operational) ➔ Phase 2 Active (Lexical Retriever)

---

## 📌 1. EXECUTIVE MISSION & FIRST PRINCIPLES
Why build a RAG (Retrieval-Augmented Generation) system from scratch?

> *"Vibe coding sucks when something breaks."*  
Most developers in 2026 assemble 400MB npm/pip packages (`langchain`, `llama-index`, `pinecone`) without understanding a single line of memory management, tokenization, or vector math. When the pipeline silently hallucinates or crashes, they are helpless.

By engineering every component in pure standard-library Python:
1. **Zero Black Boxes:** You know exactly where every byte of memory goes.
2. **Extreme Portability:** Runs effortlessly on a potato 4GB RAM laptop or an embedded Linux box.
3. **Authentic Systems Engineering:** High-impact resume proof: *"Engineered a zero-dependency RAG engine from scratch in pure Python at 17."*

---

## 🏗️ 2. SYSTEM ARCHITECTURE PIPELINE

```
+-------------------------------------------------------------------------+
|                        RAW KNOWLEDGE CORPUS                             |
|       (rawdata.txt: 5,117 Words of Hardware/Kinematics/Cyber Specs)     |
+-------------------------------------------------------------------------+
                                    |
                                    v  [PHASE 1: CHUNKER - DONE]
+-------------------------------------------------------------------------+
|                       DETERMINISTIC SLICER                              |
|   rag_chunk.py: Read -> .split() -> Window 350 words -> 15 Chunk Files  |
|                  [chunk_1.txt ... chunk_15.txt]                         |
+-------------------------------------------------------------------------+
                                    |
                                    v  [PHASE 2: RETRIEVER - ACTIVE]
+-------------------------------------------------------------------------+
|                     LEXICAL KEYWORD RETRIEVER                           |
| rag_search.py: Clean Query -> Tokenize -> Scan Chunks -> Count Overlap  |
|                     Argmax(Score) -> Winning Chunk                      |
+-------------------------------------------------------------------------+
                                    |
                                    v  [PHASE 3: INJECTION - UPCOMING]
+-------------------------------------------------------------------------+
|                       CONTEXT AUGMENTED PROMPT                          |
|         "Context: {chunk} \n Question: {q} \n Answer strictly..."       |
+-------------------------------------------------------------------------+
                                    |
                                    v  [PHASE 4: INFERENCE - UPCOMING]
+-------------------------------------------------------------------------+
|                  ZERO-DEPENDENCY LLM GENERATION                         |
|      urllib.request -> Gemini / Groq API -> Parse JSON -> Output        |
+-------------------------------------------------------------------------+
```

---

## 📜 3. WHAT WAS BUILT IN PREVIOUS CHATS (PHASE 1 CHUNKER)

### The Problem Solved:
LLMs have finite context windows and get confused when fed an entire 50-page manual at once. We needed a clean, deterministic script to segment a raw 5,117-word document (`rawdata.txt`) into bite-sized semantic files.

### The Code Authored by Rehan (`rag_chunk.py`):
```python
import os

target = "rawdata.txt" if os.path.exists("rawdata.txt") else os.path.join(os.path.dirname(__file__), "rawdata.txt")
with open(target, "r", encoding="utf-8") as f:
    x = f.read().split()

z = 350
q = 1
for i in range(0, len(x), 350):
    filename = f"chunk_{q}.txt"
    with open(filename, "w", encoding="utf-8") as f_out:
        f_out.write(" ".join(x[i:z]))
    z += 350
    q += 1
```

### Bugs Encountered & First-Principles Lessons:
1. **Windows Path Unicode Escape:**  
   - *Bug:* `SyntaxError: (unicode error) 'unicodeescape'` when path had `\U...`.  
   - *Fix:* Prefix path strings with `r"..."` or use forward slashes `/`. Now modernized to dynamic `os.path` relative paths for Linux Mint compatibility.
2. **File Wrapper vs String:**  
   - *Bug:* `print(f)` printed `<_io.TextIOWrapper...>` instead of text.  
   - *Fix:* Must explicitly invoke `.read()` on the file descriptor.
3. **List Serialization:**  
   - *Bug:* `f_out.write(x[i:z])` threw `TypeError: write() argument must be str, not list`.  
   - *Fix:* Glued slice elements into a single string using `" ".join(x[i:z])`.
4. **File Overwrite Protection:**  
   - *Bug:* Mode `"x"` crashed with `FileExistsError` on second run.  
   - *Fix:* Switched to mode `"w"` for clean idempotency.
5. **Loop Range Boundary:**  
   - *Bug:* `for i in range(0, z+350, 350)` ran only once because `z=0` meant stop was 350.  
   - *Fix:* Bound loop stop condition to `len(x)` (total word count).

### Verified Receipts:
- 15 physical chunk files generated: `chunk_1.txt` through `chunk_15.txt`.
- Each chunk contains exactly ~350 words of rich technical data.

---

## 🎯 4. PHASE 2: THE LEXICAL KEYWORD RETRIEVER (ACTIVE SPRINT)

### Core Objective:
Create `rag_search.py`. Given an arbitrary user query (e.g., *"What is the baud rate of VectorWrite?"*), find the single chunk file that holds the correct answer **without using AI or embeddings**.

### Algorithmic Blueprint:
1. **Query Tokenization:**
   - Raw query string: `query = "What is the baud rate of VectorWrite?"`
   - Clean & lowercase: `tokens = query.lower().split()`
   - Tokens become: `['what', 'is', 'the', 'baud', 'rate', 'of', 'vectorwrite?']`
2. **Chunk Corpus Iteration:**
   - Loop `i` from `1` to `15`:
     - Open and read `f"chunk_{i}.txt"`.
     - Lowercase chunk text: `chunk_text = f.read().lower()`
3. **Scoring Function (Term Overlap):**
   - For every `word` in `tokens`:
     - If `word in chunk_text`: `score += 1` (or add frequency).
4. **Argmax Tracking:**
   - Maintain `best_score = -1` and `winning_chunk = ""`.
   - If current `score > best_score`:
     - Update `best_score = score`
     - Update `winning_chunk = filename`
5. **Output Verification:**
   - Print: `f"Top Chunk: {winning_chunk} with Score: {best_score}"`
   - Print first 200 characters of winning chunk to verify visually.

---

## 🚀 5. PHASE 3 & 4: CONTEXT INJECTION & PURE-PYTHON LLM CALL

### The Master Prompt Structure:
```text
System: You are an expert technical documentation assistant.
Context:
\"\"\"{winning_chunk_content}\"\"\"

Question: {user_query}

Instruction: Answer the question strictly using the provided context above. 
If the information is not present, respond with: "Data unavailable in knowledge base."
```

### The Zero-Dependency API Call:
Using Python's standard `urllib.request` (zero `pip install requests` needed):
```python
import json
import urllib.request

# Payload construction for Gemini / Groq free endpoint
# Deterministic temperature = 0.0 or 0.2
```

---

## 📂 6. DIRECTORY STRUCTURE

```
learn coding/
├── LAPTOP_CONTEXT.md              # Hardware, OS & laptop quick-start
├── AGENTS.md                      # AI Coaching instructions & rules
├── HOW_TO_CODE_WITH_ME.md         # Device transition guide
├── THE_20_QUESTION_GAUNTLET.md    # Algorithmic sprint ladder
├── LEVEL_OF_REHAN_IN_CODING.md    # Progress receipts
└── rag/
    ├── RAG_CONTEXT.md             # << THIS MASTER ARCHITECTURAL DOCUMENT >>
    ├── rawdata.txt                # 5,117-word raw corpus
    ├── rag_chunk.py               # Chunker (Finished)
    ├── rag_search.py              # Lexical Retriever (Active task)
    ├── chunk_1.txt                # Sliced text chunks (1 to 15)
    └── ...
```

---

## 🛑 STRICT RULES FOR ANY AI ASSISTANT WORKING ON THIS
- **No Code Dumps:** Do NOT write `rag_search.py` for Rehan.
- **Socratic Increments:** Ask him how he wants to structure the loop, how he wants to handle case sensitivity, and let him write the logic.
- **Dry-Run Enforced:** Make him trace with sample variables before executing.