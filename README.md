# 🔍 claude-explain

> **Instantly understand any code snippet — right from your terminal.**

![Demo](docs/demo.gif)
<!-- Replace the path above with your actual demo GIF after recording -->

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Powered by Claude](https://img.shields.io/badge/powered%20by-Claude%20AI-orange.svg)](https://www.anthropic.com)

---

## 💡 Why This Is Useful

> **Stop Googling. Start understanding.**

| Without `claude-explain` | With `claude-explain` |
|--------------------------|----------------------|
| Copy code → open browser → search Stack Overflow → read 10 answers | `claude-explain "your code"` → done ✅ |
| Spend 5 minutes understanding a regex | Get a plain-English explanation in 3 seconds |
| Ask a colleague to decode that list comprehension | Ask Claude instead, any time, offline-friendly |
| Context-switch out of your terminal | Stay in the flow 🚀 |

---

## 📦 Installation

### Option 1 — Install directly from GitHub (recommended)

```bash
pip install git+https://github.com/your-username/claude-explain.git
```

### Option 2 — Clone and install locally

```bash
git clone https://github.com/your-username/claude-explain.git
cd claude-explain
pip install -e .
```

### Option 3 — One-liner with the install script (Linux / macOS)

```bash
curl -fsSL https://raw.githubusercontent.com/your-username/claude-explain/main/install.sh | bash
```

---

## 🔑 Getting Your API Key

1. Go to **[console.anthropic.com](https://console.anthropic.com)**
2. Sign up or log in
3. Navigate to **API Keys** → **Create Key**
4. Copy the key (starts with `sk-ant-...`)

Then export it in your shell:

```bash
export ANTHROPIC_API_KEY="sk-ant-YOUR_KEY_HERE"
```

To make it permanent, add it to your `~/.bashrc`, `~/.zshrc`, or `~/.profile`:

```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-YOUR_KEY_HERE"' >> ~/.zshrc
source ~/.zshrc
```

---

## 🚀 Usage

### Pass code as an argument

```bash
claude-explain "import re; re.findall(r'\d+', 'abc123def456')"
```

### Pipe code from stdin

```bash
echo "sorted(words, key=lambda w: len(w))" | claude-explain
```

### Pipe from a file

```bash
cat my_script.py | claude-explain
```

### Interactive mode (no arguments)

```bash
claude-explain
# Enter code to explain (single line): ...
```

---

## 🎬 Demo

Real examples with actual Claude output:

---

### 1 — Regular expression
```bash
$ claude-explain "import re; re.findall(r'\d+', 'price: 42 USD, qty: 7')"
```
**Output:**
```
This code uses Python's built-in regex module to find all sequences of digits
in the string "price: 42 USD, qty: 7". The result would be ['42', '7'] —
a list of every number found in the text.
```

---

### 2 — List comprehension
```bash
$ claude-explain "[x**2 for x in range(10) if x % 2 == 0]"
```
**Output:**
```
This builds a list of squared values for every even number from 0 to 9.
The result is [0, 4, 16, 36, 64] — squares of 0, 2, 4, 6, and 8.
```

---

### 3 — The lambda (everyone's favourite mystery)
```bash
$ claude-explain "f = lambda x: x**2"
```
**Output:**
```
This creates a small anonymous function called f that takes a number x
and returns its square. For example, f(3) gives 9, and f(5) gives 25.
Think of it as a tiny math machine: put a number in, get its square out.
```

---

### 4 — Decorator
```bash
$ claude-explain "@functools.lru_cache(maxsize=128)
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)"
```
**Output:**
```
This defines a recursive Fibonacci function with caching. The @lru_cache
decorator stores up to 128 previously computed results so the function
doesn't recalculate them — turning an exponentially slow algorithm into
a fast one by remembering answers it has already worked out.
```

---

### 5 — Context manager
```bash
$ claude-explain "with open('data.csv') as f: lines = f.readlines()"
```
**Output:**
```
This opens the file "data.csv", reads all of its lines into a list called
"lines", and then automatically closes the file — even if an error occurs.
The "with" keyword handles the cleanup so you don't have to.
```

---

### 6 — فارسی / Persian
```bash
$ claude-explain "sorted(students, key=lambda s: s['grade'], reverse=True)"
```
**خروجی:**
```
این کد لیست دانش‌آموزان را بر اساس نمره‌شان از بیشترین به کمترین مرتب می‌کند.
هر دانش‌آموز یک دیکشنری است و مقدار کلید 'grade' ملاک مرتب‌سازی است.
```

---

## 🛠 Requirements

- Python 3.8 or newer
- `requests` (installed automatically)
- An Anthropic API key ([get one here](https://console.anthropic.com))

---

## 📁 Project Structure

```
claude-explain/
├── claude_explain/
│   ├── __init__.py
│   └── cli.py          # ← all the magic lives here
├── docs/
│   └── demo.gif        # ← record with asciinema or terminalizer
├── pyproject.toml
├── setup.py
├── requirements.txt
├── install.sh
├── LICENSE
├── .gitignore
└── README.md
```

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss major changes.

1. Fork the repo
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

[MIT](LICENSE) © 2024 Your Name

---

## ⭐ Show Your Support

If this tool saved you even 30 seconds, consider giving it a star on GitHub — it helps others find it!

---

<details>
<summary>🇮🇷 راهنمای فارسی</summary>

## معرفی

`claude-explain` یک ابزار خط فرمان است که با استفاده از هوش مصنوعی Claude، هر قطعه کد پایتون (یا هر زبانی) را به زبان ساده توضیح می‌دهد.

## نصب

```bash
pip install git+https://github.com/your-username/claude-explain.git
```

## تنظیم کلید API

۱. به [console.anthropic.com](https://console.anthropic.com) بروید  
۲. یک کلید API بسازید  
۳. در ترمینال اجرا کنید:

```bash
export ANTHROPIC_API_KEY="sk-ant-کلید-شما"
```

## استفاده

```bash
# آرگومان مستقیم
claude-explain "sorted(lst, key=lambda x: x[1])"

# از طریق پایپ
echo "[i for i in range(100) if i % 3 == 0]" | claude-explain

# از فایل
cat script.py | claude-explain
```

</details>
