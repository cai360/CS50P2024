def main():
    Input = input("Input: ")
    print(shorten(Input))



def shorten(word):
    List = []
    for char in word:
        if not char.lower() in ['a', 'e', 'i', 'o', 'u']:
            List.append(char)
    return List


if __name__ == "__main__":
    main()








