import sys

def main():
    check_file_argv()
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")
    count = 0
    for line in lines:
        if check_line(line) == False:
            count += 1
    print(count)





#check file
def check_file_argv():
    if len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

#check space and #
def check_line(line):
    if line.isspace():
        return True
    if line.lstrip(" ").startswith("#"):
        return True
    return False



#outputs the number of lines of code in that file

if __name__ == "__main__":
    main()









