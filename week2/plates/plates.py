def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

#lengh
    if len(s) > 6 or len(s) < 2:
        return False
#first two letter cant be numble
    if s[0].isalpha() == False or  s[1].isalpha() == False:
        return False

#first number cant be 0
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                #the number cant not be in the middle
                if s[i:len(s)].isdecimal()== False:
                    return False
                else:
                    break
        i = i + 1


#only accept number and alpha
    if s.isalnum() == False:
        return False
    else:
        return True







 #if s.startswith(" " ,0 , len(s))
main()
