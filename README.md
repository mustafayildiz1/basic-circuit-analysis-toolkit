# Basic Circuit Analysis Toolkit ⚡

This project is a small collection of **Python utilities** for very simple DC circuit analysis.  
It is designed as a learning project that combines my **Electrical & Electronics Engineering** background with basic **Python** skills.

The focus is on:
- Ohm’s Law calculations
- Series and parallel resistor combinations
- Simple voltage divider calculations
- A few practical examples (like choosing a resistor for an LED)

---

## 🎯 Goals of the Project

- Practice turning basic engineering formulas into clean Python functions  
- Show clear, readable code that someone else can understand  
- Use Jupyter notebooks to explain engineering logic step by step  
- Add a few simple tests to validate the functions

This is **not** a full simulator. It’s a beginner-level toolkit with well-explained examples.

---

## 🧰 Tech Stack

- Python 3.x  
- Jupyter Notebook  
- (Optional) NumPy for small numeric helpers  
- pytest (for basic unit tests)

---

## 📂 Project Structure

```text
basic-circuit-analysis-toolkit/
├─ README.md
├─ requirements.txt
├─ src/
│   └─ circuit_toolkit/
│       ├─ __init__.py
│       ├─ resistors.py
│       └─ dc_analysis.py
├─ examples/
│   ├─ 01_basic_resistors.ipynb
│   ├─ 02_voltage_divider.ipynb
│   └─ 03_led_resistor_calculation.ipynb
└─ tests/
    └─ test_resistors.py
