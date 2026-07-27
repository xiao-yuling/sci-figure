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
    ax.grid(True, axis="y", color="#d9d9d9", linewidth=0.35, linestyle="--")
    ax.set_axisbelow(True)


rng = np.random.default_rng(42)
data = [
    rng.normal(1.0, 0.18, 80),
    rng.normal(1.25, 0.22, 80),
    rng.normal(1.48, 0.20, 80),
    rng.normal(1.35, 0.26, 80),
]

fig, ax = plt.subplots(figsize=(3.45, 2.45))
parts = ax.violinplot(data, showmeans=False, showmedians=False, showextrema=False)
for body in parts["bodies"]:
    body.set_facecolor("#b7c9e2")
    body.set_edgecolor("#4d4d4d")
    body.set_linewidth(0.45)
    body.set_alpha(0.9)

ax.boxplot(
    data,
    widths=0.18,
    patch_artist=True,
    showfliers=False,
    boxprops={"facecolor": "white", "edgecolor": "black", "linewidth": 0.7},
    medianprops={"color": "#d55e00", "linewidth": 1.0},
    whiskerprops={"color": "black", "linewidth": 0.7},
    capprops={"color": "black", "linewidth": 0.7},
)

ax.set_title("Violin and Box Example", pad=5)
ax.set_xlabel("Group")
ax.set_ylabel("Value")
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(["A", "B", "C", "D"])
finish_axes(ax)

fig.tight_layout(pad=0.6)
fig.savefig(GALLERY / "violin-box-example.png", dpi=300, bbox_inches="tight")
plt.close(fig)
