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


def finish_axes(ax, grid_axis="both"):
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(0.8)
    ax.tick_params(direction="out", top=False, right=False, length=3, width=0.7)
    ax.grid(True, axis=grid_axis, color="#d9d9d9", linewidth=0.35, linestyle="--")
    ax.set_axisbelow(True)


rng = np.random.default_rng(42)
x = np.linspace(0, 10, 120)
y = 0.45 + 0.08 * x + 0.25 * np.sin(x) + rng.normal(0, 0.08, size=x.size)
groups = ["A", "B", "C"]
bars = [0.72, 0.95, 1.12]
heat = rng.normal(0, 0.7, size=(5, 6))

fig, axes = plt.subplots(2, 2, figsize=(5.2, 3.8))
ax1, ax2, ax3, ax4 = axes.ravel()

ax1.plot(x, y, color="#0072b2", linewidth=1.1)
ax1.set_title("(a) Trend", pad=4)
ax1.set_xlabel("Time")
ax1.set_ylabel("Value")
finish_axes(ax1)

ax2.bar(groups, bars, color=["#999999", "#0072b2", "#d55e00"], edgecolor="black", linewidth=0.4)
ax2.set_title("(b) Group Summary", pad=4)
ax2.set_xlabel("Group")
ax2.set_ylabel("Response")
finish_axes(ax2, grid_axis="y")

im = ax3.imshow(heat, cmap="RdBu_r", vmin=-2, vmax=2, aspect="auto")
ax3.set_title("(c) Matrix Pattern", pad=4)
ax3.set_xlabel("Condition")
ax3.set_ylabel("Feature")
ax3.tick_params(direction="out", top=False, right=False, length=3, width=0.7)
for spine in ax3.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(0.8)
fig.colorbar(im, ax=ax3, fraction=0.046, pad=0.04)

scatter_x = rng.normal(0.0, 1.0, 120)
scatter_y = 0.35 * scatter_x + rng.normal(0.0, 0.65, 120)
ax4.scatter(scatter_x, scatter_y, s=13, color="#6e6e6e", edgecolor="white", linewidth=0.2)
ax4.set_title("(d) Relationship", pad=4)
ax4.set_xlabel("Variable 1")
ax4.set_ylabel("Variable 2")
finish_axes(ax4)

fig.tight_layout(pad=0.8)
fig.savefig(GALLERY / "multipanel-example.png", dpi=300, bbox_inches="tight")
plt.close(fig)
