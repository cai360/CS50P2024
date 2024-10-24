def main():
    Input = input("Input: ")
    message = shorten(Input)
    print(message)



def shorten(word):
    message = ""
    for char in word:
        if not char.lower() in ['a', 'e', 'i', 'o', 'u']:
            print(char)
            message += char
    return message


if __name__ == "__main__":
    main()
