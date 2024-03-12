def difference_of_squares(n):
    p = []
    for x in range(1,n+1):
        p.append(x**2)
        
    r = []
    for x in range(1,n+1):
        r.append(x)
    
    total = sum(r)
    j = total ** 2
    k = sum(p)
    return (j - k)

# solution for https://www.codewars.com/kata/558f9f51e85b46e9fa000025
