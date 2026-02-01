#                           Scaled Image
# Given a string representing the width and height of an image, and a number to scale the image, return the scaled width and height.

# The input string is in the format "WxH". For example, "800x600".
# The scale is a number to multiply the width and height by.
# Return the scaled dimensions in the same "WxH" format.

def scaled_image(dimensions, scale):
    width, height = map(int, dimensions.split('x'))
    scaled_width = int(width * scale)
    scaled_height = int(height * scale)
    return f"{scaled_width}x{scaled_height}"