
from PIL import Image
import io

drawings = Image.open("0.jpeg")
with io.BytesIO() as output:
    drawings.save(output, format="JPEG")
    croppedimage1 = drawings.crop((170,50,400,260))
    croppedimage1.save("cropped_image1.jpg")
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

    croppedimage5 = drawings.crop((420,50,650,260))
    croppedimage5.save("cropped_image5.jpg")
    croppedimage5.show()
    croppedimage6 = drawings.crop((420,300,650,520))
    croppedimage6.save("cropped_image6.jpg")
    croppedimage6.show()
    croppedimage7 = drawings.crop((420, 550, 650, 780))
    croppedimage7.save("cropped_image7.jpg")
    croppedimage7.show()
    croppedimage8 = drawings.crop((420, 800, 650, 1030))
    croppedimage8.save("cropped_image8.jpg")
    croppedimage8.show()

# Create a list to store the image data as bytes
image_data_list = []

# Open and convert images to JPEG
image1 = Image.open("IMG_2426.jpg")
with io.BytesIO() as output:
    image1.save(output, format="JPEG")
    image_data_list.append(output.getvalue())



