"""
Basic resistor calculations for simple DC circuits.
All resistances are in ohms (Ω), voltage in volts (V), current in amperes (A).
"""

from typing import List


def total_series_resistance(resistors: List[float]) -> float:
    """
    Return the total resistance of resistors connected in series.
    R_total = R1 + R2 + ... + Rn
    """
    if not resistors:
        raise ValueError("Resistor list cannot be empty.")
    if any(r <= 0 for r in resistors):
        raise ValueError("All resistances must be positive.")
    return float(sum(resistors))


def total_parallel_resistance(resistors: List[float]) -> float:
    """
    Return the total resistance of resistors connected in parallel.
    1/R_total = 1/R1 + 1/R2 + ... + 1/Rn
    """
    if not resistors:
        raise ValueError("Resistor list cannot be empty.")
    inv_sum = 0.0
    for r in resistors:
        if r <= 0:
            raise ValueError("All resistances must be positive.")
        inv_sum += 1.0 / r
    return 1.0 / inv_sum


def voltage_divider(v_in: float, r_top: float, r_bottom: float) -> float:
    """
    Simple voltage divider:
    V_out = V_in * (R_bottom / (R_top + R_bottom))
    """
    if r_top <= 0 or r_bottom <= 0:
        raise ValueError("Resistances must be positive.")
    return v_in * (r_bottom / (r_top + r_bottom))
