#!/usr/bin/env python3
"""ChatGPT-style web interface powered by OpenAI GPT-4o."""

import json
import os
import sys

try:
    from flask import Flask, Response, render_template, request, stream_with_context
except ImportError:
    sys.exit("flask not found. Run: pip install -r requirements.txt")

try:
    from openai import OpenAI
except ImportError:
    sys.exit("openai not found. Run: pip install -r requirements.txt")

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    sys.exit(
        "OPENAI_API_KEY not set.\n"
        "Add it to a .env file or export it:\n"
        "  export OPENAI_API_KEY=sk-..."
    )
client = OpenAI(api_key=api_key)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])
    model = data.get("model", "gpt-4o")

    def generate():
        try:
            stream = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
            )
            for chunk in stream:
                delta = chunk.choices[0].delta
                if delta.content:
                    yield f"data: {json.dumps({'content': delta.content})}\n\n"
        except Exception as exc:
            yield f"data: {json.dumps({'error': str(exc)})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Running at http://localhost:{port}")
    app.run(debug=False, port=port, threaded=True)
