# integrate 𝑓(𝑥)=𝑥^2+3𝑥+2
import numpy as np
from scipy import integrate

# Define the variable
x = sp.symbols('x')

# Define the function
f = x**2 + 3*x + 2

# Compute the integral
integral = sp.integrate(f, x)

# Print the result
print("The integral of", f, "is:", integral)


#include numpy and scipy[HOW?]