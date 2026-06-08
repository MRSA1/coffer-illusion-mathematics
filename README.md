# Mathematics Behind Coffer Illusion

This repository contains the complete code and supplementary materials for the paper:

**"Mathematics Behind Coffer Illusion: Closed-form Energy Analysis, Perceptual Dominance Inequality and Monte-Carlo Validation"**

**Authors:** Md. Rad Sarar Anando, Md. Towkir Ahmmed Rownak

---

## 📌 Abstract

The Coffer Illusion is an image that can be seen either as a grid of rectangles or as a set of hidden circles. This repository provides the mathematical and computational framework for analyzing why rectangles are seen first and circles emerge later.

We derive closed-form expressions for geometric constants (α_R, α_C, F(Δθ,σ_θ)), establish the perceptual dominance inequality A_R > β·A_C, and validate our theoretical predictions through Monte-Carlo simulations.

---

## 📁 Repository Structure

```
coffer-illusion-mathematics/
├── src/                    # Source code
│   ├── __init__.py         # Package initializer
│   ├── gabor_filters.py    # Gabor kernel generation (Eq. 2)
│   ├── closed_form.py      # Closed-form α_R, α_C, F(Δθ,σ_θ) (Eq. 4,5,6)
│   ├── monte_carlo.py      # Monte-Carlo simulation (Table 1)
│   └── figures.py          # Figure generation S1-S5
├── figures/                # Generated figures
│   ├── Figure_S1_Phase_Diagram.png
│   ├── Figure_S2_Phase_Diagram_2D.png
│   ├── Figure_S3_Monte_Carlo_Scatter.png
│   ├── Figure_S4_AC_Comparison.png
│   └── Figure_S5_Gabor_Kernel.png
├── notebooks/              # Jupyter notebooks
├── data/                   # Simulation results
├── requirements.txt        # Python dependencies
├── LICENSE                 # MIT License
└── README.md               # This file
```

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

**Required packages:**
- numpy ≥ 1.21.0
- matplotlib ≥ 3.5.0
- scipy ≥ 1.7.0
- pandas ≥ 1.3.0
- jupyter ≥ 1.0.0

---

## 🚀 Usage

### Generate all figures (S1-S5):

```bash
python src/figures.py
```

### Run Monte-Carlo simulation:

```bash
python src/monte_carlo.py
```

### Compute closed-form constants:

```python
from src.closed_form import alpha_R_closed, alpha_C_closed, F_dilution, Beta
import numpy as np

# Parameters
sigma_x = sigma_y = 4.0      # Gaussian envelope width (pixels)
wavelength = 8.0              # Stripe wavelength (pixels)
k = 2 * np.pi / wavelength    # Angular spatial frequency

# Compute constants
alpha_R = alpha_R_closed(sigma_x, sigma_y, k)   # Step edge gain
alpha_C = alpha_C_closed(sigma_x, sigma_y, k)   # Stripe gain
F = F_dilution(delta_theta=0.133, sigma_theta=0.35)  # Orientation dilution
beta = Beta(sigma_x, sigma_y, k, 0.133, 0.35)   # Dominance threshold

print(f"α_R = {alpha_R:.6f}")
print(f"α_C = {alpha_C:.6f}")
print(f"α_C/α_R = {alpha_C/alpha_R:.6f}")
print(f"β = {beta:.6f}")
```

### Interactive exploration:

```bash
jupyter notebook notebooks/coffer_illusion_demo.ipynb
```

---

## 📊 Figures

| Figure | Description | Paper Reference |
|:------:|-------------|:---------------:|
| **S1** | 1D Phase Diagram: α_C/α_R vs kσ_x | Main Paper Fig. 2 |
| **S2** | 2D Phase Diagram: α_C/α_R vs kσ_x and σ_x/σ_y | SM Eq. S14 |
| **S3** | Monte-Carlo Scatter Plot (four outcome categories) | Main Paper Table 1 |
| **S4** | Example images for different A_C values | Main Paper Eq. 1 |
| **S5** | Gabor kernel visualization | Main Paper Eq. 2, SM Eq. S2 |

### Figure Previews

**Figure S1: Phase Diagram** - Shows the ratio α_C/α_R as a function of kσ_x

**Figure S2: 2D Phase Diagram** - Contour plot showing α_C/α_R vs kσ_x and σ_x/σ_y

**Figure S3: Monte-Carlo Scatter Plot** - Four outcome categories (Local Only, Global Only, Both, Neither)

**Figure S4: AC Comparison** - Example images with A_C = 0.1, 0.5, 1.2

**Figure S5: Gabor Kernel** - Visualization of unnormalized and normalized Gabor filters

---

## 📐 Key Mathematical Results

### Closed-Form Constants (Paper Eqs. 4, 5, 6)

| Constant | Expression | Value (Typical) |
|:--------:|:----------:|:---------------:|
| **α_R** | Step edge gain | 10.026254 |
| **α_C** | Stripe gain | 7.455000 |
| **α_C/α_R** | Gain ratio | 0.743600 |
| **F(Δθ,σ_θ)** | Orientation dilution | 0.892000 |
| **β** | Dominance threshold | 0.663000 |

### Perceptual Dominance Inequality (Paper Eq. 7)

> **Local detectors favor rectangles when:** 
> 
> $$A_R > \beta \cdot A_C$$
> 
> where $\beta = \frac{\alpha_C}{\alpha_R} \times F(\Delta\theta, \sigma_\theta)$

### Physical Interpretation

- When **A_R > β·A_C** → Rectangle perception dominates (seen first)
- When **A_R < β·A_C** → Circle perception emerges later
- The threshold β depends on:
  - Gabor filter parameters (σ_x, σ_y, k)
  - Local orientation spread (Δθ)
  - Neural orientation tuning width (σ_θ)

---

## 📊 Monte-Carlo Simulation Results (Table 1)

| Category | Percentage | Interpretation |
|:--------:|:----------:|:---------------|
| **Local Only** | ≈42% | Rectangle dominant (seen first) |
| **Global Only** | ≈26% | Circle detected (emerges later) |
| **Both** | ≈19% | Both cues present simultaneously |
| **Neither** | ≈13% | No clear dominance |

*Results from 200 trials with random A_C (0-1.6), radius (8-40 px), wavelength (6-12 px)*

---

## 📖 Citation

If you use this code in your research, please cite:

```bibtex
@article{anando2026coffer,
  title={Mathematics Behind Coffer Illusion: Closed-form Energy Analysis, 
         Perceptual Dominance Inequality and Monte-Carlo Validation},
  author={Anando, Md. Rad Sarar and Rownak, Md. Towkir Ahmmed},
  journal={Young Scientist},
  year={2026},
  note={in review}
}
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Md. Rad Sarar Anando**  
📨 radsararanando@gmail.com



---

## 🙏 Acknowledgments

We thank the reviewers for their valuable comments and suggestions that helped improve this work.

---

## 🔗 Repository Link

**https://github.com/MRSA1/coffer-illusion-mathematics**



---



*Last updated: June 2026*
```
