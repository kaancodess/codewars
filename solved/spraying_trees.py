def task(w, n, c):
    if w == "Monday":
        name = "James"
    if w == "Tuesday":
        name = "John"
    if w == "Wednesday":
        name = "Robert"
    if w == "Thursday":
        name = "Michael"
    if w == "Friday":
        name = "William"
        
    return f'It is {w} today, {name}, you have to work, you must spray {n} trees and you need {n * c} dollars to buy liquid'

# solution for https://www.codewars.com/kata/5981a139f5471fd1b2000071/train/python
