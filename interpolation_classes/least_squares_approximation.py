from approximation_strategy import ApproximationStrategy
import numpy as np

class LeastSquaresApproximation(ApproximationStrategy):
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




