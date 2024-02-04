def calculator(x,y,op):
    
    operators = ["+","-","/","*"]
    
    if type(x) == str or type(y) == str:
        return "unknown value"
    
    if op in operators:
        if op == "+":
            return x + y

        elif op == "-":
            return x - y

        elif op == "/":
            return x / y

        elif op == "*":
            return x * y
        
    else:
        return "unknown value"

# solution for https://www.codewars.com/kata/5810085c533d69f4980001cf/train/python
