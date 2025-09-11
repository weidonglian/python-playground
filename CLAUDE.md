# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python playground project for learning algorithms, machine learning, and various Python libraries. The project uses **uv** for package management with a lightweight-by-default approach - only 18 core packages are installed by default, with optional dependency groups for specific use cases.

## Package Management

This project uses **uv** (not pip or conda) for package management. Key commands:

```bash
# Install lightweight core dependencies (default)
uv sync --no-dev

# Install with optional dependency groups
uv sync --group data      # Data science (pandas, seaborn, etc.)
uv sync --group vision    # Computer vision (opencv, pillow)
uv sync --group ml        # Machine learning (torch, fastai)
uv sync --group web       # Web development (fastapi, gradio)
uv sync --group jupyter   # Jupyter notebooks
uv sync --group dev       # Development tools
uv sync --group all       # Everything
```

## Running Code

**Always use `uv run` for executing Python code:**

```bash
# Run examples with lightweight installation
uv run --no-dev python examples/single_cli.py
uv run --no-dev python examples/fib_spiral.py

# Run tests (lightweight works for basic tests)
uv run --no-dev pytest
uv run --no-dev pytest tests/test_sorting.py -v

# Run specific test functions
uv run --no-dev pytest tests/test_sorting.py::test_merge_sort_basic
```

## Project Structure

```
├── algorithms/           # Algorithm implementations
│   ├── sorting.py       # Sorting algorithms (merge_sort, quick_sort)
│   └── inversion.py     # Inversion counting algorithms
├── examples/            # Example scripts and demos
│   ├── single_cli.py    # Click CLI example
│   ├── fib_spiral.py    # Fibonacci spiral visualization
│   ├── ai_agent.py      # AI agent implementation
│   └── hello_pydantic.py # Pydantic model example
├── tests/               # Test files
│   ├── test_sorting.py  # Sorting algorithm tests
│   ├── test_algorithms.py # General algorithm tests
│   └── test_inversion.py # Inversion counting tests
└── pyproject.toml       # Project configuration
```

## Development Workflow

### Testing
The project uses pytest with Go-style simple tests (no classes, just functions with assert):

```bash
# Run all tests
uv run --no-dev pytest

# Run with verbose output
uv run --no-dev pytest -v

# Run specific test files
uv run --no-dev pytest tests/test_sorting.py

# Run parameterized tests
uv run --no-dev pytest tests/test_sorting.py::test_sorting_algorithms -v
```

### Code Quality
Install dev dependencies first: `uv sync --group dev`

```bash
# Format code
uv run black src/ tests/ examples/
uv run isort src/ tests/ examples/

# Check code quality
uv run flake8 src/ tests/ examples/
uv run mypy src/

# Run all checks
uv run pytest && uv run black --check src/ tests/ examples/
```

## Key Dependencies

### Core (always installed)
- **click**: CLI utilities
- **requests**: HTTP requests  
- **matplotlib**: Basic plotting
- **numpy**: Numeric computing
- **fastapi**: Web framework
- **pydantic**: Data validation
- **dotenv**: Environment variables

### Optional Groups
- **data**: pandas, seaborn, scikit-learn
- **vision**: opencv-python, pillow
- **ml**: torch, fastai, transformers
- **web**: gradio, streamlit
- **jupyter**: jupyter, ipykernel
- **dev**: pytest, black, flake8, mypy

## Python Version

- **Target**: Python 3.12+ (specified in pyproject.toml)
- **Current**: Python 3.13 (from .python-version)

## Important Notes

- The project is designed to be **lightweight by default** - use `--no-dev` for basic usage
- Always prefer `uv run` over direct Python execution
- Tests use simple function-based style with `assert` statements
- Type checking is configured with mypy (strict mode enabled)
- Code formatting follows Black standards with 88-character line length