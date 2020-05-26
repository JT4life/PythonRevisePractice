empNum = "s"
parts = ""

while empNum != "sentinal":
    valid = False

    empNum = input("Enter emp number (ddd-dd-dddd): ")
    parts = empNum.split('-')

    if len(parts) == 3:
        if len(parts[0]) == 3 and len(parts[1]) == 2 and len(parts[2]) == 4:
            if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
                valid = True
    print(valid)

# e_no='sentinel'
# # parts=''
# # while  e_no !='':
# #     valid=False
# #     e_no=input('enter employee no(ddd-dd-dddd):')
# #     parts=e_no.split('-')
# #     if len(parts)==3:
# #         if len(parts[0])==3 and len(parts[1])==2 and len(parts[2])==4:
# #             if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
# #                 valid=True
# #     print(valid)