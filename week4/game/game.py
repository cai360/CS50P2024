import random




while True:
    try:
        level = int(input("lever: "))
        if level > 0:
            break
        else:
            continue
    except:
        pass


num = random.randint(1,level)

while True:
    try:
        guess = int(input("guess"))
        if num > 0:
            if guess > num:
                print("Too large!")
            elif guess < num:
                print("Too small!")
            else:
                print("Just right!")
                break
        else:
            continue
    except:
        pass



