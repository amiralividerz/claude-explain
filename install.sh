#!/usr/bin/env bash
# install.sh — sets up claude-explain in a dedicated virtualenv
# Usage: bash install.sh

set -euo pipefail

VENV_DIR="$HOME/.claude-explain-env"
REPO_URL="https://github.com/your-username/claude-explain.git"

echo "======================================"
echo "  Installing claude-explain"
echo "======================================"
echo ""

# ── 1. Check Python ──────────────────────────────────────────────────────────
if ! command -v python3 &>/dev/null; then
    echo "❌  python3 not found. Please install Python 3.8+ first."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
REQUIRED="3.8"

if python3 -c "import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "✅  Python $PYTHON_VERSION found"
else
    echo "❌  Python $REQUIRED+ required (found $PYTHON_VERSION)"
    exit 1
fi

# ── 2. Create virtualenv ─────────────────────────────────────────────────────
echo ""
echo "📦  Creating virtualenv at $VENV_DIR ..."
python3 -m venv "$VENV_DIR"

# ── 3. Install package ───────────────────────────────────────────────────────
echo ""
echo "⬇️   Installing claude-explain ..."

# If we're inside the cloned repo, install locally; otherwise from GitHub
if [ -f "$(dirname "$0")/pyproject.toml" ]; then
    "$VENV_DIR/bin/pip" install --upgrade pip -q
    "$VENV_DIR/bin/pip" install -e "$(dirname "$0")" -q
    echo "✅  Installed from local source"
else
    "$VENV_DIR/bin/pip" install --upgrade pip -q
    "$VENV_DIR/bin/pip" install "git+$REPO_URL" -q
    echo "✅  Installed from GitHub"
fi

# ── 4. Create a wrapper in /usr/local/bin (optional, asks for sudo) ──────────
WRAPPER="/usr/local/bin/claude-explain"
BIN="$VENV_DIR/bin/claude-explain"

echo ""
if [ -w "/usr/local/bin" ] || sudo -n true 2>/dev/null; then
    echo "🔗  Linking to /usr/local/bin/claude-explain ..."
    sudo ln -sf "$BIN" "$WRAPPER" 2>/dev/null || ln -sf "$BIN" "$WRAPPER"
    echo "✅  Linked. You can now run: claude-explain"
else
    echo "ℹ️   Skipping /usr/local/bin link (no write permission)."
    echo "    Add the following to your shell rc file (~/.bashrc / ~/.zshrc):"
    echo ""
    echo "    export PATH=\"$VENV_DIR/bin:\$PATH\""
fi

# ── 5. API key reminder ───────────────────────────────────────────────────────
echo ""
echo "======================================"
echo "  Almost done!"
echo "======================================"
echo ""
echo "1️⃣   Get your API key at: https://console.anthropic.com"
echo "2️⃣   Export it:"
echo ""
echo "     export ANTHROPIC_API_KEY='sk-ant-YOUR_KEY_HERE'"
echo ""
echo "3️⃣   Try it:"
echo ""
echo "     claude-explain \"lambda x: x**2\""
echo ""
echo "Happy explaining! 🎉"
