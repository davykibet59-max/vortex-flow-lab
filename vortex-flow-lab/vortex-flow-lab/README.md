# Vortex Flow Lab (ParaView Portfolio Project)

A **ParaView-ready scientific visualization project** that explores a synthetic 2D unsteady flow field around an obstacle.  
The dataset is packaged as a time series of VTK structured-grid files with **velocity vectors** and **pressure scalars**.

## Why this is a good portfolio piece
- Shows time-varying CFD-style visualization workflow
- Demonstrates vector + scalar field handling in ParaView
- Supports streamlines, glyphs, contours, and temporal animation
- Includes reproducible data generation in Python

## Folder structure
- `data/` — VTK time-series files
- `scripts/generate_flow_data.py` — regenerates the dataset
- `statefiles/` — placeholder for your ParaView state files
- `screenshots/` — add renders before pushing to GitHub

## Suggested ParaView workflow
1. Open all `data/flow_*.vtk` files as a file series.
2. Click **Apply** and verify time controls appear.
3. Use **Calculator** to derive velocity magnitude if needed.
4. Add:
   - **Glyph** filter for local velocity direction
   - **Stream Tracer** for flow paths
   - **Contour** on pressure
   - **Warp By Vector** only if you want a stylized view
5. Create an animation across all time steps and export screenshots or video.

## Suggested screenshots for GitHub
- Streamlines colored by velocity magnitude
- Pressure contour with obstacle wake
- Side-by-side frame montage showing temporal change

## Skills demonstrated
- Scientific dataset generation
- Time-series organization
- Vector/scalar visualization design
- Reproducible workflow for ParaView

## How to regenerate
Run:

```bash
python scripts/generate_flow_data.py
```

## Next upgrade ideas
- Add cylinder geometry as a separate mesh
- Export a `.pvd` collection file
- Add a saved ParaView state file after styling
