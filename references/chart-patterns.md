# Chart patterns

Choose chart types by the scientific question first.

| Question | Good patterns |
|---|---|
| How well do two quantities agree? | Scatter, calibration plot, Bland-Altman-style residual plot |
| How does a metric change over time? | Line plot, uncertainty ribbon, event-marked trend |
| Which group is larger or smaller? | Bar chart, dot plot, interval plot |
| How is a quantity distributed? | Histogram, density, box plot, violin plot |
| How do many variables vary together? | Heatmap, clustered matrix, correlation matrix |
| How do effect estimates compare? | Forest plot, interval plot |
| How do multiple panels support one claim? | Multi-panel grid with unique evidence per panel |

## Multi-panel rule

Each panel should answer a distinct question. If covering one panel does not
remove evidence from the figure, merge it, replace it, or remove it.

## Common traps

- Repeating the same data with different chart types.
- Using saturated colors only to make panels look different.
- Labeling panels with floating letters when integrated panel titles are clearer.
- Exporting only a raster preview when editable text is needed.
