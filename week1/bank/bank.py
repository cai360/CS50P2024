

def main():
    greeting = input("start greeting ")
    compare(formatted (greeting))


def formatted(phrase):
    greeting = phrase.lstrip(" ").lower()
    return greeting

def compare(phrase):
    flag = phrase.find("h")

    if phrase.startswith('hello'):
        print("$0")
    elif flag == 0:
        print("$20")
    else:
        print("$100")


main()
