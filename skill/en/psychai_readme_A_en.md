# PsychAI · Option A User Guide

**Version**: v1.1 · 2026-05-15
**Author**: Wei63
**License**: CC BY-NC-SA 4.0 (Attribution · NonCommercial · ShareAlike)
**Commercial licensing**: j0sphe8@outlook.com

---

## What is this?

PsychAI Option A is a local Skill that runs inside **Claude Code**.

Type `/psychai` and it automatically scans the text materials on your computer — chat logs, diary entries, transcribed recordings, anything you've written — then uses 11 clinical psychology frameworks to build you a comprehensive personal psychological profile. The profile is stored locally and updated continuously every time you run it; the more you use it, the more accurate it gets.

All your data stays on your computer. Nothing is uploaded to any server.

---

## Option A or Option B?

| | Option A (this guide) | Option B |
|--|--|--|
| How it works | Claude Code local Skill | Paste a prompt into any AI |
| Setup required | ~30 minutes to install | None — works instantly |
| Material reading | Auto-scans your local folder | Manual copy-paste |
| Profile storage | Saved locally, continues seamlessly across sessions | Must paste snapshot manually each new conversation |
| Best for | Users who want the full experience and don't mind initial setup | Users who want to try it quickly |

**I recommend Option A.** The setup bar is a bit higher than B, but you only do it once — after that, everything is automatic: materials are read automatically, your profile is updated automatically, and analysis accumulates over time without any manual effort. That's an experience B simply can't match.

If you just want to try it first, start with **Option B** and come back to set up A once you're sold on it.

---

## Installation video tutorial

> 📹 Video tutorial link (coming soon)

Watching the video before reading the steps below is recommended — it walks through the full process from installation to first run.

---

## What you need

> ⚠️ **Windows and macOS use different Skill files. Download the version that matches your system.**

### Required
- A **Claude account** with an active **Pro plan** ($20/month)
  - Sign up at claude.ai
  - Pro gives you Claude Code access — no separate API key needed
- **Python 3.11 or later**
  - Windows: download the installer from python.org; check "Add to PATH" during installation
  - macOS: run `brew install python@3.11` in Terminal (requires Homebrew)

### Note for users in mainland China
Accessing Claude requires:
- **A reliable proxy** with nodes that support Claude (some nodes are blocked)
- **A non-mainland phone number** to register at claude.ai
- **An international credit card or PayPal** to subscribe to Pro (Alipay/WeChat Pay not supported)

> If these aren't available to you right now, start with Option B — it works with domestic AI services.

### Optional (WeChat chat log reading)
- **WeFlow** (Windows only): decrypts your local WeChat database so PsychAI can read your chat history directly
  - Download: https://github.com/hicccc77/WeFlow
  - No extra configuration needed after installation — PsychAI detects it automatically

---

## Installation steps

### Step 1 · Install Claude Code

Open a terminal (PowerShell on Windows, Terminal on macOS) and run:

```
npm install -g @anthropic-ai/claude-code
```

> If `npm` is not found, install Node.js first: https://nodejs.org (download the LTS version)

Verify the installation:
```
claude --version
```
A version number means success.

### Step 2 · Log in to your Claude account

Run:
```
claude
```

On first launch, it will prompt you to authorize in a browser. Follow the prompt and log in with your claude.ai account. Once logged in, close the browser and return to the terminal.

### Step 3 · Download the PsychAI file

Download the Skill file from GitHub:

| File | Note |
|------|------|
| `psychai_skill_windows_en.md` (Windows) or `psychai_skill_mac_en.md` (macOS) | Choose the version that matches your system |

> The file extraction script `extract_text.py` is created automatically on first run — **you do not need to download it manually**.

### Step 4 · Place the Skill file

Move the downloaded skill file (`.md`) into this directory:

**Windows**:
```
C:\Users\YourUsername\.claude\commands\
```

**macOS**:
```
~/.claude/commands/
```

> If the `commands` folder doesn't exist, create it manually.

You can rename the file anything you like, but keep the `.md` extension. The trigger command `/psychai` is defined inside the file and is not affected by the filename.

### Step 5 · Install Python dependencies

In your terminal, run:

```
pip install python-docx
```

If you need to process PDF files, also run:
```
pip install pdfplumber
```

### Step 6 · [Optional] Install WeFlow (Windows WeChat users)

WeFlow decrypts your local WeChat database so PsychAI can read your chat history directly.

1. Download the latest version from https://github.com/hicccc77/WeFlow
2. Run WeFlow and follow the in-app prompts to export your WeChat data
3. PsychAI will automatically detect WeFlow's output path on startup

---

## Quick verification

After installation, navigate to your working directory in a terminal and launch Claude Code:

```
claude
```

Then type:

```
/psychai
```

PsychAI will check the environment and start the onboarding flow. If you see a welcome message and the questionnaire begins, the installation is successful.

---

## What materials work best

Once installed, place your text materials in the `input/` folder inside your working directory — PsychAI will scan them automatically. These material types work best:

| Material type | Notes |
|--------------|-------|
| **Chat logs** | Conversations with friends, family, or partners (WeChat export or manual copy both work) |
| **Diary / journal entries** | Anything you've written about yourself, your emotions, or events — no need to be polished |
| **Transcribed recordings** | Recordings of yourself talking, or conversations with others, converted to text |
| **Casual writing** | Fragments are fine — nothing needs to be complete |

More material means more accurate analysis — the more behavioral patterns PsychAI can see, the better the profile.

---

## How to update

When a new version is released:

1. Download the new skill file from GitHub
2. Replace the old file in `~/.claude/commands/`

No other reinstallation needed. See [CHANGELOG](../../CHANGELOG.md) for what changed in each release.

---

## FAQ

**Q: Running `/psychai` gives "command not found"?**
Check that the skill file is in the correct directory (`~/.claude/commands/`) and that the file extension is `.md`.

**Q: "Python not found" error?**
Windows: confirm you checked "Add to PATH" during Python installation, or use the full path to run it. macOS: try `python3 --version` to confirm the version.

**Q: WeFlow can't detect WeChat data?**
Make sure WeChat has been logged in on this device before, and that WeFlow has completed its initial export. In some cases you may need to run WeFlow as administrator.

**Q: Where are my analysis results saved?**
In the `analysis/` folder inside your working directory, by default.

**Q: What's the difference between Claude Pro and an API key?**
Option A only requires a Claude Pro subscription — no API key needed. Both can power Claude Code, but for most users Pro is the simpler and cheaper option.

---

## Contact and feedback

- **User experience survey**: https://wj.qq.com/s2/26641498/fbcf/
- **Commercial licensing / partnerships**: j0sphe8@outlook.com
- **Bug reports**: GitHub Issues

---

*PsychAI · Wei63 · CC BY-NC-SA 4.0*
