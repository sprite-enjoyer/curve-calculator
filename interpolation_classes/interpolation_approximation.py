from . import approximation_strategy

class InterpolationStrategy(approximation_strategy.ApproximationStrategy):

  def __init__(self):
    pass

  def approximate(self, x_arr, y_arr):
    n = len(x_arr)
    results = []

    for x_interp in x_arr:
        result = 0
        for j in range(n):
            term = y_arr[j]
            for i in range(n):
                if i != j:
                    if x_arr[j] - x_arr[i] == 0: 
                       term *= 1
                    else:
                      term *= (x_interp - x_arr[i]) / (x_arr[j] - x_arr[i])
            result += term
        results.append(result)

    return results 

  def gaussian_elimination(self, A, B):
    n = len(A)

    for i in range(n):
        A[i].extend(B[i])

    for i in range(n):
        diag = A[i][i]
        for j in range(i, n + 1):
            A[i][j] /= diag

        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(i, n + 1):
                    A[k][j] -= factor * A[i][j]

    coefficients = [row[-1] for row in A]

    return coefficients[:4]
  
  def draw(self):
    pass
  
  
  