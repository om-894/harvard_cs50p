
import sys
from PIL import Image, ImageOps
import os   #handles file extensions

if len(sys.argv) == 3:
    extensions = [".jpg", ".jpeg", ".png"]
    extension1 = os.path.splitext(sys.argv[1])  # stores a tuple, sirst is filename and second is extension
    extension2 = os.path.splitext(sys.argv[2])
    if extension1[1] == extension2[1] and extension1[1] in extensions:  # wants extensions to be the same.
        try:
            user_image = Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File doesnt exist")

        shirt = Image.open("shirt.png")
        size = shirt.size   # this returns a tuple, the dimentions are
        # the same size as the shirt.png
        # (width, height)
        user_image = ImageOps.fit(user_image, size)
        user_image.paste(shirt, shirt)
        user_image.save(sys.argv[2])
    elif extension1[1] != extension2[1]:
        sys.exit("imput and output have different extensions")
    else:
        sys.exit("wrong extension")
elif len(sys.argv) < 3:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command line arguments")
