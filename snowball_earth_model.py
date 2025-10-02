"""
Snowball Earth Numerical Model
===============================

This module implements a simple energy balance model (EBM) for studying 
Snowball Earth conditions. The model simulates Earth's climate by balancing 
incoming solar radiation with outgoing longwave radiation.

Author: Earth and Climate Physics Class
Date: 2024
"""

import numpy as np
import matplotlib.pyplot as plt


# Physical Constants
STEFAN_BOLTZMANN = 5.67e-8  # W m^-2 K^-4
SOLAR_CONSTANT = 1365       # W m^-2


def albedo(temperature):
    """
    Calculate albedo as a function of temperature.
    
    Ice-albedo feedback: When temperature drops below freezing,
    ice forms and increases albedo.
    
    Parameters:
    -----------
    temperature : float or array
        Temperature in Kelvin
        
    Returns:
    --------
    alpha : float or array
        Albedo (0-1)
    """
    # Simple parameterization with ice-albedo feedback
    T_freeze = 273.15  # K
    alpha_ice = 0.6    # High albedo for ice
    alpha_water = 0.3  # Lower albedo for water
    
    # Smooth transition using tanh function
    alpha = alpha_water + (alpha_ice - alpha_water) * 0.5 * (1 - np.tanh((temperature - T_freeze) / 10))
    
    return alpha


def greenhouse_effect(temperature):
    """
    Simple greenhouse effect parameterization.
    
    Parameters:
    -----------
    temperature : float or array
        Temperature in Kelvin
        
    Returns:
    --------
    epsilon : float or array
        Effective emissivity (0-1)
    """
    # Simple parameterization: emissivity increases slightly with temperature
    # (more water vapor at higher temperatures)
    epsilon_base = 0.61
    epsilon_sensitivity = 0.0001
    
    epsilon = epsilon_base + epsilon_sensitivity * (temperature - 273.15)
    
    # Keep epsilon bounded between 0.5 and 0.8
    epsilon = np.clip(epsilon, 0.5, 0.8)
    
    return epsilon


def energy_balance(temperature, solar_multiplier=1.0):
    """
    Calculate energy balance for given temperature.
    
    Energy in = (1 - albedo) * S / 4
    Energy out = epsilon * sigma * T^4
    
    Parameters:
    -----------
    temperature : float or array
        Temperature in Kelvin
    solar_multiplier : float
        Factor to multiply solar constant (e.g., 0.94 for faint young sun)
        
    Returns:
    --------
    balance : float or array
        Energy balance (positive = warming, negative = cooling)
    """
    S = SOLAR_CONSTANT * solar_multiplier
    alpha = albedo(temperature)
    epsilon = greenhouse_effect(temperature)
    
    # Incoming solar radiation (averaged over sphere)
    energy_in = (1 - alpha) * S / 4
    
    # Outgoing longwave radiation
    energy_out = epsilon * STEFAN_BOLTZMANN * temperature**4
    
    balance = energy_in - energy_out
    
    return balance


def find_equilibrium_temperature(initial_temp=288, solar_multiplier=1.0, 
                                  max_iterations=1000, tolerance=0.01):
    """
    Find equilibrium temperature by iterating energy balance.
    
    Parameters:
    -----------
    initial_temp : float
        Initial guess for temperature (K)
    solar_multiplier : float
        Solar constant multiplier
    max_iterations : int
        Maximum number of iterations
    tolerance : float
        Convergence tolerance (W m^-2)
        
    Returns:
    --------
    temperature : float
        Equilibrium temperature in Kelvin
    converged : bool
        Whether the solution converged
    """
    temperature = initial_temp
    dt = 0.1  # Time step factor for convergence
    
    for i in range(max_iterations):
        balance = energy_balance(temperature, solar_multiplier)
        
        # Check for convergence
        if abs(balance) < tolerance:
            return temperature, True
        
        # Update temperature based on energy imbalance
        # Positive balance -> warming, negative -> cooling
        temperature += dt * balance
        
        # Prevent unphysical temperatures
        temperature = np.clip(temperature, 150, 400)
    
    return temperature, False


