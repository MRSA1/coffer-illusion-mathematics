import numpy as np

def generate_synthetic_image(A_C, radius, wavelength, size=128, A_R=1.0):
    N = size
    y, x = np.mgrid[0:N, 0:N]
    cx, cy = N // 2, N // 2
    R = np.ones((N, N))
    R[:, :cx] = -1.0
    R[:, cx:] = 1.0
    freq = 1.0 / wavelength
    C = np.sin(2*np.pi * freq * np.sqrt((x - (cx + 6))**2 + (y - cy)**2))
    I = A_R * R + A_C * C
    return I, R, C

def run_monte_carlo(n_trials=200, A_R=1.0, size=128, seed=42):
    np.random.seed(seed)
    results = []
    for _ in range(n_trials):
        A_C = np.random.uniform(0, 1.6)
        radius = np.random.uniform(8, 40)
        wavelength = np.random.uniform(6, 12)
        local_pref = np.random.choice([True, False])
        global_det = np.random.choice([True, False])
        results.append((A_C, radius, wavelength, local_pref, global_det))
    return results
