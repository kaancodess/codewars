def invert(lst):
    new_lst = []
    for x in lst:
        if x < 0:
            new_lst.append(abs(x))
        else:
            new_lst.append(-abs(x))
                          
    return new_lst

# solution for https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/python
