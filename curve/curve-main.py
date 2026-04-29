import numpy as np
import matplotlib.pyplot as plt

# Define x values
x = np.linspace(-10, 10, 400)

# Define which n values to plot
n_values = [2, 4, 6, 8]

# Create the plot
plt.figure(figsize=(10, 6))

for n in n_values:
    if n < 0:
        # For negative powers, skip x=0
        x_plot = x[x != 0]
        y = x_plot ** n
        plt.plot(x_plot, y, label=f'n = {n}', linewidth=2)
    else:
        y = x ** n
        plt.plot(x, y, label=f'n = {n}', linewidth=2)

# Add reference lines
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='black', linestyle='-', alpha=0.3)
plt.grid(True, alpha=0.3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Power Functions: y = xⁿ')
plt.legend()
plt.xlim(-5, 5)
plt.ylim(-100, 100)
plt.show()