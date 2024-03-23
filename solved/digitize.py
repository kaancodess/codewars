def digitize(n):
    lst = []
    for x in str(n):
        lst.append(x)
    res = [eval(i) for i in lst]
    
    return res

# solution for https://www.codewars.com/kata/5417423f9e2e6c2f040002ae/train/python
