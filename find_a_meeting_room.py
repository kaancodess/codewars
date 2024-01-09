def meeting(rooms):
    for o in rooms:
        if o == "O":
            empty_room = o
            return rooms.index(empty_room)
    else:
        return 'None available!'
    
# solution for https://www.codewars.com/kata/57f604a21bd4fe771b00009c/train/python