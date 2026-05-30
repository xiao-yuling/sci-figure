from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
GALLERY = ROOT / "gallery"
GALLERY.mkdir(parents=True, exist_ok=True)

mpl.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "DejaVu Serif", "serif"],
    "mathtext.fontset": "custom",
    "mathtext.rm": "Times New Roman",
    "mathtext.it": "Times New Roman:italic",
    "mathtext.bf": "Times New Roman:bold",
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
values = rng.normal(loc=0.0, scale=0.85, size=900)
values = np.clip(values, -2.6, 2.6)

fig, ax = plt.subplots(figsize=(3.35, 2.35))
ax.hist(values, bins=32, color="#7f7f7f", edgecolor="black", linewidth=0.35, alpha=0.9)
ax.axvline(0, color="#d62728", linestyle="--", linewidth=0.9, label="Reference")
ax.axvline(values.mean(), color="#0072b2", linewidth=0.9, label="Mean")

ax.set_title("Histogram Example", pad=5)
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
ax.legend(loc="upper right", fontsize=6)
finish_axes(ax)

fig.tight_layout(pad=0.6)
fig.savefig(GALLERY / "histogram-example.png", dpi=300, bbox_inches="tight")
plt.close(fig)
