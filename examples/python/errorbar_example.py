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
    ax.grid(True, axis="x", color="#d9d9d9", linewidth=0.35, linestyle="--")
    ax.set_axisbelow(True)


labels = ["A", "B", "C", "D", "E"]
effect = np.array([0.18, 0.34, -0.08, 0.52, 0.27])
lower = np.array([0.10, 0.14, 0.12, 0.16, 0.11])
upper = np.array([0.12, 0.13, 0.15, 0.18, 0.14])
y = np.arange(len(labels))

fig, ax = plt.subplots(figsize=(3.45, 2.35))
ax.axvline(0, color="#4d4d4d", linewidth=0.8, linestyle="--")
ax.errorbar(
    effect,
    y,
    xerr=[lower, upper],
    fmt="o",
    color="#0072b2",
    ecolor="#4d4d4d",
    elinewidth=0.8,
    capsize=2.5,
    markersize=4,
)

ax.set_title("Interval Plot Example", pad=5)
ax.set_xlabel("Effect Estimate")
ax.set_ylabel("Group")
ax.set_yticks(y)
ax.set_yticklabels(labels)
finish_axes(ax)

fig.tight_layout(pad=0.6)
fig.savefig(GALLERY / "interval-example.png", dpi=300, bbox_inches="tight")
plt.close(fig)
