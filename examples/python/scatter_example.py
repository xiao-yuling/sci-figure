from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
GALLERY = ROOT / "gallery"
GALLERY.mkdir(parents=True, exist_ok=True)

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "mathtext.fontset": "custom",
    "mathtext.rm": "Arial",
    "mathtext.it": "Arial:italic",
    "mathtext.bf": "Arial:bold",
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "font.size": 7,
    "axes.spines.right": True,
    "axes.spines.top": True,
    "axes.linewidth": 0.8,
    "axes.titleweight": "bold",
    "axes.titlesize": 8,
    "legend.frameon": False,
})


def finish_axes(ax):
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(0.8)
    ax.tick_params(direction="out", top=False, right=False, length=3, width=0.7)
    ax.grid(True, which="major", color="#d9d9d9", linewidth=0.35, linestyle="--")
    ax.set_axisbelow(True)


rng = np.random.default_rng(42)
x = np.linspace(0.0, 5.0, 260)
y = 0.2 + 0.9 * x + rng.normal(0, 0.45, size=x.size)
y = np.clip(y, 0, None)

slope, intercept = np.polyfit(x, y, 1)
y_fit = slope * x + intercept
ss_res = np.sum((y - y_fit) ** 2)
ss_tot = np.sum((y - y.mean()) ** 2)
r2 = 1 - ss_res / ss_tot

fig, ax = plt.subplots(figsize=(3.35, 2.55))
ax.scatter(x, y, s=14, color="#6e6e6e", edgecolor="white", linewidth=0.25, alpha=0.8)
ax.plot([0, 5.2], [0, 5.2], color="black", linestyle="--", linewidth=0.8, label="1:1 line")
ax.plot(x, y_fit, color="#0072b2", linewidth=1.0, label="Linear fit")
ax.text(
    0.18,
    4.85,
    f"$R^2$ = {r2:.3f}",
    ha="left",
    va="top",
    bbox={"facecolor": "white", "edgecolor": "black", "linewidth": 0.45, "pad": 2},
)

ax.set_title("Scatter Plot Example", pad=5)
ax.set_xlabel("Measured Value")
ax.set_ylabel("Predicted Value")
ax.set_xlim(0, 5.2)
ax.set_ylim(0, 5.2)
ax.legend(loc="lower right", fontsize=6)
finish_axes(ax)

fig.tight_layout(pad=0.6)
fig.savefig(GALLERY / "scatter-example.png", dpi=300, bbox_inches="tight")
plt.close(fig)
