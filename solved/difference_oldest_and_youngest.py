def difference_in_ages(ages):
    ages.sort()
    min_age = ages[0]
    max_age = ages[-1]
    diff =  max_age - min_age
    return (min_age , max_age , diff)

# solution for https://codewars.com/kata/5720a1cb65a504fdff0003e2/train/python
