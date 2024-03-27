def zipvalidate(postcode):
    valid = "1234567890"
    if len(postcode) == 6:
        if postcode.startswith(("0","5","7","8","9")):
            return False
        else:
            if postcode.isnumeric() == False:
                return False
            else:
                return True
    else:
        return False

# solution for https://www.codewars.com/kata/552e45cc30b0dbd01100001a/train/python
