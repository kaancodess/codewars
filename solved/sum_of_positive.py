def positive_sum(arr):
    lst = []
    for x in arr:
        if x > 0:
            lst.append(x)
    return sum(lst)

# solution for https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
