def descending_order(num):
    res = list(map(int, str(num)))
    res.sort(reverse = True)
    result = ''
    for x in res:
        result += str(x)
    return int(result)

# solution for https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
