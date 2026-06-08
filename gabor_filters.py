import numpy as np

def gabor_kernel(size, wavelength, theta, sigma_x, sigma_y, phase=0.0):
    half = size // 2
    y, x = np.mgrid[-half:half+1, -half:half+1]
    x_theta = x * np.cos(theta) + y * np.sin(theta)
    y_theta = -x * np.sin(theta) + y * np.cos(theta)
    exp_part = np.exp(-0.5 * ((x_theta**2)/(sigma_x**2) + (y_theta**2)/(sigma_y**2)))
    cos_part = np.cos(2*np.pi * x_theta / wavelength + phase)
    kernel = exp_part * cos_part
    kernel = kernel / np.sqrt(np.sum(kernel**2))
    return kernel

def center_response(img, kernel):
    N = img.shape[0]
    h = kernel.shape[0] // 2
    cx, cy = N // 2, N // 2
    region = img[cx-h:cx-h+kernel.shape[0], cy-h:cy-h+kernel.shape[1]]
    return np.sum(region * kernel)
