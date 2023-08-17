print("Hello World!!!!")
import argparse
import openpyxl as px


parser = argparse.ArgumentParser()


parser.add_argument('--output_file', type=str, default='output.txt')
parser.add_argument('--out_exl', type=str, default='output.xlsx')

args = parser.parse_args()

output_file = args.output_file
out_exl = args.out_exl

with open(output_file, "r") as file:
     lines = [line.rstrip().split(" ") for line in file.readlines()]
     file.close()

wb = px.Workbook()
ws = wb.active

for i in range(len(lines[0])):
    for j in range(len(lines)):
        ws.cell(row = j + 2, column = i + 2).value = str(lines[j][i])

wb.save(out_exl)
