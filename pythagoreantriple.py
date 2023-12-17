def pythagorean_triple(a,b,c):
    lst = [a,b,c]
    lst.sort()
    print(lst)
    c = lst[-1] # biggest number in the list
    rest_of_them = lst[:-1]
    a,b = rest_of_them[0] , rest_of_them[1]
    print(f"rest of them a: {a}")
    print(f"rest of them b: {b}")
    print(f"biggest {c}")
    if(a**2 + b**2 == c**2):
        return True
    else:
        return False
print(pythagorean_triple(13,12,5))
