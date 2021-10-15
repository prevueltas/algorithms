import numpy as np
import matplotlib.pyplot as plt

# x - coordinates
x = np.arange(0, 10, 0.1)

# y - coordinates
y_log = np.log2(x)
y_linear = x
y_linear_log = y_log * y_linear
y_quadratic = x * x

plt.plot(x, y_log)
plt.plot(x, y_linear)
plt.plot(x, y_linear_log)
plt.plot(x, y_quadratic)

plt.show()
