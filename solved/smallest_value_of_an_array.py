def find_smallest(numbers, to_return):
    if to_return == "value":
        return min(numbers)
    else:
        min_num = min(numbers)
        return numbers.index(min_num)
    
# solution for https://www.codewars.com/kata/544a54fd18b8e06d240005c0/train/python