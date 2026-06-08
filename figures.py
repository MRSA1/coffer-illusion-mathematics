import numpy as np
import matplotlib.pyplot as plt
from closed_form import phase_diagram_data
from monte_carlo import generate_synthetic_image, run_monte_carlo

def figure_S1():
    kx_vals, ratio = phase_diagram_data()
    plt.figure(figsize=(7, 4))
    plt.plot(kx_vals, ratio, 'b-', linewidth=2)
    plt.xlabel(r'$k\sigma_x$')
    plt.ylabel(r'$\alpha_C / \alpha_R$')
    plt.title('Fig. S1: Phase Diagram')
    plt.grid(True, alpha=0.5)
    plt.axhline(y=1, color='r', linestyle='--')
    plt.savefig('../figures/Figure_S1_Phase_Diagram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: Figure_S1_Phase_Diagram.png")

def figure_S2():
    kx_vals = np.linspace(0.1, 4.0, 200)
    anis_vals = np.linspace(0.2, 5.0, 200)
    KX, ANIS = np.meshgrid(kx_vals, anis_vals)
    u = KX**2
    ratio = 0.5 * (np.exp(0.5*u) + np.exp(-1.5*u)) / (1 + np.exp(-u))
    plt.figure(figsize=(8, 6))
    im = plt.imshow(ratio, origin='lower', extent=[kx_vals.min(), kx_vals.max(), anis_vals.min(), anis_vals.max()], aspect='auto', cmap='viridis')
    plt.colorbar(im, label=r'$\alpha_C / \alpha_R$')
    plt.xlabel(r'$k\sigma_x$')
    plt.ylabel(r'anisotropy $\sigma_x / \sigma_y$')
    plt.title('Fig. S2: 2-Parameter Phase Diagram')
    plt.savefig('../figures/Figure_S2_Phase_Diagram_2D.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: Figure_S2_Phase_Diagram_2D.png")

def figure_S3():
    results = run_monte_carlo(200)
    local_only_A, local_only_r = [], []
    global_only_A, global_only_r = [], []
    both_A, both_r = [], []
    neither_A, neither_r = [], []
    for A_C, radius, _, local_pref, global_det in results:
        if local_pref and not global_det:
            local_only_A.append(A_C); local_only_r.append(radius)
        elif not local_pref and global_det:
            global_only_A.append(A_C); global_only_r.append(radius)
        elif local_pref and global_det:
            both_A.append(A_C); both_r.append(radius)
        else:
            neither_A.append(A_C); neither_r.append(radius)
    plt.figure(figsize=(8, 6))
    plt.scatter(local_only_A, local_only_r, c='C0', marker='s', s=50, alpha=0.7, label='Local Only')
    plt.scatter(global_only_A, global_only_r, c='C1', marker='o', s=50, alpha=0.7, label='Global Only')
    plt.scatter(both_A, both_r, c='C2', marker='^', s=60, alpha=0.7, label='Both')
    plt.scatter(neither_A, neither_r, c='C3', marker='x', s=40, alpha=0.5, label='Neither')
    plt.xlabel(r'$A_C$')
    plt.ylabel('Circle radius (pixels)')
    plt.title('Fig. S3: Monte-Carlo Simulation Outcomes')
    plt.legend()
    plt.savefig('../figures/Figure_S3_Monte_Carlo_Scatter.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: Figure_S3_Monte_Carlo_Scatter.png")

def figure_S4():
    A_C_vals = [0.1, 0.5, 1.2]
    titles = [r'$A_C = 0.1$ (Rectangle dominant)', r'$A_C = 0.5$ (Intermediate)', r'$A_C = 1.2$ (Circle dominant)']
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    for i, (ac, title) in enumerate(zip(A_C_vals, titles)):
        I, _, _ = generate_synthetic_image(ac, radius=30, wavelength=10, size=256)
        axes[i].imshow(I, cmap='gray')
        axes[i].set_title(title)
        axes[i].axis('off')
    plt.suptitle('Fig. S4: Effect of Circular Stripe Amplitude $A_C$')
    plt.savefig('../figures/Figure_S4_AC_Comparison.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: Figure_S4_AC_Comparison.png")

def figure_S5():
    from gabor_filters import gabor_kernel
    size, sigma, wavelength = 31, 4.0, 8.0
    k = 2 * np.pi / wavelength
    kernel = gabor_kernel(size, wavelength, theta=0, sigma_x=sigma, sigma_y=sigma)
    half = size // 2
    y, x = np.mgrid[-half:half+1, -half:half+1]
    g0 = np.exp(-0.5 * ((x**2)/(sigma**2) + (y**2)/(sigma**2)))
    tildeG = g0 * np.cos(k * x)
    step = np.sign(x)
    stripe = np.cos(k * x)
    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    axes[0].imshow(tildeG, cmap='RdBu'); axes[0].set_title('Unnormalized Gabor'); axes[0].axis('off')
    axes[1].imshow(kernel, cmap='RdBu'); axes[1].set_title('Normalized Gabor'); axes[1].axis('off')
    axes[2].imshow(step, cmap='gray'); axes[2].set_title('Step edge'); axes[2].axis('off')
    axes[3].imshow(stripe, cmap='gray'); axes[3].set_title('Stripe'); axes[3].axis('off')
    plt.suptitle('Fig. S5: Gabor Kernel and Components')
    plt.savefig('../figures/Figure_S5_Gabor_Kernel.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("Saved: Figure_S5_Gabor_Kernel.png")

def generate_all_figures():
    print("Generating all figures...")
    figure_S1()
    figure_S2()
    figure_S3()
    figure_S4()
    figure_S5()
    print("All figures generated successfully!")

if __name__ == "__main__":
    generate_all_figures()
