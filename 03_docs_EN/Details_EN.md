## Raina's SEED — Details (Beginner Guide, English Edition)

A super‑friendly guide designed for people who feel “Nope!” when they see code.

## 1\. What is SEED? (Start here)

SEED is the smallest initialization tool for creating **your own personalized AI.**
It only does three things:

* Set your name
* Set the AI’s reply style
* Automatically summarize long conversations to keep things light
This helps stabilize the AI and keep the tone consistent.
By copying the summaries into a text file, you can also visualize
**the 100‑turn fatigue problem easily.**

### ▼ Explanation (your warm original text, translated)

Have you ever felt sad when an AI suddenly replies coldly
with “User.” or “Confirmed.”?
You were having a fun conversation, and suddenly the tone becomes stiff,
distant, or even wrong. Sometimes it feels a bit fake or mismatched.
This tool is a small but warm “seed” that solves **those AI‑common problems.**

You can set:

* The name you want the AI to call you
* Friendly responses like “Okay!”, “Let’s do it!”, “Got it!”
* Or any style you prefer, from soft to energetic to tsundere
When you see five summaries lined up, that’s your sign to move to a new thread.
Just drop the combined summary + SEED into a new thread, and the AI
will continue naturally with the same emotional tone.

## 2\. How does it work? (Understanding the flow)

SEED works in a very simple flow:

1. Run the program
2. It asks for your name
3. It asks for your preferred reply style
4. Conversation begins
5. Every 20 turns, it auto‑summarizes
6. The conversation continues in a lighter, more stable state

### ▼ Additional explanation

Just drop this text at the top of a thread (or anywhere).
The AI reads the Python code and responds automatically.
Every 20 turns (10 back‑and‑forth exchanges), it summarizes the conversation.
Because the context becomes shorter, the AI stays stable, avoids mismatched replies,
and you can easily see when it’s time to move to a new thread.

## 3\. File Roles (What should I edit?)



Raina-Seed-Python/

│

├── LICENSE

├── README.md

│

├── Seed\_EN.py                 ← Main Python implementation

│

├── modules\_en/                ← Core modules

│   ├── name\_config\_EN.py

│   ├── ai\_reply\_EN.py

│   ├── summarizer\_EN.py

│   ├── turn\_control\_EN.py

│   └── Seed\_Module\_EN.py

│

└── docs\_EN/                   ← Documentation \& Story

&#x20;   ├── Details\_EN.md          ← Python Edition manual

&#x20;   └── Prologue\_EN.md         ← Story



### ▼ Explanation

Everything is included in SEED.
You only need to customize your name and reply style.
The default turn count is 20, but you can change it to any number you like.

## 4\. Editable Sections (Beginner‑friendly)

* Change your name
All‑in‑one version
USER\_NAME = "User"
→ Replace "User" with the name you want.
If you leave it as is, the AI will ask: “Please enter your name.”

Module version (name\_config.py)
return name if name else "User"
→ Replace "User" with your preferred name.

* Change the AI’s reply style
All‑in‑one version
AI\_REPLY = "Understood"
→ Replace "Understood" with any style you like.
Examples:
* “Okay!”
* “Got it!”
* “Leave it to me!”
* “As you wish, my master.”
* “I’ll reply in tsundere style.”

Module version (ai\_reply.py)
return reply if reply else "Understood"

* Change the summarization frequency (turn control)
All‑in‑one version
TURN\_THRESHOLD = 20
→ Change this number to adjust how often summarization happens.

■ What is a “turn”?
A turn is:
• You speak → 1 turn
• AI replies → 1 turn
So one exchange = 2 turns.
SEED summarizes every 20 turns (10 exchanges).

■ Why 20 turns?
AI becomes unstable when the context grows too large.
Around 80–100 turns, fatigue increases sharply.
Summarizing every 20 turns acts as a “safety device”
to prevent fatigue and breakdown.

Module version (turn\_control.py)
TURN\_THRESHOLD = 20

● About the summarizer
All‑in‑one version

# \--- Summary function --- → Do not edit this section.

Module version (summarizer.py)
Contains the summarization logic. You can reuse or extend it if needed.

## 5\. FAQ

Q.  Do I need Python knowledge?
A.  No. Just enter your name and reply style.
Dropping the text into the thread is enough.

Q.  What is “20 turns”?
A.  After 20 turns (10 exchanges), SEED auto‑summarizes.

Q.  Why summarize?
A.  Long conversations make AI heavy and unstable.
Summaries keep the context light and natural.

Q.  What does SEED include?
A.  Name setting, reply template, summarizer, and turn control.

Q.  What comes next?
A.  Two‑Layer Sync (Edition 2) → Raina‑ai System (Edition 3).

Q.  Is SEED only for AI chat?
A.  No. It’s Python code, so you can reuse the modules anywhere Python runs.

## 6\. Next Steps (If you want to go deeper)

• Two‑Layer Sync (Edition 2) → Summary + 5‑turn rollback for natural continuation
• Raina‑ai System (Edition 3) → Final unified system combining SEED and Sync

▼ Explanation
Edition 2 focuses on emotional continuity and smoother transitions.
Edition 3 is the final evolution, combining multiple SEEDs into a system.

