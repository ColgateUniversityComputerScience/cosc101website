# ----------------------------------------------------------
# --------              HW 6: Images               ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name:
# Time spent:
# Collaborators and sources:
#   (List any collaborators or sources here.)
# ----------------------------------------------------------


import cImage as image
import os.path


# -------------------------------
# EXAMPLE FUNCTION: RED FILTER
# -------------------------------
# Here is an example of a transformation function. Note that this
# function is called from the main() function below.

def red_filter(img):
    """ (Image object) -> Image object
    Returns a copy of img where the blue and green have been filtered
    out and only red remains.
    """
    red_only_img = img.copy() # create copy to manipulate
    w = img.getWidth()
    h = img.getHeight()
    for x in range(w): # iterate through all (x, y) pixel pairs
        for y in range(h):
            pixel = img.getPixel(x, y)
            red = pixel.getRed() # get original red value
            redPixel = image.Pixel(red, 0, 0)
            red_only_img.setPixel(x, y, redPixel) # replace pixel
    return red_only_img # return filtered image


#--------------------------------
# GRADED FUNCTIONS
#--------------------------------
# Fill in docstrings and code for all of the functions required by the
# homework assignment. For your convenience, each of the function
# definitions have been started for you. However, note that all of the
# functions are currently defined to return None. You will need to change
# that for all of these functions.


def flip_horizontal(img):
    ''' (ImageObject) -> ImageObject

    '''
    return None


def flip_vertical(img):
    ''' (ImageObject) -> ImageObject

    '''
    return None


def rotate_clockwise(img):
    ''' (ImageObject) -> ImageObject

    '''
    return None


def to_negative(img):
    ''' (ImageObject) -> ImageObject

    '''
    return None
    

def to_blacknwhite(img, intensity):
    ''' (ImageObject) -> ImageObject

    '''
    return None


def scale_up(img):
    ''' (ImageObject) -> ImageObject

    '''
    return None


def scale_down(img):
    ''' (ImageObject) -> ImageObject

    '''
    return None


def leave_color(img):
    ''' (Image object) -> Image object

    '''
    return None


## Challenge problem (optional)

def challenge(img):
    ''' (ImageObject) -> ImageObject

    '''
    return None


# -------------------------------
# HELPER FUNCTIONS
# -------------------------------
# These functions are provided to help you test your code. They are not graded.

def open_image(fname=None):
    ''' () -> ImageObject or None
    Return an Image object from file name, either given as a parameter or input
    by the user. Return None if the file does not exist or is not a .gif file.
    '''
    # if no filename given, get filename from user
    if not fname:
        fname = input("Enter an image filename: ")

    # check if .gif file
    if not fname[-4:] == '.gif':
        print("Error: "+fname+" is not a .gif file")
        return None

    # check if file does not exists
    if not os.path.exists(fname):
        print("Error: There is no " + fname + " file")
        return None

    # return image from file
    return image.Image(fname)


def display_image(img):
    ''' (ImageObject) -> NoneType
    Display an image. Note: You must click to close the image before the program
    can continue running.
    '''
    w = img.getWidth()
    h = img.getHeight()
    win = image.ImageWin("Image", w, h)
    img.draw(win)
    win.exitonclick()
    return None


def save_image(img, fname):
    ''' (ImageObject, str) -> NoneType
    Save an image to the file fname.
    '''
    img.save(fname)
    return None


#--------------------------------
# BEGIN MAIN FUNCTION
#--------------------------------
# The code below calls all of the transformation functions
# you wrote on the provided .gif files and displays the results.
# You can also test your code using another .gif image of your choice 
# by modifying this function.

def main():
    """ () -> NoneType
    Main Program that load image(s) from file(s) and performs
    transformations to those images as required for this homework. 
    """
    for imgname in ['colgate','rose','grid']:
        original_img = image.Image(f'img/{imgname}.gif')
        red_img = red_filter(original_img)
        display_image(red_img)

        horiz_img = flip_horizontal(original_img)
        if horiz_img is not None:
            display_image(horiz_img)
        else:
            print("incomplete: flip_horizontal is not implemented or still returns None")

        vertical_img = flip_vertical(original_img)
        if vertical_img is not None:
            display_image(vertical_img)
        else:
            print("incomplete: flip_vertical is not implemented or still returns None")

        rot_image = rotate_clockwise(original_img)
        if rot_image is not None:
            display_image(rot_image)
        else:
            print("incomplete: rotate_clockwise is not implemented or still returns None")

        neg_image = to_negative(original_img)
        if neg_image is not None:
            display_image(neg_image)
        else:
            print("incomplete: to_negative is not implemented or still returns None")

        bnw_img = to_blacknwhite(original_img, intensity = 100)
        if bnw_img is not None:
            display_image(bnw_img)
        else:
            print("incomplete: to_blacknwhite is not implemented or still returns None")
        up_img = scale_up(original_img)
        if up_img is not None:
            display_image(up_img)
        else:
            print("incomplete: scale_up is not implemented or still returns None")

        down_img = scale_down(original_img)
        if down_img is not None:
            display_image(down_img)
        else:
            print("incomplete: scale_down is not implemented or still returns None")


    for imgname in ['colgate','rose','grid']:
        original_img = image.Image(f'img/{imgname}.gif')
        display_image(original_img)

        leave_color_img = leave_color(original_img)
        if leave_color_img is not None:
            display_image(leave_color_img)
        else:
            print("incomplete: leave_color is not implemented or still returns None")



# start the main function, but only if this file is being run "directly"
if __name__ == '__main__':
    main()
