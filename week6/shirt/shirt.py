import sys
from os.path import splitext
from PIL import Image
from PIL import ImageOps


# get 2 argv (input, output)

def main():
    check_len()
    #check match
    if check_end(sys.argv[1]) != check_end(sys.argv[2]):

        sys.exit("Input and output have different extensions")

    try:
        before = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    #let the muppet size as same as the shirt
    after = ImageOps.fit(before, size)

    #overlay the shirt with Image.paste
    after.paste(shirt, shirt)

    after.save(sys.argv[2])



def check_len():
    #if the user does not specify exactly two command-line arguments,
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


def check_end(name):
    #check if the file extenstion is jpg, jpeg or png
    #end = name[name.index("."):].lower()
    try:
        end = splitext(name)
        match end[1]:
            case ".jpg" | ".jpeg" | ".png":
                return end[1]
            case _:
                sys.exit("Invalid output")
    except ValueError:
        sys.exit("Invalid output")



if __name__ == "__main__":
    main()
