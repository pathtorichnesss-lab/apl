# AI Chat

A ChatGPT-style web chat interface powered by OpenAI GPT-4o.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Paste your OpenAI API key into .env
```

## Run

```bash
python app.py
```

Then open **http://localhost:5000** in your browser.

## Features

- Dark ChatGPT-style UI
- Streaming responses (text appears as it's generated)
- Multi-turn conversation with memory
- Sidebar with chat history
- Model switcher (GPT-4o, GPT-4o mini, GPT-3.5 Turbo)
- New chat button

## CLI mode (optional)

```bash
python bot.py               # interactive terminal chat
python bot.py "your prompt" # one-shot
```
