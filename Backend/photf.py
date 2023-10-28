
from PIL import Image
import io

# Create a list to store the image data as bytes
image_data_list = []

# Open and convert images to JPEG
image1 = Image.open("IMG_2426.jpg")
with io.BytesIO() as output:
    image1.save(output, format="JPEG")
    image_data_list.append(output.getvalue())

image2 = Image.open("0.jpeg")
with io.BytesIO() as output:
    image2.save(output, format="JPEG")
    image_data_list.append(output.getvalue())


