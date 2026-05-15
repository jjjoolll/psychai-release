# PsychAI User Guide (Option B · Prompt Version)
# Author: Wei63 | Version: v1.1 | 2026-05-15

---

## What is this

PsychAI is a system prompt. Load it into **any conversational AI** (Claude, ChatGPT, Doubao, etc.) and it becomes a focused personal psychology analysis assistant — built on over ten clinical psychology frameworks including Big Five personality, attachment theory, defense mechanisms, schema therapy, and more. Give it material about yourself, and it builds you a psychological profile.

It's not therapy software. It has no medical function. Think of it as a conversation partner with a complete psychology knowledge base — one that can help you see parts of yourself you can't see on your own.

---

## Option A or Option B?

PsychAI comes in two versions. You're reading the **Option B (prompt) guide**.

| | Option B (this guide) | Option A |
|--|--|--|
| How it works | Paste a prompt into any AI | Claude Code local Skill |
| Setup required | None — works instantly | ~30 minutes to install |
| Standout feature | Works with any AI, free tier is fine | Auto-reads local files, profile saves permanently |
| Best for | Users who want to try it quickly | Users who want the full automated experience |

For a more complete experience, see the [**Option A guide**](../../skill/simpcn/psychai_readme_A_simpcn.md).

---

## What you need to get started

**You need:**
- Any conversational AI account, for example:
  - **Claude** (claude.ai) — free tier works, Pro gives longer context
  - **ChatGPT** (chat.openai.com) — free tier works, GPT-4o gives better results
  - **Doubao**, **Kimi**, **DeepSeek**, or any other AI assistant
- About 5–10 minutes for the initial questionnaire

**You don't need:**
- Any technical knowledge
- A psychology background
- Material prepared in advance (you can share things as you go)

---

## How to use it

**Step 1: Get the prompt file**

Open `psychai_prompt_v1_en.md` from the package, and copy everything below the line that says "Copy the system prompt from here." Or upload the file directly into your AI conversation — no copy-pasting needed.

**Step 2: Load the prompt**

Three ways to do it — pick one:

- **Option A (recommended, Claude)**: Create a new Project on claude.ai, go to Project settings, and paste the prompt into the "System prompt" field. Every conversation in that Project automatically loads the assistant — no need to repeat.

- **Option B (upload)**: Upload `psychai_prompt_v1_en.md` directly into your conversation. The AI reads the file automatically. Works on Claude, ChatGPT, and others.

- **Option C (universal)**: Open a new conversation on any AI platform, send the prompt text as your first message, then continue from there. You'll need to resend it each new conversation.

**Step 3: Follow its lead**

It'll introduce itself, then guide you through a few questions. There are no right or wrong answers — the more specific you are, the more accurate the analysis. You can also skip the questionnaire and hand it material directly to start.

---

## What material works best

| Type | Notes |
|------|-------|
| **Journal / freewriting** | Anything you've written about yourself, your feelings, or events |
| **Chat logs** | Conversations with friends, family, or partners (just copy-paste) |
| **Transcribed recordings** | Recordings of yourself or conversations with others, converted to text |
| **Casual writing** | Doesn't need to be polished — fragments are fine |
| **Direct conversation** | No material needed — just talking to it works too |

More material generally means more accurate analysis — behavior patterns become clearer with more data.

---

## Saving progress across conversations (snapshot feature)

Most AIs don't remember previous conversations when you start a new one. PsychAI solves this with snapshots:

**Generating a snapshot**: After the first full analysis, it automatically appends a `[PsychAI Profile Snapshot]` block at the end — a structured summary of your current profile.

**Using a snapshot**: Next time you start a new conversation, paste the snapshot at the very beginning. It'll pick up from where your profile left off — no questionnaire needed.

**Updating a snapshot**: After each new batch of material with meaningful updates, it'll automatically attach a new snapshot. Save the new one over the old one.

Tip: Keep your latest snapshot somewhere easy to access — a notes app, a document — so you can paste it in quickly.

---

## What it can't do

- **Not therapy**: Its analysis is based on what you share in text — it can't replace an in-person professional assessment
- **No medical function**: It can't diagnose any mental health condition or prescribe any treatment
- **No data storage**: Everything lives only in your AI conversation — when you close it, it's gone (which is why the snapshot matters)
- **Limited to what you share**: It can only work with what you're willing to tell it

If things are already significantly affecting your daily life, please reach out to a qualified mental health professional.

---

## FAQ

**Q: Which AI should I use?**
Use whichever you're most comfortable with. Claude and ChatGPT have longer context windows — better for processing large amounts of material without getting cut off. Other AIs work fine too, especially for lighter use. Free tiers are generally enough to start.

**Q: What about my privacy?**
Your conversations are handled by whichever AI platform you use. PsychAI itself collects no data. Privacy policies vary by platform — check the official documentation for the AI you're using. If privacy is a concern, you can anonymize names and sensitive details when sharing material.

**Q: How accurate is the analysis?**
It makes inferences from what you share — the more honest and complete the material, the closer the analysis gets to reality. If a conclusion doesn't match your own understanding, just tell it. It updates based on your corrections. Your self-knowledge always takes priority over its inferences.

**Q: Can it analyze other people too?**
Yes. You can give it material about someone else (like a chat log with them) and ask it to analyze that person, or the dynamic between the two of you.

**Q: Does it work in languages other than Chinese?**
Yes. If you talk to it in English, it understands and responds in English. There's also a simplified Chinese version and a traditional Chinese version of this guide in the same package.

---

## License

© Wei63, 2026

This project is licensed under **CC BY-NC-SA 4.0**:
- **Attribution**: Credit must be given to "Wei63" when using, sharing, or building on this work
- **NonCommercial**: No commercial use permitted
- **ShareAlike**: Derivatives must carry the same license — they also cannot be used commercially

**Commercial licensing**: Contact the author for commercial use inquiries.

Full license: [creativecommons.org/licenses/by-nc-sa/4.0](https://creativecommons.org/licenses/by-nc-sa/4.0)

---

## Feedback

This project is ongoing. If you've used it, the feedback form is here (completely optional):

https://wj.qq.com/s2/26641498/fbcf/

One sentence is enough — whether it helped, what didn't work, what you'd want added. This is an open project and I'd like to build it with everyone who uses it.

---

*Guide version v1.1 | Updates will be posted on release channels*
