import xlrd
from xlwt import Workbook
from xlutils.copy import copy
import sys
#reads Excel file from location
loc = ("C:\\Users\\JT\\Documents\\Excel\\readFromExcelSample.xlsx")

def read_excel(loc):
    try:
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        row_count = sheet.nrows
        for i in range(row_count):
            print((sheet.row_values(i)))
    except:
        print("Exception occurred")

read_excel(loc)

#Create File Excel
def create_excel(name, fields, data):
    workbook = Workbook()
    sheet1 = workbook.add_sheet('Sheet 1')

    try:
        for index in range(len(fields)):
            sheet1.write(0, index, fields[index])
        c = 0
        r = 1
        for row in data:
            for value in row:
                sheet1.write(r, c, value)
                c = c + 1
            r = r + 1
            c = 0
        workbook.save(name + ".xls")
    except:
        print("Exception occurred")


# columns = ["Name","Salary"]
# data = [["Josh",5000],["Jerry",4000],["Joe",6000]]
# create_excel("createExampleExcel3", columns, data)

def append_to_excel(name, data):
    try:
        book_open = xlrd.open_workbook(name+".xls")
        sheet = book_open.sheet_by_index(0) #start opening sheet at 0 index
        row_count = sheet.nrows
        column_counter = sheet.ncols

        book = copy(book_open)
        sheet1 = book.get_sheet(0)
        c = 0
        for row in data:
            for value in row:
                sheet1.write(row_count, c, value)
                c = c+1
            row_count = row_count + 1
            c = 0
        book.save(name+".xls")
    except:
        print(sys.exc_info)


# new_data=[["Kelly",5000],["jonny",4000],["tom",3000],["nancy",2000]]
# append_to_excel("createExampleExcel",new_data)