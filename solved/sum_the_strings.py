def sum_str(a, b):
    if len(a) == 0 and len(b) == 0:
        return "0"
    
    elif len(a) == 0:
        return b
    
    elif len(b) == 0:
        return a
    
    else:
        total = int(a) + int(b)
        return str(total)

# solution for https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python
