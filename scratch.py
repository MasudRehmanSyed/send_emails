# import xlsxwriter as xl
# import csv
#
# x = [f'85-{x}' for x in range(80, 0, -10)]
#
# y = [f'{x}-85' for x in range(80, 0, -10)]
#
# final85 = []
# for n, l in enumerate(x):
#     final85.append(l)
#     final85.append(y[n])
#
#
#
#
# workbook = xl.Workbook(f'C:\users\Rawni\Downloads\Transition.xlsx')
#
# worksheet= workbook.add_worksheet()
#
# row, col = 0, 0
#
# for x in final85:
#     worksheet.write_row(row, col, x)
#     row +=1
#
# workbook.close()
cvs_data = "birthdays.csv"
import datetime as dt, csv, pandas as pd

now = dt.datetime.now()
year = now.year
month = now.month
hour = now.hour

day_of_week = now.weekday()
date_of_birth = dt.datetime(year, month, day_of_week, hour)
print(date_of_birth)

# with open(cvs_data, 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',', lineterminator='\n\n')
#     # gets field names
#     fields = next(csv_reader)
#
# print(fields)
from pathlib import Path
letter = Path('./letter_templates/letter_1.txt').read_text()
letter = letter.replace('[NAME]', 'Rawni')
print(letter)

