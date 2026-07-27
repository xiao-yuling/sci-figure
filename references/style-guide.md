# Style guide

Use these defaults unless the target journal or provided template overrides them.

## Typography

- Use Arial as the default font for manuscript figures.
- Use Helvetica, DejaVu Sans, or another sans-serif fallback when Arial is not available.
- Keep base text around 6.5-8 pt for compact journal figures.
- Use larger text only for slide-sized or poster-sized outputs.
- Keep ordinary words outside math mode.
- Use mathtext or LaTeX only for symbols, formulas, subscripts, superscripts, Greek letters, and mathematical units.

## Axes and ticks

- Keep all four spines visible for standard scientific plots.
- Use outward ticks only on the left and bottom.
- Use light major gridlines only when they improve reading values.
- Avoid heavy frames, dense minor ticks, or decorative backgrounds.

## Panel titles

- Single standalone plots do not need panel letters.
- Multi-panel figures should use compact integrated subtitles such as `(a) Panel title`.
- Panel titles should describe the comparison or measurement, not the chart type alone.
- Keep title style consistent across panels.

## Color

- Prefer neutral base colors with one signal color and one accent color.
- Reserve red and green for directional or signed semantics.
- Check that the figure remains legible in grayscale.
- Avoid assigning unrelated saturated colors to related method families.


### Biomedical pastel option

Use this low-saturation palette for experimental comparisons when it remains
legible against the selected background:

~~~python
SCI_BIOMEDICAL_PASTEL = {
    "neutral_grey": "#D6D6D6",
    "mist_blue": "#9CB0C3",
    "sage_green": "#7C9D97",
    "soft_orange": "#EAB080",
}
~~~

For line plots, use strokes of at least 1.2 pt and reinforce pale colors with
line styles, markers, or dark outlines. Do not rely on the sage-green and
soft-orange distinction alone; verify grayscale and color-vision legibility.
## Export

- Use SVG as the primary editable vector output.
- Use PDF when the manuscript workflow requires it.
- Use TIFF or high-DPI PNG for raster submission or preview.
- Avoid delivering PNG alone for manuscript figures that may need text adjustment.
