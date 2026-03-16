# GitHub Actions Practice PoC

A proof-of-concept repository demonstrating a complete **GitHub Actions CI pipeline** that automatically runs on every Pull Request.

## What this PoC demonstrates

When a PR is opened (or updated), the workflow automatically:

| Step | Tool | What it does |
|------|------|-------------|
| ✅ **Lint** | `flake8` | Checks code style and catches common errors |
| 🔨 **Build** | `pip install` | Installs dependencies and verifies the package imports correctly |
| 🧪 **Test** | `pytest` + `pytest-cov` | Runs the full test suite and measures code coverage |
| 💬 **Report** | `actions/github-script` | Posts a summary comment directly on the PR |

## Project structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions workflow
├── src/
│   └── calculator.py       # Sample Python library (arithmetic operations)
├── tests/
│   └── test_calculator.py  # pytest test suite
├── requirements.txt        # Python dependencies
└── README.md
```

## Running locally

```bash
# Install dependencies
pip install -r requirements.txt

# Lint
flake8 src/ tests/ --max-line-length=100

# Test with coverage
pytest tests/ --cov=src --cov-report=term-missing -v
```

## CI workflow overview

The workflow (`.github/workflows/ci.yml`) is triggered on every `pull_request` and defines four sequential jobs:

1. **lint** – runs `flake8` to enforce code style  
2. **build** – installs dependencies and verifies the package loads correctly (depends on *lint*)  
3. **test** – runs `pytest` with coverage reporting (depends on *build*)  
4. **report** – posts a Markdown summary comment on the PR with the pass/fail status of each step (always runs, even on failure)

### Sample PR comment

```
## 🤖 CI Pipeline Summary

**Overall:** ✅ All checks passed!

| Step  | Status |
|-------|--------|
| ✅ Lint (flake8)   | `success` |
| ✅ Build (install) | `success` |
| ✅ Test (pytest)   | `success` |

> Workflow run: #42
```
