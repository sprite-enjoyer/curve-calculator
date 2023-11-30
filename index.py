from Image_processor import ImageProcessor
from interpolation_classes import least_squares_approximation, spline_approximation, interpolation_approximation
import numpy as np

image_processor = ImageProcessor("./files/curve.png")
pixel_arr = image_processor.get_2d_pixel_array()
curve_points = image_processor.get_curve_points(pixel_arr)

approximation_strategy1 = least_squares_approximation.LeastSquaresApproximation()
approximation_strategy2 = spline_approximation.SplineApproximation()
approximation_strategy3 = interpolation_approximation.InterpolationStrategy()

squares_result = approximation_strategy1.approximate(curve_points[0], curve_points[1])
spline_result = approximation_strategy2.approximate(curve_points[0], curve_points[1])

# too slow; couldn't test;
# interpolation_result = approximation_strategy3.approximate(curve_points[0], curve_points[1])


# approximation_strategy1.draw(squares_result[0], squares_result[1])

# a bit slow
# approximation_strategy2.draw(spline_result)


# too slow to test or implement
# approximation_strategy3.draw()