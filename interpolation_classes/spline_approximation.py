from approximation_strategy import ApproximationStrategy
import numpy as np

class SplineApproximation(ApproximationStrategy):
  
  def __init__(self):
    self.cubicPolynomialArr = []

  def approximate(self, x_arr, y_arr):
    n = len(x_arr) - 1
    h = [x_arr[i + 1] - x_arr[i] for i in range(n)]

    alpha = [0] * (n + 1)
    for i in range(1, n):
        alpha[i] = 3 * (y_arr[i + 1] - y_arr[i]) / h[i] - 3 * (y_arr[i] - y_arr[i - 1]) / h[i - 1]

    l = [1] + [0] * n
    mu = [0] * (n + 1)
    z = [0] * (n + 1)

    for i in range(1, n):
        l[i] = 2 * (x_arr[i + 1] - x_arr[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    l[n] = 1
    z[n] = 0
    c = [0] * (n + 1)
    b = [0] * (n + 1)
    d = [0] * (n + 1)

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y_arr[j + 1] - y_arr[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    coefficients = [[y_arr[i], b[i], c[i], d[i]] for i in range(n)]
    return coefficients

