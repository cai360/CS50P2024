import validators

def main():
    flag = validators.email(input("email: "))
    if flag:
        print("Valid")
    else:
        print("Invalid")

main()

