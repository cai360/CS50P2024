from calendar import Calendar
import csv
from tabulate import tabulate

def main():

    c = Calendar()
    empty_calendar = c.monthdayscalendar(2024, 12)
    csv_file_path = 'calendar.csv'
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(empty_calendar)

    print(f"CSV file '{csv_file_path}' created successfully.&quot")




if __name__ == "__main__":
    main()
