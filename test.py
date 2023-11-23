from matplotlib.pyplot import gray
import numpy as np
from Image_processor import ImageManager
from PIL import Image

image_manager = ImageManager("./photo.jpg")
start_arr = image_manager.get_2d_pixel_array()
result_arr = image_manager.get_vertical_edges(start_arr)

img1 = Image.fromarray(np.array(start_arr, dtype=np.uint8))
img2 = Image.fromarray(np.array(result_arr, dtype=np.uint8))

img2.show()