import datetime

ask = input("Enter date for deadline (mm/dd/yyyy)")
date = datetime.datetime.strptime(ask, "%M/%d/%Y").date()
today = input("Enter today's date (mm/dd/yyyy)")
formatCurrent = datetime.datetime.strptime(today, '%M/%d/%Y').date()

dueDate = date - formatCurrent
print(dueDate)
