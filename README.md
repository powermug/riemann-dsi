# Distributional Stability Index (DSI) for Riemann Zeta Zeros

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18108122.svg)](https://doi.org/10.5281/zenodo.18108122)
[![License](https://img.shields.io/badge/License-All%20Rights%20Reserved-red.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This repository contains the computational code for the paper:

> **A Geometric Diagnostic for Riemann Zeta Zero Distribution via the Distributional Stability Index**
> 
> Jeonghoon Lee (2025)

## Overview

The **Distributional Stability Index (DSI)** is a geometric invariant defined as:

$$\Phi = \frac{\text{Var}(X)}{\text{MAD}(X)^2}$$

where Var is the variance and MAD is the mean absolute deviation.

### Key Results

| Distribution | DSI Value |
|--------------|-----------|
| Uniform | 4/3 ≈ 1.3333 |
| Normal | π/2 ≈ 1.5708 |
| Zeta zeros (under RH) | → 4/3 |

Under the Riemann Hypothesis, the DSI of the zero ordinate sequence converges to **exactly 4/3** with rate O(N⁻²).

## Installation

```bash
git clone https://github.com/powermug/riemann-dsi.git
cd riemann-dsi
pip install -r requirements.txt
```

## Quick Start

```python
from src.dsi import compute_dsi, print_convergence_table

# Compute DSI for a sequence
dsi = compute_dsi([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"DSI = {dsi}")  # Output: DSI = 1.32

# Reproduce Table 5.1 from the paper
print_convergence_table()
```

## Reproducing Paper Results

Run the verification script to reproduce all tables from the paper:

```bash
cd src
python verify_tables.py
```

This will output:
- **Table 5.1**: DSI convergence for N = 10² to 10⁶
- **Table 5.2**: Perturbation sensitivity analysis

### Expected Output (Table 5.1)

```
         N |            Φ_N |    |Φ_N - 4/3|
--------------------------------------------------
       100 |    1.3332000000 |       1.33e-04
      1000 |    1.3333320000 |       1.33e-06
     10000 |    1.3333333200 |       1.33e-08
    100000 |    1.3333333332 |       1.33e-10
   1000000 |    1.3333333333 |       1.33e-12
```

## File Structure

```
riemann-dsi/
├── README.md
├── LICENSE
├── requirements.txt
├── src/
│   ├── dsi.py              # Core DSI computation
│   ├── perturbation.py     # Perturbation sensitivity analysis
│   └── verify_tables.py    # Reproduce paper tables
└── notebooks/
    └── DSI_Demo.ipynb      # Interactive demonstration
```

## Mathematical Background

### DSI Definition

For a sequence {x₁, x₂, ..., xₙ} with mean μ:

$$\Phi_N = \frac{\frac{1}{N}\sum_{k=1}^{N}(x_k - \mu)^2}{\left(\frac{1}{N}\sum_{k=1}^{N}|x_k - \mu|\right)^2}$$

### Convergence Under RH

If all Riemann zeta zeros lie on the critical line (σ = 1/2), then R_k = k and:

$$\Phi_N = \frac{4}{3}\left(1 - \frac{1}{N^2}\right) \to \frac{4}{3}$$

with convergence rate O(N⁻²).

### Perturbation Sensitivity

If a fraction δ of zeros deviate to σ = 0.6:

| Perturbation | DSI | Deviation |
|--------------|-----|-----------|
| 0% (RH) | 1.3333 | +0.01% |
| 1% | 1.338 | +0.35% |
| 5% | 1.352 | +1.4% |
| 10% | 1.371 | +2.8% |

## Citation

If you use this code, please cite:

```bibtex
@misc{lee_2026_18108122,
  author       = {Lee, Jeonghoon},
  title        = {A Geometric Diagnostic for Riemann Zeta Zero
                   Distribution via the Distributional Stability
                   Index
                  },
  month        = jan,
  year         = 2026,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18108122},
  url          = {https://doi.org/10.5281/zenodo.18108122},
}
```

## License

Copyright (c) 2025 Jeonghoon Lee. All Rights Reserved.

For academic/research use only. Commercial use requires written permission from the author.

Contact: powermug@knou.ac.kr

## Contact

- **Author**: Jeonghoon Lee
- **Email**: powermug@knou.ac.kr
