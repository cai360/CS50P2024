import sys
import csv

def main():
    file_exit = check_argvs()
    #check two comman-line arguments
    if (file_exit):
        try:
            #read the file & create a file
            with open(sys.argv[1], "r") as before_file, open(sys.argv[2], "w") as after_file:
                reader = csv.DictReader(before_file)
                writer = csv.DictWriter(after_file, fieldnames = ["first", "last", "house"])

                #writer titles into afterfile
                writer.writeheader()
                for row in reader:
                    #seperate the first name and last name
                    last, first = row["name"].split(",")
                    writer.writerow({"first": first.lstrip(), "last": last.lstrip(), "house":row["house"]})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


def check_argvs():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    return True

if __name__ == "__main__":
    main()

