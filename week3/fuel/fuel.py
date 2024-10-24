def main():
    percentage = get()
    print_percentage(percentage)

def get():
    while True:
        try:
            num = input("Fraction: ")
            fracition, numerator = num.split('/')
            fracition, numerator = int(fracition), int(numerator)
            percentage = fracition/numerator*100
            return percentage
        except (ValueError, ZeroDivisionError):
            pass


def print_percentage(per):

    if per > 100:
        get()
    elif per < 1 or per == 1:
        print("E")
    elif per > 99 or per == 99:
        print("F")
    else:
        print(f"{round(per)}%")


main()
