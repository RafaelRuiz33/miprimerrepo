import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# NumPy: crear un arreglo
arr = np.array([1, 2, 3, 4, 5])
print("Array NumPy:", arr)

# Pandas: crear un DataFrame
df = pd.DataFrame({"Columna1": [10, 20, 30], "Columna2": [40, 50, 60]})
print("\nDataFrame Pandas:\n", df)

# Matplotlib: graficar
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Gráfico de prueba")
plt.show()