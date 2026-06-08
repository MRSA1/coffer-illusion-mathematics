import numpy as np
from math import erf, pi, sqrt

def alpha_R_closed(sigma_x, sigma_y, k):
    return 2.0 * sqrt(2*pi) * sqrt(sigma_x * sigma_y) * np.exp(-0.5 * (k**2) * (sigma_x**2)) / np.sqrt(1.0 + np.exp(-(k**2)*(sigma_x**2)))

def alpha_C_closed(sigma_x, sigma_y, k):
    return sqrt(2*pi) * sqrt(sigma_x * sigma_y) * (1.0 + np.exp(-2.0 * (k**2) * (sigma_x**2))) / np.sqrt(1.0 + np.exp(-(k**2)*(sigma_x**2)))

def F_dilution(delta_theta, sigma_theta):
    if delta_theta <= 0:
        return 1.0
    a = delta_theta / (2.0 * sqrt(2) * sigma_theta)
    integral = sqrt(2*pi) * sigma_theta * erf(a)
    return integral / delta_theta

def Beta(sigma_x, sigma_y, k, delta_theta, sigma_theta):
    alpha_R = alpha_R_closed(sigma_x, sigma_y, k)
    alpha_C = alpha_C_closed(sigma_x, sigma_y, k)
    F = F_dilution(delta_theta, sigma_theta)
    return (alpha_C / alpha_R) * F

def phase_diagram_data(kx_range=(0.1, 4.0), n_points=500):
    kx_vals = np.linspace(kx_range[0], kx_range[1], n_points)
    u = kx_vals**2
    ratio = 0.5 * (np.exp(0.5*u) + np.exp(-1.5*u)) / (1 + np.exp(-u))
    return kx_vals, ratio
