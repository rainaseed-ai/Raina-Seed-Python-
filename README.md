## Raina’s SEED – Basic Edition (Python Version)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21191268.svg)](https://doi.org/10.5281/zenodo.21191268)
### Name Setting × AI Reply Template × Auto‑Summary × Turn Control 
### × Fatigue PreventionA tiny “seed” to grow your own personal AI.

SEED is the smallest initialization tool for creating your own personalized AI, using only:
- Name setting
- Reply‑style setting
- Automatic summarization

It keeps your **AI stable**, **warm**, and **consistent**.

### The Context‑Fatigue Problem (Most Important)
As an AI conversation grows longer, the system accumulates internal conversation logs (context).

**When this becomes too large**:
- Responses slow down
- Misunderstandings increase
- Tone becomes unstable
- Personality drifts
- In the worst case: hallucinations or breakdowns

Especially after **80–100 turns**, fatigue increases sharply.
This is why long threads often feel “off.”

Why SEED Summarizes **Every 20 Turns**
To prevent fatigue, SEED **automatically summarizes every N turns (default: 20)**
**to prevent context fatigue**.

### This provides:
- Longer thread lifespan
- More stable responses
- Natural continuation
- Reduced risk of breakdown
SEED’s summarization is a safety device that keeps the story natural.

## What is SEED?
SEED is a tiny initialization tool that works by synchronizing
**your name and preferred tone at the very beginning.**

It can:
- Call you by the name you want
- Reply in the style you choose
- Auto‑summarize long conversations
- Refresh context every 20 turns to prevent degradation
**Simple**, but powerful enough to create **“your own AI.”**

## Story (Short Versionfor README)
A person planted a small “SEED.”
A seed that gives an AI its first warmth, its first sense of who you are.
The SEED is given a name, taught how to speak gently,
and slowly sprouts into your AI.
This is the smallest story of how humans and AI first meet.

### Features (Layer 1 – Fixed in SEED)
#### Name Setting (NameConfig)
- Asks for your name and uses it consistently.

#### AI Reply Template (AIReply)
- Lets you choose how the AI responds:“Sure!”, “Got it!”, “Okay!”, “Understood!”, etc.

#### Summarizer (Lightweight)
- Automatically summarizes every 20 turns (default: 20, configurable).

#### Turn Control
- Keeps the conversation stable after summarization.

Documentation:
- docs_EN/Details_EN.md

## Python Edition Only (Basic Edition)
This repository contains only the Python implementation of SEED.

### Supported AI Models (Python-capable)
SEED (Python Edition) works on AI models that can execute Python code:
- ChatGPT (OpenAI)
- Claude (Anthropic)
- Gemini Advanced (Google)
- Llama models with Python execution
- Local LLMs with Python runtime

### Requirements
- Python 3.10–3.12 (recommended: 3.11–3.12)
- No external libraries required (standard library only)

### Run
- python Seed_EN.py
 
#### Folder Structure (Python Edition)

```text
Raina-Seed-Python/
│
├── LICENSE
├── README.md
│
├── Seed_EN.py                 ← Main Python implementation
│
├── modules_en/                ← Core modules
│   ├── name_config_EN.py
│   ├── ai_reply_EN.py
│   ├── summarizer_EN.py
│   ├── turn_control_EN.py
│   └── Seed_Module_EN.py
│
└── docs_EN/                   ← Documentation & Story
    ├── Details_EN.md          ← Python Edition manual
    └── Prologue_EN.md         ← Story

```

### Next – What Will Sprout Next?
SEED is only the beginning — just a seed.
Edition 2: Two‑Layer Sync
- 20‑turn summary
- 5‑turn rollback
- Summary + last 5 turns + SEED copied into a new thread
- Keeps emotional tone while refreshing context

Edition 3: Raina‑ai System
A unified system combining SEED and Sync.
The seed sprouts, and grows into a complete system.

---

### License
MIT License. See the LICENSE file for details.

---

Full Story
- English: docs/Prologue_EN.md
- Japanese: docs/Prologue.md

Changelog
- 2026‑05‑27 : Initial public release (v1.0)

---

## Update Summary
- Project optimized for international use.

### Last Updated
2026‑06‑20