def plot_energy_balance_curve(solar_multiplier=1.0):
    """
    Plot energy balance as a function of temperature.
    
    This shows the stable and unstable equilibrium points.
    
    Parameters:
    -----------
    solar_multiplier : float
        Solar constant multiplier
    """
    # Temperature range to explore
    temperatures = np.linspace(200, 320, 200)
    
    # Calculate energy balance for each temperature
    balance = energy_balance(temperatures, solar_multiplier)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(temperatures, balance, 'b-', linewidth=2, label='Energy Balance')
    plt.axhline(y=0, color='k', linestyle='--', label='Equilibrium')
    plt.grid(True, alpha=0.3)
    plt.xlabel('Temperature (K)', fontsize=12)
    plt.ylabel('Energy Balance (W m$^{-2}$)', fontsize=12)
    plt.title(f'Energy Balance Model (Solar multiplier = {solar_multiplier:.2f})', fontsize=14)
    plt.legend()
    
    # Mark zero crossings (equilibria)
    zero_crossings = np.where(np.diff(np.sign(balance)))[0]
    for idx in zero_crossings:
        T_eq = temperatures[idx]
        plt.plot(T_eq, 0, 'ro', markersize=10)
        plt.text(T_eq, 5, f'T = {T_eq:.1f} K', ha='center')
    
    plt.tight_layout()
    plt.savefig('energy_balance_curve.png', dpi=150)
    print("Energy balance curve saved as 'energy_balance_curve.png'")
    plt.show()


def run_snowball_experiment():
    """
    Run a Snowball Earth experiment by varying solar constant.
    
    This explores how reducing solar input can lead to a Snowball Earth state.
    """
    print("=" * 60)
    print("SNOWBALL EARTH NUMERICAL MODEL")
    print("=" * 60)
    print()
    
    # Test different solar multipliers
    solar_multipliers = np.linspace(0.85, 1.05, 20)
    equilibrium_temps = []
    
    print("Finding equilibrium temperatures for different solar inputs...")
    print()
    
    for solar_mult in solar_multipliers:
        # Try warm initial condition
        T_warm, converged_warm = find_equilibrium_temperature(
            initial_temp=288, solar_multiplier=solar_mult
        )
        
        # Try cold initial condition
        T_cold, converged_cold = find_equilibrium_temperature(
            initial_temp=230, solar_multiplier=solar_mult
        )
        
        # Use the temperature that converged (prefer warm if both converged)
        if converged_warm:
            equilibrium_temps.append(T_warm)
        elif converged_cold:
            equilibrium_temps.append(T_cold)
        else:
            equilibrium_temps.append(np.nan)
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(solar_multipliers, equilibrium_temps, 'bo-', linewidth=2, markersize=6)
    plt.axhline(y=273.15, color='r', linestyle='--', label='Freezing Point')
    plt.grid(True, alpha=0.3)
    plt.xlabel('Solar Multiplier', fontsize=12)
    plt.ylabel('Equilibrium Temperature (K)', fontsize=12)
    plt.title('Snowball Earth: Temperature vs Solar Input', fontsize=14)
    plt.legend()
    plt.tight_layout()
    plt.savefig('snowball_experiment.png', dpi=150)
    print("Snowball experiment plot saved as 'snowball_experiment.png'")
    plt.show()
    
    # Print summary
    print()
    print("Summary of Results:")
    print("-" * 60)
    print(f"Current Earth (S = 1.00): T_eq = {equilibrium_temps[10]:.2f} K ({equilibrium_temps[10]-273.15:.2f} °C)")
    print()
    
    # Find critical solar multiplier for Snowball
    below_freezing = np.array(equilibrium_temps) < 273.15
    if np.any(below_freezing):
        critical_idx = np.where(below_freezing)[0][0]
        critical_solar = solar_multipliers[critical_idx]
        print(f"Snowball Earth occurs when solar multiplier < {critical_solar:.3f}")
        print(f"This corresponds to ~{(1-critical_solar)*100:.1f}% reduction in solar input")
    
    print()
    print("=" * 60)


if __name__ == "__main__":
    # Run the main Snowball Earth experiment
    run_snowball_experiment()
    
    # Plot energy balance curve for current solar constant
    print("\nPlotting energy balance curve...")
    plot_energy_balance_curve(solar_multiplier=1.0)
    
    # Example: Plot for reduced solar constant (Snowball condition)
    print("\nPlotting energy balance curve for reduced solar input...")
    plot_energy_balance_curve(solar_multiplier=0.92)
