def main():
    percentage = convert(input("Fraction: "))
    print(gauge(percentage))


def convert(fraction):
        fracition, numerator = fraction.split('/')
        fracition, numerator = int(fracition), int(numerator)
        percentage = fracition/numerator*100
        return percentage
    



def gauge(percentage):
    if percentage > 100:
        convert(input("Fraction: "))
    elif percentage < 1 or percentage == 1:
        return "E"
    elif percentage > 99 or percentage == 99:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
