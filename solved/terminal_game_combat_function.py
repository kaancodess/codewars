def combat(health, damage):
    new_health = health - damage 
    if new_health <= 0:
        return 0
    else:
        return new_health

# solution for https://www.codewars.com/kata/586c1cf4b98de0399300001d/train/python
