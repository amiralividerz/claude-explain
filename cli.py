#!/usr/bin/env python3
"""
claude-explain: Explain any code snippet using Claude AI.
"""

import os
import sys
import json

try:
    import requests
except ImportError:
    print("Error: 'requests' library not found. Run: pip install requests", file=sys.stderr)
    sys.exit(1)


API_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-3-haiku-20240307"
SYSTEM_PROMPT = (
    "You are a helpful code explainer. "
    "When given a code snippet, explain clearly and concisely what it does. "
    "If the user's code or context is in Persian (Farsi), respond in Persian. "
    "Otherwise respond in English. "
    "Be brief, friendly, and avoid unnecessary jargon. "
    "Output only the explanation — no preamble, no markdown code blocks, no extra commentary."
)


def get_api_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        print(
            "Error: ANTHROPIC_API_KEY environment variable is not set.\n"
            "Get your API key at: https://console.anthropic.com\n"
            "Then run:  export ANTHROPIC_API_KEY='sk-ant-...'",
            file=sys.stderr,
        )
        sys.exit(1)
    return key


def read_code() -> str:
    """
    Priority:
      1. Command-line argument(s)
      2. Piped stdin (non-interactive)
      3. Interactive stdin prompt
    """
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:]).strip()

    if not sys.stdin.isatty():
        code = sys.stdin.read().strip()
        if code:
            return code
        print("Error: No code received from stdin.", file=sys.stderr)
        sys.exit(1)

    # Interactive fallback
    try:
        print("Enter code to explain (single line): ", end="", flush=True)
        code = input().strip()
    except (EOFError, KeyboardInterrupt):
        print("\nAborted.", file=sys.stderr)
        sys.exit(1)

    if not code:
        print("Error: No code provided.", file=sys.stderr)
        sys.exit(1)

    return code


def explain_code(code: str, api_key: str) -> str:
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    payload = {
        "model": MODEL,
        "max_tokens": 512,
        "system": SYSTEM_PROMPT,
        "messages": [
            {
                "role": "user",
                "content": f"Explain this code:\n\n{code}",
            }
        ],
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
    except requests.exceptions.ConnectionError:
        print(
            "Error: Could not connect to the Anthropic API.\n"
            "Check your internet connection and try again.",
            file=sys.stderr,
        )
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("Error: The API request timed out. Please try again.", file=sys.stderr)
        sys.exit(1)

    if response.status_code == 401:
        print(
            "Error: Invalid API key.\n"
            "Make sure ANTHROPIC_API_KEY is set correctly.\n"
            "Get your key at: https://console.anthropic.com",
            file=sys.stderr,
        )
        sys.exit(1)
    elif response.status_code == 429:
        print(
            "Error: Rate limit exceeded. Please wait a moment and try again.",
            file=sys.stderr,
        )
        sys.exit(1)
    elif response.status_code != 200:
        try:
            err = response.json().get("error", {}).get("message", response.text)
        except Exception:
            err = response.text
        print(f"Error: API returned status {response.status_code}: {err}", file=sys.stderr)
        sys.exit(1)

    try:
        data = response.json()
        return data["content"][0]["text"].strip()
    except (KeyError, IndexError, json.JSONDecodeError) as exc:
        print(f"Error: Unexpected API response format: {exc}", file=sys.stderr)
        sys.exit(1)


def main():
    api_key = get_api_key()
    code = read_code()

    if not code:
        print("Error: Code snippet is empty.", file=sys.stderr)
        sys.exit(1)

    explanation = explain_code(code, api_key)
    print(explanation)


if __name__ == "__main__":
    main()
