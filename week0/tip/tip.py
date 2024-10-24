def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d1 = d.removeprefix('$')
    d2 = float(d1)
    return d2


def percent_to_float(p):
    p1 = p.removesuffix('%')
    print(p1)
    p2 = float(p1) * 0.01
    print(p2)
    return p2

main()
