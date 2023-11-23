from PIL import Image

class ImageManager: 

  def __init__(self, path: str):
    self.path = path

  def get_2d_pixel_array(self):
    image = Image.open(self.path)
    pixel_arr = list(map(lambda x: list(x), image.getdata()))
    width, height = image.size  
    result = []
    
    for h in range(height):
      temp_list = []
      for w in range(width):
        temp_list.append(pixel_arr[h * width + w])
      result.append(temp_list)
    
    return result
  
  def apply_kernel(self, pixel_arr: list[list[tuple]], kernel):
    width, height = len(pixel_arr[0]), len(pixel_arr) 
    result = []

    for h in range(1, height - 1):
      temp_arr = []
      for w in range(1, width - 1):
        temp_matrix = [
          [ 
          pixel_arr[h - 1][w - 1], 
          pixel_arr[h - 1][w],
          pixel_arr[h - 1][w + 1]
          ],
          [
          pixel_arr[h][w - 1],
          pixel_arr[h][w],
          pixel_arr[h][w + 1]
          ],
          [
          pixel_arr[h + 1][w - 1],
          pixel_arr[h + 1][w],
          pixel_arr[h + 1][w + 1],
          ]
        ]

        sum = [0, 0, 0]
        for i in range(3):
          for j in range(3):
            sum[0] += temp_matrix[i][j][0] * kernel[i][j]
            sum[1] += temp_matrix[i][j][1] * kernel[i][j]
            sum[2] += temp_matrix[i][j][2] * kernel[i][j]

        temp_arr.append(sum)

      result.append(temp_arr)

    return result
  
  def get_horizontal_edges(self, pixel_arr: list[list[tuple]]):
    return self.apply_kernel(pixel_arr, [[0.25, 0.5, 0.25], [0., 0., 0.], [-0.25,-0.5, -0.25]])
      
  def get_vertical_edges(self, pixel_arr):
    return self.apply_kernel(pixel_arr, [[0.25, 0, -0.25], [0.5, 0., -0.5], [0.25, 0, -0.25]])

      
