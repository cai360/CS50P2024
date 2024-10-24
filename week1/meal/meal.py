
def main():
    time = input("what time is it? ")
    time = convert(time)

    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00 :
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")
    else:
        print("")


def convert(time):
    hour, minutes = time.split(":")
    minutes = float(minutes) / 60
    hour = float(hour)+ minutes
    return hour

if __name__ == "__main__":
    main ()

