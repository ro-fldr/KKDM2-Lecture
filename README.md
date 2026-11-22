# KDDM2 Lecture: Python Tooling for Data Science

Demo notebooks and notes for the KDDM2 lecture.

## Tools
- [uv](https://docs.astral.sh/uv/): fast Python package and environment manager (`uv sync`, `uv run`)
- Jupyter + `ipywidgets` + `plotly`: interactive plots, sliders, and maps
- [marimo](https://marimo.io): reactive Python notebooks saved as `.py` files
- `scikit-learn` + `statsmodels`: custom transformers, pipelines, time-series CV and incorporating external models like ARMA from statsmodels

## Files
- `01_interactive_jupyter.ipynb`: interactive plots, sensor cleaning, and weather station maps
- `02_sklearn_timeseries_pipeline.ipynb`: time-series preprocessing pipeline and forecasting
- `commands.md`: small cheat sheet for `uv`, some things about`marimo`, and `scikit-learn`
- `data/`: weather station metadata and sensor CSV files

## Setup
```bash
uv sync
uv run jupyter lab
# or for native view open the file in an modern editor like vscode or pycharm
```

---

If you have any questions send me a DM or hit me up on Teachcenter :)