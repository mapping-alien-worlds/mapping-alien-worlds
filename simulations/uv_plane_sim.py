"""
Mapping Alien Worlds — uv-plane interferometric simulation
===========================================================
Simulates a 10-satellite circular optical interferometer (100 km baseline)
observing an Earth-like exoplanet surface at ~1.3 pc, with 24-epoch
super-synthesis, and compares dirty imaging vs. Wiener reconstruction.

Requirements: numpy, scipy, matplotlib
Usage:        python uv_plane_sim.py
License:      MIT
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

LAMBDA = 550e-9
D_PC = 1.3
D_M = D_PC * 3.086e16
N_SAT = 10
BASELINE = 100e3
N_EPOCHS = 24
N = 256
SEED = 42


def figure1_baseline_resolution():
    baselines = np.logspace(0, 4, 200) * 1e3
    res_km = 1.22 * LAMBDA / baselines * D_M / 1e3
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(baselines / 1e3, res_km, lw=2, color="navy")
    for B_km in (10, 100, 1000):
        r = 1.22 * LAMBDA / (B_km * 1e3) * D_M / 1e3
        ax.scatter([B_km], [r], zorder=5, color="crimson")
        ax.annotate(f"{B_km} km: {r:.0f} km", (B_km, r),
                    textcoords="offset points", xytext=(10, 8))
    ax.axhline(12742, ls="--", color="gray")
    ax.text(1.2, 14000, "Earth diameter (12,742 km)", color="gray")
    ax.set_xlabel("Baseline (km)")
    ax.set_ylabel(f"Surface resolution @ {D_PC} pc (km)")
    ax.set_title("Baseline vs. Resolution (lambda=550 nm)")
    ax.grid(alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig("fig1_baseline_resolution.png", dpi=150)
    print("Saved fig1_baseline_resolution.png")


def make_planet_surface(rng):
    y, x = np.mgrid[-1:1:N * 1j, -1:1:N * 1j]
    disk = np.hypot(x, y) < 0.8
    surf = np.zeros((N, N))
    surf[disk] = 0.3
    for _ in range(6):
        cx, cy = rng.uniform(-0.5, 0.5, 2)
        s = rng.uniform(0.1, 0.3)
        surf[((x - cx) ** 2 + (y - cy) ** 2 < s ** 2) & disk] = 0.8
    surf[(np.abs(y) > 0.65) & disk] = 0.95
    clouds = gaussian_filter(rng.random((N, N)), 8)
    surf = np.clip(surf + (clouds > 0.55) * 0.4 * disk, 0, 1) * disk
    return surf


def uv_coverage():
    ang = np.linspace(0, 2 * np.pi, N_SAT, endpoint=False)
    mask = np.zeros((N, N))
    scale = N / 2.2 / BASELINE
    for ep in range(N_EPOCHS):
        rot = ep * np.pi / N_EPOCHS
        px = BASELINE / 2 * np.cos(ang + rot)
        py = BASELINE / 2 * np.sin(ang + rot)
        for i in range(N_SAT):
            for j in range(i + 1, N_SAT):
                for s in (1, -1):
                    u = int(round(s * (px[i] - px[j]) * scale)) + N // 2
                    v = int(round(s * (py[i] - py[j]) * scale)) + N // 2
                    if 0 <= u < N and 0 <= v < N:
                        mask[v, u] = 1
    return mask


def figure2_uv_simulation():
    rng = np.random.default_rng(1)
    surf = make_planet_surface(rng)
    mask = uv_coverage()
    F = np.fft.fftshift(np.fft.fft2(surf))
    Fs = F * mask
    dirty = np.abs(np.fft.ifft2(np.fft.ifftshift(Fs)))
    recon = np.abs(np.fft.ifft2(np.fft.ifftshift(Fs * mask / (mask ** 2 + 0.05))))
    recon = gaussian_filter(recon, 1.5)
    fill = mask.sum() / mask.size * 100
    titles = ["Ground truth surface", f"uv coverage ({fill:.1f}%)",
              "Dirty image", "Wiener reconstruction"]
    fig, axes = plt.subplots(1, 4, figsize=(16, 4.2))
    for ax, im, t in zip(axes, [surf, mask, dirty, recon], titles):
        ax.imshow(im, cmap="gray" if "uv" in t else "viridis")
        ax.set_title(t)
        ax.axis("off")
    fig.suptitle(f"{N_SAT} satellites, {BASELINE/1e3:.0f} km baseline, "
                 f"{N_EPOCHS}-epoch super-synthesis", y=1.02)
    fig.tight_layout()
    fig.savefig("fig2_uv_simulation.png", dpi=150, bbox_inches="tight")
    print(f"Saved fig2_uv_simulation.png (uv fill: {fill:.2f}%)")


if __name__ == "__main__":
    np.random.seed(SEED)
    figure1_baseline_resolution()
    figure2_uv_simulation()
