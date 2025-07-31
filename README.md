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

This project uses [uv](https://github.com/astral-sh/uv) for package management.

### Installation

```bash
# Install dependencies and create virtual environment
uv sync

# Install with development dependencies
uv sync --group dev

# Install with Jupyter support
uv sync --group jupyter
```

### Usage

```bash
# Run a script
uv run python examples/fastapi_hello_world.py

# Run tests
uv run pytest

# Start Jupyter Lab
uv run jupyter lab

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
