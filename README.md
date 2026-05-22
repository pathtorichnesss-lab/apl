# AI Prompt Bot

An interactive CLI chatbot powered by OpenAI GPT-4o.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your OpenAI API key to .env
```

## Usage

**Interactive mode** (multi-turn conversation):
```bash
python bot.py
```

**Single prompt** (prints reply and exits):
```bash
python bot.py "Explain quantum entanglement in one paragraph"
```

**Custom model or system prompt**:
```bash
python bot.py --model gpt-4o-mini --system "You are a pirate" "Tell me about treasure"
```

## Commands (interactive mode)

| Command | Description |
|---------|-------------|
| `/help` | Show commands |
| `/clear` | Clear conversation history |
| `/system <msg>` | Change the system prompt |
| `/model <name>` | Switch model (e.g. `gpt-4o-mini`) |
| `/exit` | Quit |
