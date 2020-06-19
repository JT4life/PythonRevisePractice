import csv

with open('teachers.csv', 'a') as csvfile:
    fieldnames = ['first_name', 'last_name', 'topic']
    teachwrite = csv.DictWriter(csv, fieldnames=fieldnames)

    teachwrite.writeheader()
    teachwrite.writerow({
        'first_name':'Joshua',
        'last_name':'Thao',
        'topic':'Python'
    })