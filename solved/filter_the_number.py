def filter_string(st):
    numbers = "1234567890"
    result = ''
    for x in st:
        if x in numbers:
            result += x
    return int(result)

# solution for https://www.codewars.com/kata/55b051fac50a3292a9000025/train/python
