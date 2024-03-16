def factorial(n):
    lst = []
    for x in range(1,n + 1):
        lst.append(x)
        
    result = 1
    for y in lst:
        result *= y
        
    return result

# solution for https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python
