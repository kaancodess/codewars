def billboard(name, price=30):
    length = len(name)
    counter = 1
    total = 0
    while counter <= length:
        total += price
        counter += 1
        
    return total

# solution for https://www.codewars.com/kata/570e8ec4127ad143660001fd/train/python
