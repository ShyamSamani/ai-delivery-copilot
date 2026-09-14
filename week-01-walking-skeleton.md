# Week 1 — Walking Skeleton

**Goal:** by the end of this week you have a live URL, a GitHub repo, and tests that run automatically on every push. The app will barely do anything. That's the point — you're building the pipeline while it's still simple.

Four sessions, roughly 90 minutes each.

---

## Session 1 — Install and run something

### Install

1. **Python** — download 3.12 from [python.org/downloads](https://www.python.org/downloads/). On the first screen, tick **"Add python.exe to PATH"** before clicking Install. Don't use the Microsoft Store version; it puts files in odd places and causes confusing errors later.
2. **Git** — [git-scm.com/download/win](https://git-scm.com/download/win). Accept all the defaults.
3. **VS Code extensions** — open VS Code, click the Extensions icon in the left bar, install **Python** (by Microsoft).

Check both worked. Open PowerShell (Windows key, type "powershell"):

```powershell
py --version
git --version
```

Both should print a version number. If `py` isn't recognised, the PATH tickbox was missed — reinstall Python.

### Create the project

```powershell
cd ~\Documents
mkdir ai-delivery-copilot
cd ai-delivery-copilot
code .
```

That last command opens the folder in VS Code. From now on use VS Code's built-in terminal (**Ctrl + `**).

### Virtual environment

A virtual environment is a private copy of Python for this project, so the packages you install here can't break anything else on your machine.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**If you get a red error about "running scripts is disabled on this system"** — this is the single most common Windows blocker. Run this once, answer `Y`, then try activating again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

When it works, your prompt gets a `(.venv)` prefix. You need that prefix every time you work on the project. If you close and reopen VS Code, run the activate line again.

### First app

Create a file called `requirements.txt`:

```
streamlit
```

Install it:

```powershell
pip install -r requirements.txt
```

Create `app.py`:

```python
import streamlit as st

st.set_page_config(page_title="Project Phoenix Copilot")

st.title("Project Phoenix Delivery Copilot")
st.write("Ask a question about the project.")

question = st.text_input("Your question")

if question:
    st.info("No answer engine yet — that arrives in week 3.")
```

Run it:

```powershell
streamlit run app.py
```

A browser tab opens with your app. Type something in the box and watch it respond. Stop the server with **Ctrl + C** in the terminal.

**Done for session 1.** You have a running web app.

---

## Session 2 — Git and GitHub

### Tell Git who you are

Once, ever:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use the same email as your GitHub account.

### Ignore the junk

Create `.gitignore`:

```
.venv/
__pycache__/
*.pyc
.env
.streamlit/secrets.toml
```

`.venv` is hundreds of megabytes of installed packages — never commit it. Anyone cloning your repo rebuilds it from `requirements.txt`. That's what the file is for.

### First commit

```powershell
git init
git add .
git commit -m "Walking skeleton: Streamlit app shell"
```

Run `git status` and `git log` to see what happened. Get in the habit of running `git status` constantly — it tells you exactly where you are.

### Push to GitHub

1. Go to [github.com/new](https://github.com/new)
2. Name it `ai-delivery-copilot`, set it **Public**, and **don't** tick any of the "initialise with" boxes — you already have files
3. Create it, then copy the commands GitHub shows you under "push an existing repository". They'll look like:

```powershell
git remote add origin https://github.com/YOURNAME/ai-delivery-copilot.git
git branch -M main
git push -u origin main
```

Refresh the GitHub page. Your code is there.

### Then use the GUI

Now that you've done it by hand, use VS Code's Source Control panel (the branch icon in the left bar) for day-to-day commits. Typing commands once teaches you what's happening; clicking buttons afterwards is faster. Both are fine.

**Done for session 2.**

---

## Session 3 — Tests and CI

This is the session that makes you different from someone following a tutorial.

### Some code worth testing

Create the folder structure. In VS Code, right-click in the file explorer to add folders and files:

```
src/copilot/answering.py
tests/test_answering.py
```

`src/copilot/answering.py`:

```python
def answer(question: str) -> str:
    """Placeholder answer engine. Real retrieval arrives in week 3."""
    cleaned = question.strip()
    if not cleaned:
        return "Please ask a question."
    return f"I don't know yet, but you asked: {cleaned}"
```

`tests/test_answering.py`:

```python
from copilot.answering import answer


def test_blank_question_asks_again():
    assert answer("   ") == "Please ask a question."


def test_question_is_echoed_back():
    assert "testing" in answer("Why is testing amber?")
```

A test is just a function starting with `test_` that asserts something is true. If the assertion fails, the test fails. That's the whole idea.

### Wire it up

Create `pyproject.toml` so pytest can find your `src` folder:

```toml
[tool.pytest.ini_options]
pythonpath = ["src"]
```

Create `requirements-dev.txt`:

```
pytest
ruff
```

Install and run:

```powershell
pip install -r requirements-dev.txt
pytest
ruff check .
```

You should see two passing tests, and ruff (a linter — it catches style problems and obvious bugs) reporting no issues.

Now break something deliberately. Change `"Please ask a question."` to `"Ask something."` in `answering.py`, run `pytest` again, and read the failure output. Then change it back. Knowing what a failure looks like is worth more than seeing a pass.

### Use it in the app

Update `app.py` to use the function:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

import streamlit as st

from copilot.answering import answer

st.set_page_config(page_title="Project Phoenix Copilot")

st.title("Project Phoenix Delivery Copilot")
st.write("Ask a question about the project.")

question = st.text_input("Your question")

if question:
    st.write(answer(question))
```

### GitHub Actions

Create `.github/workflows/ci.yml` (the folder name starts with a dot):

```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-dev.txt

      - name: Lint
        run: ruff check .

      - name: Test
        run: pytest
```

Read it top to bottom — it's genuinely this simple. On every push, GitHub rents a Linux machine, checks out your code, installs Python, installs your dependencies, lints, and runs your tests.

Commit and push:

```powershell
git add .
git commit -m "Add answering module, tests and CI"
git push
```

Go to your repo on GitHub and click the **Actions** tab. Watch it run. Green tick means passing.

**Now break it on purpose.** Change a test so it fails, push, and watch GitHub go red and email you. Fix it and push again. That loop — red, fix, green — is what CI is.

**Done for session 3.**

---

## Session 4 — Deploy

### Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
2. Authorise it to see your repositories
3. **Create app** → pick your repo, branch `main`, main file `app.py`
4. Deploy

A few minutes later you have a public URL. Send it to someone.

### Confirm continuous deployment

Change the title in `app.py` to something else. Commit, push, wait a minute, refresh the live URL. It updated itself.

You now have CI and CD. Every push runs your tests and updates your live app.

### Optional refinement

Right now those two things are independent — Streamlit redeploys whether or not your tests pass. To gate deployment properly, work on `main`, and add a `release` branch that Streamlit watches. Merge `main` into `release` only when CI is green. That's a simplified version of how real teams do it, and it's worth setting up once you're comfortable with branching. Don't do it this week.

---

## What you'll have

```
ai-delivery-copilot/
├── .github/workflows/ci.yml
├── src/copilot/answering.py
├── tests/test_answering.py
├── app.py
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
└── .gitignore
```

Plus a live URL and a green CI badge.

You've touched Python packaging, virtual environments, Git, GitHub, linting, unit testing, GitHub Actions and cloud deployment. Not one line of AI code yet — and that's fine, because the hard infrastructure is now behind you.

---

## Week 2 preview

Build the Project Phoenix dataset — the twelve files from your original plan — and write tests that load and validate it. Your CI starts checking that every risk in `risks.csv` has an owner and that every action has a due date. That's where testing starts feeling useful rather than ceremonial.

## Week 3 preview

The actual RAG: chunk the documents, embed them, store the vectors, retrieve, and answer. The `answer()` function you wrote in session 3 gets a real implementation, and everything around it already works.
