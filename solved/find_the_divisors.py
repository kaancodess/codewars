def divisors(integer):
    lst = []
    for x in range(2,integer):
        if integer % x == 0:
            lst.append(x)
    if len(lst) <= 0:
        return f"{integer} is prime"
    else:
        return lst

# solution for https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/python
