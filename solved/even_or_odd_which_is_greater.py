def even_or_odd(s): # odd tek
    even = []
    odd = []
    x = [int(i) for i in s]
    for y in x:
        if y % 2 == 0:
            even.append(y)
        else:
            odd.append(y)
    total_even = sum(even)
    total_odd = sum(odd)
        
    if total_even > total_odd:
        return "Even is greater than Odd"
        
    elif total_odd > total_even:
        return "Odd is greater than Even"
        
    else:
        return "Even and Odd are the same"

# solution for https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/python
