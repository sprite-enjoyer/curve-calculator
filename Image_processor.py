from PIL import Image

class ImageManager: 

  def __init__(self, path: str):
    self.path = path

  def convert_to_grayscale(self, image: Image.Image):
    return list(map(lambda x : int(0.299 * x[0] + 0.587 * x[1] + 0.114 * x[2]), image.getdata()))

  def convert_pixel_arr_to_2d(self, pixel_arr: list, height: int, width:int):
    result = []
    for h in range(height):
      temp_list = []
      for w in range(width):
        temp_list.append(pixel_arr[h * width + w])
      result.append(temp_list)
    return result
    
  def get_2d_pixel_array(self):
    image = Image.open(self.path)
    pixel_arr = self.convert_to_grayscale(image)
    width, height = image.size 
    result = self.convert_pixel_arr_to_2d(pixel_arr, height, width)
    return result

  def get_curve_points(self, pixel_arr_2d):
    backgroundColor = pixel_arr_2d[0][0]
    coordinates_arr = [[], []]

    for height in range(len(pixel_arr_2d)):
      for width in range(len(pixel_arr_2d[0])):
        if pixel_arr_2d[height][width] is not backgroundColor:
          coordinates_arr[0].append(width)
          coordinates_arr[1].append(height)
    return coordinates_arr
