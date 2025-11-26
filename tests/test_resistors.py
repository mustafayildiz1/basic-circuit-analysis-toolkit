from circuit_toolkit import (
    total_series_resistance,
    total_parallel_resistance,
    voltage_divider,
)


def test_series_resistance_simple():
    assert total_series_resistance([100, 200, 300]) == 600.0


def test_parallel_resistance_simple():
    # 100 || 100 = 50 ohms
    r = total_parallel_resistance([100, 100])
    assert abs(r - 50.0) < 1e-6


def test_voltage_divider_half():
    # 10 V, R_top = 1k, R_bottom = 1k → 5 V out
    v_out = voltage_divider(10.0, 1000.0, 1000.0)
    assert abs(v_out - 5.0) < 1e-6
