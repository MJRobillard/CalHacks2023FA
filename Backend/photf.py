
from PIL import Image
import io

drawings = Image.open("0.jpeg")
with io.BytesIO() as output:
    drawings.save(output, format="JPEG")
    croppedimage1 = drawings.crop((170,50,400,260))
    croppedimage1.save("cropped_image.jpg")
    croppedimage1.show()
    croppedimage2 = drawings.crop((170, 300, 400, 530))
    croppedimage2.save("cropped_image2.jpg")
    croppedimage2.show()
    croppedimage3 = drawings.crop((170, 550, 400, 780))
    croppedimage3.save("cropped_image3.jpg")
    croppedimage3.show()
    croppedimage4 = drawings.crop((170, 800, 400, 1030))
    croppedimage4.save("cropped_image4.jpg")
    croppedimage4.show()

    croppedimage10 = drawings.crop((420,50,650,260))
    croppedimage10.save("cropped_image10.jpg")
    croppedimage10.show()
    croppedimage20 = drawings.crop((420,300,650,520))
    croppedimage20.save("cropped_image20.jpg")
    croppedimage20.show()
    croppedimage30 = drawings.crop((420, 550, 650, 780))
    croppedimage30.save("cropped_image30.jpg")
    croppedimage30.show()
    croppedimage40 = drawings.crop((420, 800, 650, 1030))
    croppedimage40.save("cropped_image40.jpg")
    croppedimage40.show()

# Create a list to store the image data as bytes
image_data_list = []

# Open and convert images to JPEG
image1 = Image.open("IMG_2426.jpg")
with io.BytesIO() as output:
    image1.save(output, format="JPEG")
    image_data_list.append(output.getvalue())



