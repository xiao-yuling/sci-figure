# sci-figure skill

Instructions for an AI agent that creates publication-ready scientific figures.
Use this skill for manuscript figures, SCI-style plots, multi-panel result
figures, and export bundles that need editable SVG/PDF text plus high-resolution
raster previews.

## Core workflow

Before plotting, establish a figure contract:

1. State the one-sentence conclusion the figure must support.
2. Map each panel or chart element to a distinct piece of evidence.
3. Choose a backend: Python or R. If the user has not specified one, ask:
   "Python or R?"
4. Define the output contract: final size, target formats, editable text needs,
   statistics, source-data traceability, and image-integrity concerns.
5. Style only after the scientific logic is clear.

After a backend is selected, use it exclusively for plotting, previews, exports,
and visual QA. Do not render a fallback preview with the other language.

## Default SCI style

- Prefer Times New Roman for manuscript figures, with Times-compatible math text.
- Keep text editable in SVG/PDF exports.
- Use full-box axes unless the target journal explicitly requires open axes.
- Keep all four spines visible, but place outward ticks only on the left and bottom.
- Use panel subtitles only for multi-panel figures.
- For multi-panel figures, use bold integrated titles such as `(a) Panel title`.
- For a single standalone plot, use a descriptive title without a panel letter, or omit the title if the caption and axis labels are sufficient.
- Use restrained palettes with strong grayscale legibility.
- Reserve red and green for thresholds, signed changes, gains, losses, or other directional semantics.

## Python quick start

```python
import matplotlib as mpl
import matplotlib.pyplot as plt

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

for ax in axes:
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(0.8)
    ax.tick_params(direction="out", top=False, right=False, length=3, width=0.7)
```

Use LaTeX or mathtext only for scientific symbols, formulas, exponents,
subscripts, Greek letters, and mathematically formatted units. Keep ordinary
words and plain numbers outside math mode.

## R quick start

```r
library(ggplot2)

theme_set(
  theme_bw(base_size = 6.5, base_family = "Times New Roman") +
    theme(
      panel.border = element_rect(linewidth = 0.45, colour = "black", fill = NA),
      axis.line = element_blank(),
      axis.ticks = element_line(linewidth = 0.35, colour = "black"),
      legend.title = element_text(size = 6.2),
      legend.text = element_text(size = 5.8),
      plot.title = element_text(size = 7, face = "bold", hjust = 0.5),
      panel.grid.major = element_line(linewidth = 0.2, colour = "grey88"),
      panel.grid.minor = element_blank()
    )
)
```

For R multi-panel work, use `patchwork` for layout and `svglite`, `cairo_pdf`,
or `ragg` for publication exports.

## References

- Read `references/backend-selection.md` when the backend is uncertain.
- Read `references/style-guide.md` before final styling or journal-ready export.
- Read `references/chart-patterns.md` for chart-family choices.
- Read `references/qa-checklist.md` before delivery.
