
def main():
    greeting = input("start greeting ")
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.lstrip(" ").lower()
    flag = greeting.find("h")

    if greeting.startswith('hello'):
        return 0
    elif flag == 0:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
