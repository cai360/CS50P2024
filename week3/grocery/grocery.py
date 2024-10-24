
List = {}

def main():
    List = get_item()
    sort_item(List)


def get_item():
    while True:
        try:
            Item = input().upper()
            if not Item in List:
                List.update({Item: 1})
            else:
                List.update({Item: List[Item]+1})
        except EOFError:
            print()
            break
    return List

def sort_item(list):
    for i in sorted(list):
        print(list[i], i)

main()
