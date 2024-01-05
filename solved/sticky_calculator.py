def sticky_calc(operation, val1, val2):
    
    str_number = str(round(val1))  + str(round(val2))
    
    if operation == "+":
        return int(str_number) + round(val2)
    
    elif operation == "-":
        return int(str_number) - round(val2)
    
    elif operation == "*":
        return int(str_number) * round(val2)
    
    elif operation == "/":
        return round(int(str_number) / val2)

# solution for https://www.codewars.com/kata/5900750cb7c6172207000054/train/python
