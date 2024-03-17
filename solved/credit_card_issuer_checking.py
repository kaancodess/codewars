def get_issuer(number):
    x = str(number)
    
    if x.startswith("4") == True:
        if len(x) == 13 or len(x) == 16:
            return "VISA"
        else:
            return "Unknown"
    
    elif x.startswith("6011") == True and len(x) == 16:
        return "Discover"
    
    elif x.startswith(("34","37")) == True and len(x) == 15:
        return "AMEX"
    
    elif x.startswith(("51","52","53","54","55")) == True and len(x) == 16:
        return "Mastercard"
    
    else:
        return "Unknown"

# solution for https://www.codewars.com/kata/5701e43f86306a615c001868/train/python
