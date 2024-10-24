list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


Flag = True
while Flag:
    Input = input("Date: ").lstrip().rstrip()
    try:
        m, d, y = Input.split("/")
        if int(m) <= 12 and int(m)>=1 and int(d) <= 31 and int(d)>= 1:
            break
    except:
        if "," in Input:
            try:
                m, d, y = Input.split(" ")
                d = d.replace(",", "")
                if m in list:
                    m = list.index(m)+1
                if int(m) >= 1 and int(m) <=12 and int(d) >=1 and int(d) <= 31:
                    break
            except:
                print()
                pass


print(f"{y}-{int(m):02}-{int(d):02}")







