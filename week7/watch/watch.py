import re
import sys


def main():
    print(parse(input("HTML: ")))



def parse(s):
    if inframe := re.search(r"^<iframe.+</iframe>$", s):
        if match := re.search(r"https?://(?:www\.)?youtube\.com/embed/(\w+)", s):
            url = "https://youtu.be/" + match.group(1)
            return url
        else:
            return match

    else:
        return inframe



if __name__ == "__main__":
    main()
