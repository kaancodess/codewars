def two_highest(arg1):
    res = []
    [res.append(x) for x in arg1 if x not in res]
    res.sort()
    
    new_lst = res[-2:]
    new_lst.reverse()
    return new_lst

# solution for https://www.codewars.com/kata/57ab3c09bb994429df000a4a/train/python
