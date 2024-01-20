def digitize(n):
    lst  = []
    x = str(n)
    y = x[::-1]
    for x in y:
        lst.append(x)
    return ([int(x) for x in lst])

# solution for https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
