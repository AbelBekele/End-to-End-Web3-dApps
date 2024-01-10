import cv2
import numpy as np
import random

def write_name(name: str) -> str:
    # Open the Base certificate image
    img = cv2.imread("certificate/responses/selected.png")  # Replace with your base certificate image name
    # Window name in which image is displayed 
    window_name = 'Image'
    # Save all the information we are going to use
    location = (140, 800)  # Replace with the coordinates you noted. (X, Y)
    text_color = (18, 48, 134)  # Replace with the color you want the text to be
    font = cv2.FONT_HERSHEY_SIMPLEX  # Replace with a font of your choosing
    font_scale = 3  # Change the number to change font size
    font_thickness = 2
    # Insert the text to the location, with the person's name as text and fill the text in the color of our choice (and use the selected font)
    img = cv2.putText(img, name, location, font, font_scale, text_color, font_thickness, cv2.LINE_AA, False)
    img = cv2.putText(img, name, location, font, font_scale, text_color, font_thickness, cv2.LINE_AA, True)
    # Create a unique name for the file. Feel free to edit the format, this is an example
    file_name = "generated/" + name + str(random.randint(0, 255)) + ".png"
    # Save the image
    cv2.imwrite(file_name, img)
    # Display the image 
    cv2.imshow(window_name, img)
    # Return the name we generated
    return file_name