from Calculator import Calculator
import pandas as pd
from pathlib import Path

# Example
data = pd.read_csv(Path("draft-data-20-years.csv"))
calculator = Calculator(data)

# Enter in any value such as 3P%, MPG, PPG, ...
calculator.get_points("FT%")
print(calculator.data["FT%"])






