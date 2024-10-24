import re
import sys


def main():
    print(validate(sys.argv[1]))

#0~255#.#.#.#.
def validate(ip):
    #three digit"[0-2][0-5]{2}" | two digit-> "\d\d" | one digit->  "\d"

    if re.search(r"^((((2[0-5]{2}|2[0-4]\d)|1\d\d)|\d\d|\d)\.){3}(((2[0-5]{2}|1\d\d)|\d\d|\d))$", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
