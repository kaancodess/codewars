def pofi(n):
    remainder = n % 4
    if remainder == 0:
        return "1"
    elif remainder == 1:
        return "i"
    elif remainder == 2:
        return "-1"
    elif remainder == 3:
        return "-i"
    elif remainder == 4:
        return "1"

# solution for https://www.codewars.com/kata/5a97387e5ee396e70a00016d/train/python
