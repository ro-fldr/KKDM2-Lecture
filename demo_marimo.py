import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    return go, mo, np


@app.cell
def __(mo):
    mo.md(
        """
        # Reactive Data Exploration with Marimo
        Unlike Jupyter's imperative top-to-bottom cells, Marimo builds a **Directed Acyclic Graph (DAG)**.
        When you adjust the sliders below, **only the dependent cells re-execute instantly**!
        """
    )
    return


@app.cell
def __(mo):
    freq_slider = mo.ui.slider(start=0.5, stop=5.0, step=0.1, value=1.5, label="Signal Frequency (Hz)")
    noise_slider = mo.ui.slider(start=0.0, stop=1.0, step=0.05, value=0.3, label="Noise Level (σ)")
    cutoff_slider = mo.ui.slider(start=1.0, stop=3.0, step=0.1, value=2.0, label="Clip Anomaly Threshold")
    mo.vstack([freq_slider, noise_slider, cutoff_slider])
    return cutoff_slider, freq_slider, noise_slider


@app.cell
def __(cutoff_slider, freq_slider, go, mo, np, noise_slider):
    # Reactive computation: automatically updates whenever sliders change
    t = np.linspace(0, 10, 400)
    clean_signal = np.sin(2 * np.pi * freq_slider.value * t)
    noise = np.random.normal(0, noise_slider.value, size=len(t))
    raw_signal = clean_signal + noise

    # Inject a couple of sensor spikes/anomalies
    raw_signal[80] = 4.5
    raw_signal[220] = -4.0

    clipped_signal = np.clip(raw_signal, -cutoff_slider.value, cutoff_slider.value)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=raw_signal, mode="lines", name="Raw Signal (with Spikes)", opacity=0.5, line=dict(color="gray")))
    fig.add_trace(go.Scatter(x=t, y=clipped_signal, mode="lines", name="Threshold Clipped", line=dict(color="crimson", width=2)))
    fig.add_trace(go.Scatter(x=t, y=clean_signal, mode="lines", name="True Ground Truth", line=dict(color="royalblue", dash="dash")))

    fig.update_layout(
        title=f"Reactive Signal Processing (Freq: {freq_slider.value} Hz, Noise: {noise_slider.value}, Cutoff: ±{cutoff_slider.value})",
        xaxis_title="Time (s)",
        yaxis_title="Amplitude",
        template="plotly_white",
        height=450,
    )

    mo.ui.plotly(fig)
    return clean_signal, clipped_signal, fig, noise, raw_signal, t


if __name__ == "__main__":
    app.run()
