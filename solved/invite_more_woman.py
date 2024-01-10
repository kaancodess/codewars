def invite_more_women(arr):
    total = sum(arr)
    if total == 0:
        return False
    elif total < 0:
        return False
    else:
        return True
    
# solution for https://www.codewars.com/kata/58acfe4ae0201e1708000075/train/python