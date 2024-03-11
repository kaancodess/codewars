def count(x,n):
    lst = []
    total_count = x * n + 1
    y = range(x ,total_count, x)
    for z in y:
        lst.append(z)

    print(lst)
count(50,5)

# solution for https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
