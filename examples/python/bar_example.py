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


groups = ["A", "B", "C", "D"]
series_1 = np.array([0.82, 1.05, 1.18, 1.34])
series_2 = np.array([0.68, 0.94, 1.02, 1.16])
err_1 = np.array([0.06, 0.08, 0.07, 0.09])
err_2 = np.array([0.05, 0.06, 0.06, 0.08])

x = np.arange(len(groups))
width = 0.34

fig, ax = plt.subplots(figsize=(3.45, 2.45))
ax.bar(x - width / 2, series_1, width, yerr=err_1, capsize=2.5, color="#0072b2", label="Series A")
ax.bar(x + width / 2, series_2, width, yerr=err_2, capsize=2.5, color="#999999", label="Series B")

ax.set_title("Grouped Bar Example", pad=5)
ax.set_xlabel("Group")
ax.set_ylabel("Response")
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.legend(loc="upper left", fontsize=6)
finish_axes(ax)

fig.tight_layout(pad=0.6)
fig.savefig(GALLERY / "bar-example.png", dpi=300, bbox_inches="tight")
plt.close(fig)
