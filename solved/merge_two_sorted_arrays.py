def merge_arrays(arr1, arr2):
    for x in arr2:
        arr1.append(x)
    lst = []
    [lst.append(y) for y in arr1 if y not in lst]
    return sorted(lst)

# solution for https://www.codewars.com/kata/5899642f6e1b25935d000161
