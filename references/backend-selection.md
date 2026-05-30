# Backend selection

Ask the user to choose Python or R unless the backend is already explicit from
the request, existing files, or provided workflow.

Recommend Python when:

- The figure needs precise low-level layout control.
- The user provides Python, NumPy, pandas, matplotlib, or seaborn code.
- The figure requires custom annotations, calibration plots, or mixed chart types.
- The user needs scriptable SVG/PDF/TIFF exports from one file.

Recommend R when:

- The user provides R, tidyverse, ggplot2, or Bioconductor workflows.
- The figure is naturally expressed as layered grammar-of-graphics plots.
- The figure needs patchwork composition or ComplexHeatmap-style matrices.

After selection:

- Use only the selected backend for plotting, previews, exports, and visual QA.
- Do not use the other backend to render a fallback preview.
- If packages are missing, stop before rendering and report the exact blocker.
