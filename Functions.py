from PIL import Image

def text_to_binary(text):
    binary_string = ""
    for char in text:
        binary_char = format(ord(char), '08b')
        binary_string += binary_char
    return binary_string

def binary_to_text(binary_string):
    text = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        text += chr(int(byte, 2))
    return text

def encrypt_image(image_path, binary_message):
    image = Image.open(image_path)
    width, height = image.size
    binary_index = 0

    for y in range(height):
        for x in range(width):
            pixel = list(image.getpixel((x, y)))
            for i in range(3):
                if binary_index < len(binary_message):
                    pixel[i] = pixel[i] & ~1 | int(binary_message[binary_index])
                    binary_index += 1
            image.putpixel((x, y), tuple(pixel))

    encrypted_image_path = "encrypted_image.png"
    image.save(encrypted_image_path)
    return encrypted_image_path