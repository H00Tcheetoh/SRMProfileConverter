import numpy as np
import matplotlib.pyplot as plt
import math

def taylor_series_exp(x, n_terms):
    result = 0
    for n in range(n_terms):
        result += x**n / math.factorial(n)
    return result

# Define the range of x values
x_values = np.linspace(-2, 2, 400)

# Compute the Taylor series approximation for different numbers of terms
y_values_5 = [taylor_series_exp(x, 5) for x in x_values]
y_values_10 = [taylor_series_exp(x, 10) for x in x_values]
y_values_20 = [taylor_series_exp(x, 20) for x in x_values]

# Compute the actual e^x values
y_actual = np.exp(x_values)

# Plot the results
plt.plot(x_values, y_actual, label='e^x', color='black')
plt.plot(x_values, y_values_5, label='Taylor Series (5 terms)', linestyle='--')
plt.plot(x_values, y_values_10, label='Taylor Series (10 terms)', linestyle='-.')
plt.plot(x_values, y_values_20, label='Taylor Series (20 terms)', linestyle=':')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Taylor Series Approximation of $e^x$')
plt.legend()
plt.grid(True)
plt.show()