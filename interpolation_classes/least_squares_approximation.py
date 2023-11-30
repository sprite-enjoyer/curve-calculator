from matplotlib import pyplot as plt
import numpy as np
from . import approximation_strategy

class LeastSquaresApproximation(approximation_strategy.ApproximationStrategy):
  def __init__(self):
    pass

  def approximate(self, x_arr, y_arr):
    x_arr_squared = list(map(lambda x: x**2, x_arr))
    a = np.array([x_arr, x_arr_squared])
    b = np.array(y_arr)
    left = np.matmul(a, a.transpose())
    right = np.matmul(a, b.transpose()) 
    left = np.invert(left)
    right = np.matmul(left, right)
    return [right[1], right[0]]

  def draw(self, a, b):
    x = np.linspace(-10, 10, 100)
    y = a * x + b
    plt.plot(x, y)
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Linear Function: {a}x + {b}')
    plt.legend()
    
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.show()