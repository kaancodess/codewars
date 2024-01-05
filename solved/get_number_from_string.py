def get_number_from_string(st):
    numbers = "1234567890"
    result = ''
    for x in st:
        if x in numbers:
            result += x
    return int(result)

# solution for https://www.codewars.com/kata/57a37f3cbb99449513000cd8
