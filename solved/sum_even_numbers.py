def sum_even_numbers(seq): 
    lst = []
    for x in seq:
        if x % 2 == 0:
            lst.append(x)
    return sum(lst)

# solution for https://www.codewars.com/kata/586beb5ba44cfc44ed0006c3/train/python