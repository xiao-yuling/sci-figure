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


rng = np.random.default_rng(42)
data = rng.normal(0, 0.65, size=(7, 8))
data += np.linspace(-0.8, 0.8, 8)
data[2:5, 4:7] += 0.8

fig, ax = plt.subplots(figsize=(3.5, 2.65))
im = ax.imshow(data, cmap="RdBu_r", vmin=-2.0, vmax=2.0, aspect="auto")

ax.set_title("Heatmap Example", pad=5)
ax.set_xlabel("Condition")
ax.set_ylabel("Feature")
ax.set_xticks(np.arange(data.shape[1]))
ax.set_yticks(np.arange(data.shape[0]))
ax.set_xticklabels([f"C{i + 1}" for i in range(data.shape[1])])
ax.set_yticklabels([f"F{i + 1}" for i in range(data.shape[0])])
ax.tick_params(direction="out", top=False, right=False, length=3, width=0.7)

for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(0.8)

cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label("Standardized value")
cbar.ax.tick_params(direction="out", length=2.5, width=0.6)

fig.tight_layout(pad=0.6)
fig.savefig(GALLERY / "heatmap-example.png", dpi=300, bbox_inches="tight")
plt.close(fig)
