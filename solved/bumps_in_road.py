def bumps(road):
    result = ""
    for x in road:
        if x == 'n':
            result += x
    length = len(result)
    if length <= 15:
        return 'Woohoo!'
    else:
        return "Car Dead"
    
# solution for https://www.codewars.com/kata/57ed30dde7728215300005fa/train/python