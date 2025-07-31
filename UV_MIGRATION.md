# Migration to UV

This project has been migrated from conda/pip to use `uv` for package management.

## Installation

First, install uv if you haven't already:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or on macOS with Homebrew:

```bash
brew install uv
```

## Setup

1. Install dependencies and create virtual environment:

```bash
uv sync
```

2. Activate the virtual environment:

```bash
source .venv/bin/activate
```

Or use uv to run commands directly:

```bash
uv run python your_script.py
```

## Development

Install development dependencies:

```bash
uv sync --group dev
```

Run Jupyter notebooks:

```bash
uv sync --group jupyter
uv run jupyter lab
```

## Adding New Dependencies

Add a new dependency:

```bash
uv add package_name
```

Add a development dependency:

```bash
uv add --group dev package_name
```

## Migration Notes

- Replaced `environment.yml` and `requirements.txt` with `pyproject.toml`
- PyTorch dependencies now use the CUDA 11.8 index
- Added optional development and Jupyter dependency groups
- Python version pinned to 3.11 (can be changed in `.python-version`)

## Old Files

The following files are no longer needed and can be removed:

- `environment.yml`
- `requirements.txt`
