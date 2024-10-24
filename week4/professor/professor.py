
import random





def main():
    level = get_level()
    times = 0
    scores = 0
    errortime = 0
    while times < 10:
        #asking question:
        print(times)
        x = generate_integer(level)
        y = generate_integer(level)
        answer = int(input(f"{x} + {y} = " ))

        #compareing answer:
        #anwer is right
        if answer == (x + y):
            scores +=1
            times +=1
        #anwer is wrong
        else:
            print("EEE")
            errortime += 1
            while errortime < 3:
                answer = int(input(f"{x} + {y} = " ))
                if answer == (x + y):
                    times += 1
                    break
                else:
                    print("EEE")
                    errortime += 1
                    if errortime == 3:
                        print(f"{x} + {y} = {x + y}")
                        times += 1
                        break
                    else:
                        continue
    print(f"score = {scores}")



def get_level():
    while True:
        try:
            level = int(input("level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
           pass

def generate_integer(level):
    match level:
        case 1:
            num = random.randint(0, 10**level-1 )
        case 2:
            num = random.randint(10**1, 10**level-1 )
        case 3:
            num = random.randint(10**2, 10**level-1 )
        case _:
            raise ValueError
    return num




if __name__ == "__main__":
    main()
