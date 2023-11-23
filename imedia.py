from PIL import Image

def convert_to_grayscale(input_image_path, output_image_path):
    # Open the image file
    image = Image.open(input_image_path)
    
    # Convert the image to grayscale
    grayscale_image = image.convert("L")
    
    # Save the grayscale image
    grayscale_image.save(output_image_path)

    return grayscale_image

# Example usage
input_path = "./photo.jpg"
output_path = "./yle.jpg"

res = convert_to_grayscale(input_path, output_path)
res.show()
