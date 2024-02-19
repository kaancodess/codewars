def distinct(seq):
    lst = []
    for x in seq:
        if x not in lst:
            lst.append(x)
            
    return lst

# solution for https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python
