#!/usr/bin/env python3
"""AI prompt bot — interactive CLI powered by OpenAI GPT-4o."""

import argparse
import os
import sys

try:
    from openai import OpenAI
except ImportError:
    sys.exit("openai package not found. Run: pip install openai")

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

SYSTEM_PROMPT_DEFAULT = "You are a helpful assistant."

HELP_TEXT = """
Commands:
  /help          Show this help
  /clear         Clear conversation history
  /system <msg>  Change the system prompt
  /model <name>  Switch model (e.g. gpt-4o, gpt-4o-mini)
  /exit          Quit
"""


def build_client() -> OpenAI:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit(
            "OPENAI_API_KEY not set.\n"
            "Export it or add it to a .env file:\n"
            "  export OPENAI_API_KEY=sk-..."
        )
    return OpenAI(api_key=api_key)


def chat(client: OpenAI, history: list[dict], model: str) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=history,
    )
    return response.choices[0].message.content


def run_interactive(client: OpenAI, model: str, system_prompt: str) -> None:
    history: list[dict] = [{"role": "system", "content": system_prompt}]
    current_model = model

    print(f"AI Prompt Bot  |  model: {current_model}  |  type /help for commands")
    print("-" * 60)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not user_input:
            continue

        if user_input.startswith("/"):
            parts = user_input.split(maxsplit=1)
            cmd = parts[0].lower()
            arg = parts[1] if len(parts) > 1 else ""

            if cmd == "/exit":
                print("Bye!")
                break
            elif cmd == "/help":
                print(HELP_TEXT)
            elif cmd == "/clear":
                history = [{"role": "system", "content": history[0]["content"]}]
                print("Conversation cleared.")
            elif cmd == "/system":
                if not arg:
                    print(f"Current system prompt: {history[0]['content']}")
                else:
                    history[0]["content"] = arg
                    print(f"System prompt updated.")
            elif cmd == "/model":
                if not arg:
                    print(f"Current model: {current_model}")
                else:
                    current_model = arg
                    print(f"Model switched to: {current_model}")
            else:
                print(f"Unknown command: {cmd}  (type /help)")
            continue

        history.append({"role": "user", "content": user_input})
        try:
            reply = chat(client, history, current_model)
        except Exception as exc:
            print(f"Error: {exc}")
            history.pop()
            continue

        history.append({"role": "assistant", "content": reply})
        print(f"\nBot: {reply}")


def run_once(client: OpenAI, prompt: str, model: str, system_prompt: str) -> None:
    history = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]
    reply = chat(client, history, model)
    print(reply)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="AI prompt bot powered by OpenAI GPT-4o",
    )
    parser.add_argument("prompt", nargs="?", help="Single prompt (non-interactive)")
    parser.add_argument(
        "--model", default="gpt-4o", metavar="MODEL",
        help="OpenAI model to use (default: gpt-4o)"
    )
    parser.add_argument(
        "--system", default=SYSTEM_PROMPT_DEFAULT, metavar="TEXT",
        help="System prompt (default: 'You are a helpful assistant.')"
    )
    args = parser.parse_args()

    client = build_client()

    if args.prompt:
        run_once(client, args.prompt, args.model, args.system)
    else:
        run_interactive(client, args.model, args.system)


if __name__ == "__main__":
    main()
