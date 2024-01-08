#Function for interlacing with black lines
def interlace(int_image):
    width = len(int_image)
    height = len(int_image[0])

    for x in range(0, width, 2):
        for y in range(height):
            pixel = int_image[x][y]

            pixel[0] = 0
            pixel[1] = 0
            pixel[2] = 0

    return int_image


#Function for inverting colour
def invert(inv_image):
    width = len(inv_image)
    height = len(inv_image[0])

    for x in range(width):
        for y in range(height):
            pixel = inv_image[x][y]

            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]

    return inv_image


#Function for grayscaling
def grayscale(gs_image):

    width = len(gs_image)
    height = len(gs_image[0])

    for x in range(width):
        for y in range(height):
            pixel = gs_image[x][y]

            average = (pixel[0] + pixel[1] + pixel[2]) / 3

            pixel[0] = average
            pixel[1] = average
            pixel[2] = average

    return gs_image


#Function for adjusting saturation
def saturation(sat_image):

    width = len(sat_image)
    height = len(sat_image[0])

    for x in range(width):
        for y in range(height):
            pixel = sat_image[x][y]

            gs = (pixel[0] + pixel[1] + pixel[2]) / 3

            for i in range(3):
              
                if (gs + scale * (pixel[i] - gs)) > 255:
                    pixel[i] = 255
                elif (gs + scale * (pixel[i] - gs)) < 0:
                    pixel[i] = 0
                else:
                    pixel[i] = gs + scale * (pixel[i] - gs)

    return sat_image
