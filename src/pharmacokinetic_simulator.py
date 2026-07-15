#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PefkouFL-6000mg Biphasic Human Pharmacokinetic Simulation Engine
License: BSL-1.0
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_pharmacokinetic_plot():
    # Construct highly detailed time grid (0 to 72 hours, step resolution 0.1 hr)
    t = np.linspace(0, 72, 1000)
    
    # Mathematical Model Definition: Standardized 300mg Proanthocyanidin Core Matrix
    Dose = 300       # Active constituent mass (mg)
    F = 0.42         # Estimated Bioavailability fraction 
    Vd = 1.8         # Volume of distribution in human tissue (L/kg)
    
    # Phase 1 Parameters: Duodenal Monomer Absorption
    ka1 = 0.85       # Rapid absorption velocity constant (hr^-1)
    ke1 = 0.46       # Fast elimination rate constant (t_1/2 approx 1.5 hr)
    
    # Phase 2 Parameters: Colonic Microbial Cleavage (gamma-valerolactone)
    ka2 = 0.12       # Delayed cleavage/absorption constant (hr^-1)
    ke2 = 0.051      # Prolonged elimination rate constant (t_1/2 approx 13.5 hr)
    lag_phase = 6.0  # Lag-time for intestinal transit to lower colon (hours)
    
    # Initialize concentration array profiles
    C_monomer = (F * Dose * ka1) / (Vd * (ka1 - ke1)) * (np.exp(-ke1 * t) - np.exp(-ka1 * t))
    C_metabolite = np.zeros_like(t)
    
    # Apply colonic lag shift to Phase 2 modeling
    mask = t >= lag_phase
    t_lag = t[mask] - lag_phase
    C_metabolite[mask] = (F * Dose * 0.75 * ka2) / (Vd * (ka2 - ke2)) * (np.exp(-ke2 * t_lag) - np.exp(-ka2 * t_lag))
    
    # Combined Multi-Dose Simulation: 24-hour interval accumulation (tau = 24)
    C_total = C_monomer + C_metabolite
    for tau in:
        mask_tau = t >= tau
        t_tau = t[mask_tau] - tau
        C_m_new = (F * Dose * ka1) / (Vd * (ka1 - ke1)) * (np.exp(-ke1 * t_tau) - np.exp(-ka1 * t_tau))
        C_met_new = np.zeros_like(t_tau)
        
        mask_met = t_tau >= lag_phase
        t_met_lag = t_tau[mask_met] - lag_phase
        C_met_new[mask_met] = (F * Dose * 0.75 * ka2) / (Vd * (ka2 - ke2)) * (np.exp(-ke2 * t_met_lag) - np.exp(-ka2 * t_met_lag))
        
        C_total[mask_tau] += (C_m_new + C_met_new)

    # Begin high-resolution rendering with dark grid notebook formatting
    plt.figure(figsize=(11, 5.5))
    plt.plot(t, C_total, color='#008080', linewidth=2.5, label=r'Total Sustained Plasma Response ($C_{ss}$)')
    plt.plot(t, C_monomer, color='#E67E22', linewidth=1.5, linestyle='--', label='Phase 1: Duodenal Monomer Peak')
    plt.plot(t, C_metabolite, color='#27AE60', linewidth=1.5, linestyle=':', label=r'Phase 2: Colonic $\gamma$-Valerolactone Peak')
    
    # Render safety boundaries and text identifiers
    plt.axhline(y=14.0, color='#C0392B', linestyle='-.', linewidth=1.2, label='Vascular Permeability Ceiling Threshold')
    plt.title('PefkouFL-6000mg Biphasic Human Steady-State Accumulation Simulation', fontsize=12, fontweight='bold', pad=15)
    plt.xlabel('Time Post-Ingestion (Hours)', fontsize=10)
    plt.ylabel('Active Plasma Tracking Concentration (ng/mL)', fontsize=10)
    
    # Configure axes limits and visual anchors
    plt.xlim(0, 72)
    plt.ylim(0, 16)
    plt.xticks(np.arange(0, 73, 4))
    plt.grid(True, which='both', linestyle=':', color='#BDC3C7', alpha=0.6)
    plt.legend(loc='upper right', frameon=True, facecolor='#FFFFFF', edgecolor='#E0E0E0')
    
    # Save asset cleanly to images folder
    plt.tight_layout()
    output_img = "images/biphasic_pharmacokinetic_simulation.png"
    plt.savefig(output_img, dpi=300)
    plt.close()
    
    print(f"[✅ SUCCESS] Pharmacokinetic visualization successfully exported to: {output_img}")

if __name__ == "__main__":
    generate_pharmacokinetic_plot()
