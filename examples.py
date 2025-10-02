"""
Example Script: Quick Start with Snowball Earth Model
=======================================================

This script demonstrates basic usage of the Snowball Earth model.
Perfect for getting started quickly!
"""

from snowball_earth_model import (
    find_equilibrium_temperature, 
    energy_balance,
    plot_energy_balance_curve
)
import numpy as np


def example_1_current_earth():
    """Example 1: Find equilibrium temperature for current Earth"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Current Earth Conditions")
    print("="*60)
    
    temp, converged = find_equilibrium_temperature(
        initial_temp=288,  # Start near current temperature
        solar_multiplier=1.0  # Current solar constant
    )
    
    print(f"\nEquilibrium Temperature: {temp:.2f} K ({temp-273.15:.2f} °C)")
    print(f"Converged: {converged}")
    print("\nNote: This is a simplified model. Real Earth has more complex processes!")


def example_2_reduced_solar():
    """Example 2: What if the sun were dimmer?"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Reduced Solar Input (Faint Young Sun)")
    print("="*60)
    
    # During Earth's early history, the sun was ~30% dimmer
    temp, converged = find_equilibrium_temperature(
        initial_temp=288,
        solar_multiplier=0.7  # 30% reduction
    )
    
    print(f"\nWith 30% less solar input:")
    print(f"Equilibrium Temperature: {temp:.2f} K ({temp-273.15:.2f} °C)")
    print(f"Converged: {converged}")
    
    if temp < 273.15:
        print("\n⚠️  WARNING: Temperature below freezing!")
        print("This would lead to a Snowball Earth!")


def example_3_energy_balance():
    """Example 3: Calculate energy balance at different temperatures"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Energy Balance at Different Temperatures")
    print("="*60)
    
    temperatures = [250, 273.15, 288, 300]  # K
    
    print("\nEnergy balance for current solar input:")
    print("Temperature (K) | Temperature (°C) | Balance (W/m²)")
    print("-" * 60)
    
    for T in temperatures:
        balance = energy_balance(T, solar_multiplier=1.0)
        print(f"    {T:6.2f}      |     {T-273.15:6.2f}      |    {balance:6.2f}")
    
    print("\nPositive balance = warming, Negative balance = cooling")


def example_4_snowball_threshold():
    """Example 4: Find the Snowball Earth threshold"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Finding the Snowball Threshold")
    print("="*60)
    
    print("\nTesting different solar inputs...")
    
    # Try a range of solar multipliers
    solar_values = [1.0, 0.95, 0.90, 0.85]
    
    print("\nSolar Mult. | Eq. Temp (K) | Eq. Temp (°C) | Status")
    print("-" * 60)
    
    for s in solar_values:
        temp, converged = find_equilibrium_temperature(288, s)
        status = "FROZEN ❄️" if temp < 273.15 else "Liquid 💧"
        print(f"   {s:.2f}     |   {temp:6.2f}    |    {temp-273.15:6.2f}     | {status}")


def example_5_visualization():
    """Example 5: Create visualizations"""
    print("\n" + "="*60)
    print("EXAMPLE 5: Creating Visualizations")
    print("="*60)
    
    print("\nGenerating energy balance curves...")
    
    # Current Earth
    print("  - Plotting for current solar input...")
    plot_energy_balance_curve(solar_multiplier=1.0)
    
    # Reduced solar (near Snowball threshold)
    print("  - Plotting for reduced solar input...")
    plot_energy_balance_curve(solar_multiplier=0.92)
    
    print("\nPlots saved! Check the PNG files in the directory.")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("SNOWBALL EARTH MODEL - QUICK START EXAMPLES")
    print("="*60)
    print("\nThis script shows you how to use the model.")
    print("You can run each example separately or all together.")
    
    # Run all examples
    example_1_current_earth()
    example_2_reduced_solar()
    example_3_energy_balance()
    example_4_snowball_threshold()
    example_5_visualization()
    
    print("\n" + "="*60)
    print("DONE! Now try modifying the examples to explore more!")
    print("="*60)
    print("\nSuggestions:")
    print("- Try different solar multipliers")
    print("- Modify the albedo or greenhouse parameters in snowball_earth_model.py")
    print("- Calculate the critical solar reduction for Snowball Earth")
    print()
