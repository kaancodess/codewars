def narcissistic(value):
    number = str(value)
    length = len(number)
    lst = []
    for x in number:
        lst.append(int(x) ** length)
        
    total = sum(lst)
    if total == value:
        return True
    else:
        return False

# solution for https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python
