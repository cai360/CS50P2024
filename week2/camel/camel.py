inputName = input("camelCase: ")

print ("snake_case: ", end= "")
for char in inputName:
    if char.isupper():
        print("_" + char.lower() , end = "")
    else:
        print(char, end = "")



