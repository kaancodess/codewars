from math import *
def dating_range(age):
    if age <= 14:
        minimum = age - (0.10 * age)
        maximum = age + (0.10 * age)
        return f"{floor(minimum)}-{floor(maximum)}"
        
        
    else:
        minimum = floor((age / 2) + 7)
        maximum = floor((age - 7) * 2)
    
        return f"{minimum}-{maximum}"

# solution for https://www.codewars.com/kata/5803956ddb07c5c74200144e/train/python
