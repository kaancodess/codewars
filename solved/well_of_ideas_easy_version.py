def well(x):
    lst = []
    for y in x:
        if y == "good":
            lst.append(y)
    
    length = len(lst)
    if length <= 0:
        return "Fail!"
    elif length <= 2:
        return "Publish!"
    else:
        return "I smell a series!"

# solution for https://www.codewars.com/kata/57f222ce69e09c3630000212/train/python
