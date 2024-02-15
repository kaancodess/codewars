def search(budget, prices):
    lst = []
    for x in prices:
        if x <= budget:
            lst.append(x)
            
    lst.sort()
    return ','.join(str(e) for e in lst)

# solution for https://www.codewars.com/kata/56069d0c4af7f633910000d3/train/python
