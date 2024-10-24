expression = input("inter an expression: ")
x, y, z = expression.split(" ")
x, z = int(x), int(z)

match y:
    case "+":
        anwer = x + z
    case "-":
        anwer = x - z
    case "*":
        anwer = x * z
    case "/":
        anwer = round(x / z, 1)



print(f"{anwer:.1f}")
