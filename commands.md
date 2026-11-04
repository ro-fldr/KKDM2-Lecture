# Lecture Cheat Sheet: Modern Python Tooling for Data Science

Quick reference for commands and concepts used during the live demonstration.

---

## 1. Why `uv` instead of standard `pip` + `venv`?

| Feature | `pip` + `venv` | `uv` |
| :--- | :--- | :--- |
| **Speed** | Slow resolution and installation (Python-based) | **10-100x faster** (written in Rust) |
| **All-in-one** | Requires `pip`, `venv`, `pip-tools`, `pyenv` separately | Single binary manages Python versions, virtual environments, dependencies, and execution |
| **Lockfiles** | No native lockfile without third-party tools | Universal, cross-platform `uv.lock` by default |
| **Execution** | Must activate environment (`source .venv/bin/activate`) | `uv run <cmd>` automatically manages and uses the project environment |

### Core `uv` Commands

```bash
# Initialize a new Python project with pyproject.toml
uv init

# Add dependencies (installs package and records it in pyproject.toml & uv.lock)
uv add pandas scikit-learn statsmodels ipywidgets plotly

# Add development-only dependencies
uv add --dev pytest ruff

# Remove dependencies
uv remove <package-name>

# Deterministically install exact dependencies from uv.lock
uv sync

# Run scripts or tools inside the project's virtual environment
uv run python script.py
uv run jupyter lab

# Run ad-hoc tools without installing them into the current project
uvx ruff check .
```

---

## 2. Interactive Notebooks: Jupyter vs. Marimo

### Jupyter (`ipywidgets` + `plotly`)
- **Strengths**: Universal industry standard, rich ecosystem, interactive widgets via `ipywidgets`.
- **Pitfalls**:
  - Hidden state: cells can be executed out of order, leading to non-reproducible states.
  - Diffing `.ipynb` (large JSON blobs with embedded outputs) is difficult in Git.
- **Run command**:
  ```bash
  uv run jupyter lab
  ```

### Marimo
- **What is it?** A reactive notebook framework stored as pure Python files (`.py`).
- **Key differences**:
  - **Reactive execution graph (DAG)**: Modifying a variable or slider immediately and automatically updates only the cells that depend on it (like a spreadsheet).
  - **No hidden state**: Out-of-order execution is physically impossible; circular definitions are forbidden.
  - **Git-friendly**: Notebooks are saved as standard, clean Python scripts.
  - **Built-in UI**: Native sliders, tables, buttons (`mo.ui.slider(...)`) without needing separate widget extensions.
- **Run commands**:
  ```bash
  # Launch the interactive Marimo tutorial
  uv run marimo tutorial intro

  # Edit a Marimo notebook (opens browser UI)
  uv run marimo edit demo_marimo.py

  # Run as a standalone web application
  uv run marimo run demo_marimo.py
  ```

---

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
   - **Crucial**: Prevents data leakage during cross-validation by ensuring preprocessing statistics are recalculated per fold.

### Why standard K-Fold fails on Time Series:
- Random K-Fold leaks future information into past predictions (lookahead bias).
- **Solution**: Use `TimeSeriesSplit` (expanding or rolling window where train index < test index).

---

## 4. Notebook Inventory

1. [`01_interactive_jupyter.ipynb`](file:///home/uulite/projects/KKDM2_lecture/Lecture/01_interactive_jupyter.ipynb) — Widget exploration: sliders, dropdowns, interactive filtering with Plotly, interactive weather station geoplots (`px.scatter_geo` & OpenStreetMap map view with data from `data/`), and station time-series inspection.
2. [`02_sklearn_timeseries_pipeline.ipynb`](file:///home/uulite/projects/KKDM2_lecture/Lecture/02_sklearn_timeseries_pipeline.ipynb) — Custom `BaseEstimator` transformers (`SensorClipper`, `ForwardFillImputer`), custom statsmodels ARMA wrapper, `Pipeline`, and `TimeSeriesSplit` validation.
3. [`02_sklearn_timeseries_pipeline_advanced.ipynb`](file:///home/uulite/projects/KKDM2_lecture/Lecture/02_sklearn_timeseries_pipeline_advanced.ipynb) — Advanced model benchmark: comparing Baseline ARMA(2, 0, 2) against Dynamic Harmonic Regression (Fourier SARIMAX) and Tabular Lagged Gradient Boosting (`HistGradientBoostingRegressor`).
4. [`demo_marimo.py`](file:///home/uulite/projects/KKDM2_lecture/Lecture/demo_marimo.py) — Standalone reactive Marimo script demo.
