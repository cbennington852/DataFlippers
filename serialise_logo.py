import base64

def image_to_base64(filename):
    with open(filename, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string

# Replace 'your_image.png' with your file path
base64_data = image_to_base64('resources/DataFlippers.png')
print(base64_data)
