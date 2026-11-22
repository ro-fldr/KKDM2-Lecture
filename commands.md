# Lecture Cheat Sheet: Modern Python Tooling for Data Science

Quick reference for commands and concepts used during the live demonstration.

---

## 1. Why `uv` instead of standard `pip` + `venv`?

| Feature | `pip` + `venv` | `uv` |
| :--- | :--- | :--- |
| **Speed** | Slow resolution and installation (Python-based) | **10-100x faster** |
| **All-in-one** | Requires `pip`, `venv`, `pip-tools`, `pyenv` separately | Single program manages Python versions, virtual environments, dependencies, and execution |
| **Running `.py` scripts** | Must activate environment (`source .venv/bin/activate`) | `uv run <cmd>` automatically manages and finds the project environment magically |

### Core `uv` Commands

```bash
# Initialize a new Python project with basic file structure, pyproject.toml & git repo
uv init

# Add dependencies (installs package and records it in pyproject.toml & uv.lock)
uv add pandas scikit-learn statsmodels ipywidgets plotly

# Add development-only packages
uv add --dev pytest ruff

# Remove packages
uv remove <package-name>

# Deterministically install exact dependencies from uv.lock
# Also very handy when installing all dependencies from a external repo.
uv sync

# Run scripts or tools inside the project's virtual environment
uv run python script.py
uv run jupyter lab

# Run one off tools without installing them into the current project
uvx ruff check .
```

## 2. Reactive Notebooks with `marimo`

[marimo](https://marimo.io) is a reactive Python notebook that stores notebooks as pure `.py` files instead of JSON (very nice for git diffs!). 

When you update a cell or interact with a UI element, marimo automatically re-runs only the dependent cells (eliminating hidden state and out-of-order execution bugs).
- **Website:** [marimo.io](https://marimo.io)
- **Examples & Inspiration:** [marimo Gallery](https://marimo.io/gallery)


## 3. Scikit-Learn Paradigm & Time-Series Pipelines

### The Core API Contracts
1. **Transformer** (`fit(X, y)` & `transform(X)`):
   - `fit`: Learns internal state / statistics (e.g., mean, sensor threshold) strictly from training data.
   - `transform`: Applies the transformation to any data matrix (train or test).
   - Inherit from `BaseEstimator` and `TransformerMixin`.
2. **Estimator / Predictor** (`fit(X, y)` & `predict(X)`):
   - `fit`: Fits parameters of the model.
   - `predict`: Produces targets or forecasts for new observations.
   - Inherit from `BaseEstimator` and `RegressorMixin` (or `ClassifierMixin`).
3. **Pipeline** (`Pipeline([('step1', t1), ('step2', t2), ('model', est)])`):
   - Encapsulates preprocessing and modeling into a single object.
   - 🚨 Prevents data leakage during cross-validation by ensuring preprocessing statistics are recalculated per fold.
---
