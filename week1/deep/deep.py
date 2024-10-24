

def main():
    Answer = transfer(input("what is the answer? "))
    compare(Answer)


def transfer(ToBeTheSame):
    Answer = ToBeTheSame.strip(" ").lower()
    return Answer

def compare(Answer):
    if Answer == "42" or Answer ==  "forty-two" or Answer == "forty two":
        print("yes")
    else :
        print("no")


main()
