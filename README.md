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

- **🐍 Modern Python**: Uses Python 3.12+ with modern generic syntax
- **⚡ Lightweight by default**: Only 18 core packages installed by default
- **📦 Modular dependencies**: Install only what you need via optional groups
- **� Modern Testing**: Uses pytest with Go-style simple tests and advanced features
- **�🧮 Algorithms**: Data structures and algorithm implementations
- **🤖 Machine Learning**: PyTorch, FastAI experiments and tutorials
- **👁️ Computer Vision**: OpenCV tutorials and projects
- **🌐 Web Development**: FastAPI examples
- **📊 Data Science**: Pandas, NumPy, and visualization examples

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

# Test the algorithms
uv run --no-dev pytest tests/test_sorting.py -v

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
uv run --no-dev python examples/single_cli.py       # Uses: click
uv run --no-dev python examples/fib_spiral.py       # Uses: matplotlib, numpy

# Algorithm examples (test the implementations)
uv run --no-dev pytest tests/test_sorting.py -v    # Test sorting algorithms
uv run --no-dev python -c "from src.python_playground.algorithms.sorting import merge_sort; arr=[3,1,4,1,5]; merge_sort(arr); print(arr)"

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
uv run --no-dev python examples/single_cli.py
uv run --no-dev python examples/fib_spiral.py

# Run tests (lightweight - no dev dependencies needed for basic tests)
uv run --no-dev pytest

# Run tests with development tools (requires dev dependencies)
uv sync --group dev && uv run pytest -v

# Start Jupyter Lab (requires jupyter dependencies)
uv sync --group jupyter && uv run jupyter lab

# Activate virtual environment manually
source .venv/bin/activate
```

## Development

### Testing

The project uses **pytest** with Go-style simple tests and modern Python features:

```bash
# Run all tests (works with lightweight installation)
uv run --no-dev pytest

# Run tests with verbose output
uv run --no-dev pytest -v

# Run specific test file
uv run --no-dev pytest tests/test_sorting.py

# Run tests matching a pattern
uv run --no-dev pytest -k "basic"

# Run specific test function
uv run --no-dev pytest tests/test_sorting.py::test_merge_sort_basic

# Run parameterized tests (shows multiple test cases)
uv run --no-dev pytest tests/test_sorting.py::test_sorting_algorithms -v
```

**Test Structure:**

- **Simple Go-style tests**: No classes, just functions with `assert`
- **Parameterized tests**: Test multiple scenarios with `@pytest.mark.parametrize`
- **Fixtures**: Reusable test data and setup
- **Property-based testing**: Random data validation

### Code Quality

The project includes configured tools for code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking
- **pytest**: Testing

Run quality checks:

```bash
# Install dev dependencies first
uv sync --group dev

# Format code
uv run black src/ tests/ examples/
uv run isort src/ tests/ examples/

# Check code quality
uv run flake8 src/ tests/ examples/
uv run mypy src/

# Run all tests with coverage
uv run pytest --cov=src/python_playground

# Run tests and quality checks together
uv run pytest && uv run black --check src/ tests/ examples/
```

### Example Test Output

```bash
$ uv run --no-dev pytest tests/test_sorting.py -v

tests/test_sorting.py::test_merge_sort_basic PASSED
tests/test_sorting.py::test_merge_sort_empty PASSED
tests/test_sorting.py::test_quick_sort_basic PASSED
tests/test_sorting.py::test_partition PASSED
tests/test_sorting.py::test_sorting_algorithms[merge_sort] PASSED
tests/test_sorting.py::test_sorting_algorithms[quick_sort] PASSED
tests/test_sorting.py::test_quick_sort_pivot_types[QsPivot.First] PASSED
tests/test_sorting.py::test_quick_sort_pivot_types[QsPivot.Last] PASSED
tests/test_sorting.py::test_quick_sort_pivot_types[QsPivot.Random] PASSED

========================== 23 passed in 0.04s ==========================
```
