from PIL import Image

# Open the JPEG image
image = Image.open("0.jpg")

# Define the cropping coordinates (left, upper, right, lower)
left = 100
upper = 100
right = 400
lower = 400

# Crop the image
cropped_image = image.crop((left, upper, right, lower))

# Save the cropped image to a new file
cropped_image.save("cropped_image.jpg")

# Close the original image
image.close()

