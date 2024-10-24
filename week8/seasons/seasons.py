from datetime import date
import operator
import inflect

p = inflect.engine()

def main():
    birth = check_string()
    today = date.today()
    day = operator.sub(today, birth).days

    print(convert(day))



def check_string():
    birthday = input("Date of Birth: ")
    try:
        year, month, day = birthday.split("-")
        return date(int(year), int(month), int(day))
    except ValueError:
        exit("Invalid date")

def convert(day):
    min = 24 * 60 * day

    return f"{(p.number_to_words(min, andword='')).capitalize()} minutes"

if __name__ == "__main__":
    main()
