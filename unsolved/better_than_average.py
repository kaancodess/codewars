def better_than_average(class_points,your_points):
    total_points = sum(class_points)
    length = len(class_points)
    average = total_points / length
    if your_points > average:
        return True
    else:
        return False

# solution for: https://www.codewars.com/kata/5601409514fc93442500010b/train/python
