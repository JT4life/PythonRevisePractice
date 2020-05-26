rooms = {1:'Foyer', 2:'Conference Room'}
room = input("Enter room number: ")
if not room in rooms:
    print("Room not exist")
else:
    print("The room name is " + rooms[room])