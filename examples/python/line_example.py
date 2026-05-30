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
x = np.linspace(0, 24, 200)
y1 = 0.9 + 0.35 * np.sin(x / 2.7) + 0.08 * rng.normal(size=x.size)
y2 = 0.7 + 0.30 * np.cos((x - 2.0) / 3.0) + 0.08 * rng.normal(size=x.size)

fig, ax = plt.subplots(figsize=(3.45, 2.4))
ax.plot(x, y1, color="#0072b2", linewidth=1.2, label="Series A")
ax.plot(x, y2, color="#d55e00", linewidth=1.2, linestyle="--", label="Series B")

ax.set_title("Line Plot Example", pad=5)
ax.set_xlabel("Time")
ax.set_ylabel("Normalized Value")
ax.set_xlim(0, 24)
ax.legend(loc="upper right", fontsize=6)
finish_axes(ax)

fig.tight_layout(pad=0.6)
fig.savefig(GALLERY / "line-example.png", dpi=300, bbox_inches="tight")
plt.close(fig)
