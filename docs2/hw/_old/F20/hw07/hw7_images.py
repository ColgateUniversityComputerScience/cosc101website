# ----------------------------------------------------------
# --------              HW 7: Images               ---------
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
# this for (at least) some of these functions.

def negative(img):
    ''' (ImageObject) -> ImageObject

    '''
    return None


def flip_horizontal(img):
    ''' (ImageObject) -> ImageObject

    '''
    return None


def merge(img1, img2, img3, img4):
    ''' (ImageObject, ImageObject, ImageObject, ImageObject) -> ImageObject

    '''
    return None


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
# Replace the code below to call all of the transformation functions
# you wrote display and save the results. Your main should call every
# graded function you wrote above. You can test your code using the
# provided grid.gif file or another .gif image of your choosing, as
# long as the image file is in the same directory as this .py file.

def main():
    """ () -> NoneType
    Main Program that load image(s) from file(s) and performs
    transformations to those images as required for HW 04. The images
    are then displayed.
    """
    original_img = image.Image('img/colgate.gif')
    red_img = red_filter(original_img)
    display_image(red_img)
    save_image(red_img, 'img/colgate_red.gif')


# start the main function, but only if this file is being run "directly"
if __name__ == '__main__':
    main()
