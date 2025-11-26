"""
Very simple DC circuit helpers built on top of the resistor utilities.
"""

from typing import List, Dict
from .resistors import total_series_resistance


def solve_series_circuit(v_supply: float, resistors: List[float]) -> Dict[str, object]:
    """
    For a simple series circuit:
    - All resistors share the same current.
    - Voltage drops add up to the supply voltage.

    Returns a dict with:
        {
          "total_resistance": R_total,
          "current": I,
          "voltages": [V1, V2, ...]
        }
    """
    if v_supply < 0:
        raise ValueError("Supply voltage cannot be negative.")

    r_total = total_series_resistance(resistors)
    if r_total == 0:
        raise ValueError("Total resistance cannot be zero.")

    current = v_supply / r_total
    voltages = [current * r for r in resistors]

    return {
        "total_resistance": r_total,
        "current": current,
        "voltages": voltages,
    }
