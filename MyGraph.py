import matplotlib.pyplot as plt #would give error if we ran in root bc only installed in ve
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")
