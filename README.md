# SnowballEarth
Code for Snowball Earth in Earth and Climate Physics

## Description
This repository contains a numerical model for simulating Snowball Earth conditions using an energy balance model (EBM). The model explores how changes in solar radiation affect Earth's climate and can lead to global glaciation events.

## Features
- Energy balance model with ice-albedo feedback
- Greenhouse effect parameterization
- Equilibrium temperature calculations
- Visualization of energy balance curves
- Snowball Earth threshold experiments

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/ThorHMW/SnowballEarth.git
   cd SnowballEarth
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Model
Simply run the main Python script:
```bash
python snowball_earth_model.py
```

This will:
- Calculate equilibrium temperatures for various solar inputs
- Generate plots showing the Snowball Earth threshold
- Display energy balance curves

### Output
The model generates two main plots:
- `snowball_experiment.png`: Shows how equilibrium temperature varies with solar input
- `energy_balance_curve.png`: Shows energy balance as a function of temperature

### Customizing the Model
You can modify parameters in the code:
- `SOLAR_CONSTANT`: Adjust the solar constant (default: 1365 W/m²)
- `albedo()`: Modify ice-albedo feedback parameters
- `greenhouse_effect()`: Adjust greenhouse gas effects

### Example Code
```python
from snowball_earth_model import find_equilibrium_temperature, plot_energy_balance_curve

# Find equilibrium for reduced solar input
temp, converged = find_equilibrium_temperature(
    initial_temp=288,
    solar_multiplier=0.95
)
print(f"Equilibrium temperature: {temp:.2f} K")

# Plot energy balance curve
plot_energy_balance_curve(solar_multiplier=0.95)
```

## Model Description

### Energy Balance
The model balances incoming solar radiation with outgoing longwave radiation:

**Energy In:** (1 - α) × S / 4

**Energy Out:** ε × σ × T⁴

Where:
- α = albedo (reflectivity)
- S = solar constant
- ε = emissivity (greenhouse effect)
- σ = Stefan-Boltzmann constant
- T = temperature

### Ice-Albedo Feedback
When temperatures drop below freezing, ice forms and increases the planet's albedo (reflectivity), creating a positive feedback that can lead to runaway cooling—the Snowball Earth condition.

## Collaboration
This code is designed for collaborative learning. Feel free to:
- Modify parameters to explore different scenarios
- Add new features (e.g., latitude-dependent models)
- Improve the physical parameterizations
- Create additional visualization tools

## License
This is educational code for the Earth and Climate Physics class.
