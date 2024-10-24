import inflect

p = inflect.engine()
my_list = []
while True:
    try:
        name = input("name: ")
        my_list.append(name)
    except EOFError:
        break

print("Adieu, adieu, to " + p.join(my_list))




