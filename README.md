# Python Playground

A modern Python playground for learning algorithms, machine learning, and various Python libraries.

## Project Structure

```
python-playground/
├── src/                    # Source code
│   └── python_playground/  # Main package
│       ├── algorithms/     # Algorithm implementations
│       └── pytorch/        # PyTorch experiments
├── notebooks/              # Jupyter notebooks
│   ├── fastai/            # FastAI tutorials
│   ├── opencv/            # Computer vision
│   └── general/           # General experiments
├── examples/               # Example scripts and demos
├── tests/                  # Test files
├── docs/                   # Documentation
├── assets/                 # Static assets (images, data)
└── pyproject.toml         # Project configuration
```

## Features

- **Algorithms**: Data structures and algorithm implementations
- **Machine Learning**: PyTorch, FastAI experiments and tutorials
- **Computer Vision**: OpenCV tutorials and projects
- **Web Development**: FastAPI examples
- **Data Science**: Pandas, NumPy, and visualization examples

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for package management with **lightweight dependencies by default**.

## Quick Start

Install dependencies and run examples:

```bash
# Install only core lightweight dependencies (recommended for basic usage)
uv sync --no-dev

# Run examples (using the lightweight environment)
uv run --no-dev python examples/fib_spiral.py
uv run --no-dev python examples/single_cli.py --help

# Or activate the environment and run directly
source .venv/bin/activate
python examples/fib_spiral.py
```

### Install Optional Dependencies by Topic

```bash
# For data science work
uv sync --group data

# For computer vision projects
uv sync --group vision

# For machine learning (includes PyTorch, FastAI)
uv sync --group ml

# For web development (FastAPI, Gradio)
uv sync --group web

# For Jupyter notebooks
uv sync --group jupyter

# For development tools
uv sync --group dev

# Install everything
uv sync --group all
```

### Examples by Dependency Group

```bash
# Lightweight examples (default installation)
uv run python examples/single_cli.py       # Uses: click
uv run python examples/fib_spiral.py       # Uses: matplotlib, numpy

# Data science examples (requires: uv sync --group data)
# Most notebooks in notebooks/general/

# Computer vision examples (requires: uv sync --group vision)
# notebooks/opencv/

# Machine learning examples (requires: uv sync --group ml)
# notebooks/fastai/

# Web examples (requires: uv sync --group web)
uv run python examples/fastapi_hello_world.py
```

### Usage

```bash
# Run lightweight examples (work with default installation)
uv run python examples/single_cli.py
uv run python examples/fib_spiral.py

# Run tests (requires dev dependencies)
uv sync --group dev && uv run pytest

# Start Jupyter Lab (requires jupyter dependencies)
uv sync --group jupyter && uv run jupyter lab

# Activate virtual environment manually
source .venv/bin/activate
```

## Development

### Code Quality

The project includes configured tools for code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **pytest**: Testing

Run quality checks:

```bash
uv run black src/ tests/ examples/
uv run isort src/ tests/ examples/
uv run flake8 src/ tests/ examples/
uv run mypy src/
uv run pytest
```
