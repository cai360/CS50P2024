def main():

   Ans = convert()
   print (Ans)


def convert():
    I = input("enter something")
    I1 = I.replace(":)", "🙂")
    I2 = I1.replace(":(", "🙁")
    return I2



main()
