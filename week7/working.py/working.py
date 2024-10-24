import re
import sys

#"9:00 AM to 5:00 PM", -> 09:00 to 17:00


def main():
    print(check(input("Hours: ")))

def seperate(s):
    time =[]
    try:
        if "to" in s:
            time1, time2 = s.split(" to ")
            time.append(time1)
            time.append(time2)
            return time
        else:
            raise ValueError
    except ValueError:
        raise ValueError



def check(s):
    new_time = []
    time = seperate(s)
    for i in range(2):
        if match := re.search(r"^(?P<hr>((0[0-9])|(1[0-2]))|\d)(\:(?P<min>[0-5]\d))?\s(?P<mn>AM|PM)", time[i]):

            hour = convert_hr(match.group("hr"), match.group("mn"))
            min = int(convert_min(match.group("min")))
            new_time.append(f"{hour:02}:{min:02}")
        else:
            raise ValueError
    return f"{new_time[0]} to {new_time[1]}"

def convert_hr(s, m):
    num = int(s)
    if m == "AM" and num > 12:
        return ValueError
    elif m == "AM" and num < 13:
        match num:
            case 12:
                num = 0
            case _:
                num = num
    elif m == "PM":
        match num:
            case 12:
                num = num
            case _:
                num = num + 12

    return num

def convert_min(m):
    if m == None:
        return 0
    else:
        return m


if __name__ == "__main__":
    main()
