def get_sum(a,b):
    lst = []
    if a < b:
        for x in range(a,b + 1):
            lst.append(x)
        return sum(lst)
    
    else:
        a,b = b,a
        for x in range(a,b + 1):
            lst.append(x)
        return sum(lst)

# solution for https://www.codewars.com/kata/55f2b110f61eb01779000053
