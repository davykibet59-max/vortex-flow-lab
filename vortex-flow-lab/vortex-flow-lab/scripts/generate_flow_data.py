import os
import numpy as np

def write_legacy_structured_grid_vector(path, X, Y, Z, vectors, scalar=None, scalar_name='pressure', vector_name='velocity'):
    nx, ny, nz = X.shape
    npts = nx * ny * nz
    with open(path, 'w', encoding='utf-8') as f:
        f.write("# vtk DataFile Version 3.0\n")
        f.write("structured grid\nASCII\n")
        f.write("DATASET STRUCTURED_GRID\n")
        f.write(f"DIMENSIONS {nx} {ny} {nz}\n")
        f.write(f"POINTS {npts} float\n")
        for x, y, z in zip(np.ravel(X, order='F'), np.ravel(Y, order='F'), np.ravel(Z, order='F')):
            f.write(f"{x:.6f} {y:.6f} {z:.6f}\n")
        f.write(f"\nPOINT_DATA {npts}\n")
        if scalar is not None:
            f.write(f"SCALARS {scalar_name} float 1\n")
            f.write("LOOKUP_TABLE default\n")
            for value in np.ravel(scalar, order='F'):
                f.write(f"{float(value):.6f}\n")
        f.write(f"\nVECTORS {vector_name} float\n")
        u, v, w = vectors
        for uu, vv, ww in zip(np.ravel(u, order='F'), np.ravel(v, order='F'), np.ravel(w, order='F')):
            f.write(f"{float(uu):.6f} {float(vv):.6f} {float(ww):.6f}\n")

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(root, "data")
    os.makedirs(data_dir, exist_ok=True)

    nx, ny = 64, 40
    x = np.linspace(0, 12, nx)
    y = np.linspace(-3, 3, ny)
    X, Y = np.meshgrid(x, y, indexing="ij")
    Z = np.zeros_like(X)

    for t in range(10):
        phase = 2 * np.pi * t / 10
        obstacle = np.exp(-((X - 2.0) ** 2 + Y ** 2) / 0.18)
        vort1 = np.exp(-((X - (4.0 + 0.4 * t)) ** 2 + (Y - 0.8 * np.sin(phase + X * 0.2)) ** 2) / 0.5)
        vort2 = np.exp(-((X - (4.8 + 0.35 * t)) ** 2 + (Y + 0.8 * np.sin(phase + X * 0.2)) ** 2) / 0.5)

        u = 1.2 * (1 - 0.75 * obstacle) + 0.35 * np.sin(1.6 * Y + phase) * np.exp(-((X - 5.5) ** 2) / 8)
        v = 0.9 * (vort1 - vort2) + 0.15 * np.cos(0.7 * X - phase) * np.exp(-(Y ** 2) / 9)
        w = np.zeros_like(u)
        speed = np.sqrt(u * u + v * v)
        pressure = 1.0 - 0.4 * speed + 0.3 * obstacle

        write_legacy_structured_grid_vector(
            os.path.join(data_dir, f"flow_{t:03d}.vtk"),
            X[..., None], Y[..., None], Z[..., None],
            (u[..., None], v[..., None], w[..., None]),
            scalar=pressure[..., None]
        )

if __name__ == "__main__":
    main()
