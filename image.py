##############################################################
######### Utility to convert image to another size ###########
##############################################################
#
# This module provides tool to make PNG smaller.
#
# Requirements:
#   - Python 3.8 or newer
#
# Author: Pavel Vraj
# Version: 0.2
#
##############################################################

import sys
import base64
from io import BytesIO
from PIL import Image

def resize_image(input_png, max_width, max_height):
    """
    Convert PNG to max size
    Parameters:
        input_png (string): source PNG in base64 format
        max_width (int): maximum width of the resized image
        max_height (int): maximum height of the resized image
    Returns:
        status (string): ok or error
        message (string): error or status message
        output_png (string): base64 content of output PNG
    """

    status = ""
    message = ""
    resized_base64 = ""

    try:
        # Decode Base64 image
        image_data = base64.b64decode(input_png)
        
        # Open the image from bytes
        image = Image.open(BytesIO(image_data))
        
        # Calculate the new size preserving the aspect ratio
        image.thumbnail((max_width, max_height))
        
        # Save the resized image to a bytes buffer
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        
        # Get the base64 content of the resized image
        resized_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        
        status = "ok"
        message = f"Converted to size of {max_width} x {max_height}"

    except:
        status = "error"
        message = str(sys.exc_info()[1])

    response_text = {
        "status": status,
        "message": message,
        "output_png": resized_base64
    }
    
    return response_text
