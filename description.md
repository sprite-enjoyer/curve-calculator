### Approximation Methods:

1. **Least Squares Approximation:**

   - **Method in Code:** Uses the least squares method to fit a linear function (\(ax + b\)) to the given data points.
   - **Code Highlights:**
     - Utilizes the numpy library for matrix operations.
     - Draws the linear function using matplotlib.

2. **Spline Approximation:**

   - **Method in Code:** Uses cubic splines to interpolate between data points, resulting in a piecewise cubic function.
   - **Code Highlights:**
     - Calculates coefficients for cubic polynomials for each interval between data points.
     - Draws the piecewise cubic functions using matplotlib.

3. **Interpolation Approximation (Not Fully Implemented in Code):**
   - **Method in Code:** Uses an interpolation method (possibly Gaussian elimination) to approximate a curve passing through given data points.
   - **Code Highlights:**
     - The code includes a Gaussian elimination method, but the actual interpolation method is not fully implemented.

### Criteria for Comparison:

1. **Accuracy:**

   - How well does each method approximate the given curve? This can be assessed by comparing the fitted functions to the actual data points.

2. **Computational Efficiency:**

   - How efficiently does each method compute the approximation? Consider the time complexity and resource usage of each method.

3. **Robustness:**

   - How well does each method handle noisy or irregular data? Evaluate the performance under different types of input.

4. **Ease of Use and Implementation:**
   - Consider the ease of understanding and implementing each method. This includes code readability and simplicity.

### Comparison:

1. **Least Squares vs. Spline:**

   - **Accuracy:** Both methods can provide accurate approximations, but least squares fits a global linear function, while spline captures local behavior.
   - **Computational Efficiency:** Least squares is generally faster, as it involves solving a linear system. Spline requires solving systems for each interval.
   - **Robustness:** Spline may handle irregular data better due to its piecewise nature.
   - **Ease of Use:** Least squares is simpler to implement, especially with the help of libraries like numpy.

2. **Interpolation (Not Fully Implemented) vs. Others:**
   - **Accuracy:** Hard to assess without a fully implemented method, but interpolation methods typically aim for exact fitting.
   - **Computational Efficiency:** Gaussian elimination can be computationally expensive, affecting efficiency.
   - **Robustness:** Depends on the specific interpolation method used.
   - **Ease of Use:** Gaussian elimination can be complex, and the full interpolation method is not implemented.
