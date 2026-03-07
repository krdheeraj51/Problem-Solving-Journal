# Element Size
# Given a window size, the width of an element in viewport width "vw" units, and the height of an element in viewport height "vh" units, determine the size of the element in pixels.

# The given window size and returned element size are strings in the format "width x height", "1200 x 800" for example.

# "vw" units are the percent of window width. "50vw" for example, is 50% of the width of the window.

# "vh" units are the percent of window height. "50vh" for example, is 50% of the height of the window.
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-07

def element_size(window_size, element_width, element_height):
    window_width, window_height = map(int, window_size.split(' x '))
    width_value = int(element_width[:-2])
    height_value = int(element_height[:-2])
    
    if element_width.endswith('vw'):
        element_pixel_width = (width_value / 100) * window_width
    else:
        element_pixel_width = width_value
    
    if element_height.endswith('vh'):
        element_pixel_height = (height_value / 100) * window_height
    else:
        element_pixel_height = height_value
    
    return f"{int(element_pixel_width)} x {int(element_pixel_height)}"