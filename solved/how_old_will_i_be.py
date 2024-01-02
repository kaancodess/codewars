def calculate_age(year_of_birth, current_year):
    
    if current_year == year_of_birth:
        return f"You were born this very year!"
    
    elif current_year > year_of_birth:
        age = current_year - year_of_birth
        if age == 1:
            return f"You are {age} year old."
        else:
            return f"You are {age} years old."
    
    else:
        birth = year_of_birth - current_year
        if birth == 1:
            return f"You will be born in {birth} year."
        else:
            return f"You will be born in {birth} years."

# solution for https://www.codewars.com/kata/5761a717780f8950ce001473/train/python
