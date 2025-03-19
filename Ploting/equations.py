# Import libraries
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (10, 5))


# Creating vectors X and Y
x = np.linspace(1, 50, 100)
f = x * np.log(x) + 100
c = 6
g = x * np.log(x)

# Create the plot
plt.plot(x, f, label="f(n)=nlogn + 100")
plt.plot(x, c*g, label="c*g(n)=6*nlogn")
plt.axvline(x=10, color="green", linestyle="--", label="n0=10")

# Add features to our figure
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Show the plot
plt.show()
