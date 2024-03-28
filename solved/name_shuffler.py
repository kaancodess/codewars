def name_shuffler(str_):
    lst = str_.split()
    y = lst[::-1]
    x = " ".join(map(str,y))
    return str(x)

# solution for https://www.codewars.com/kata/559ac78160f0be07c200005a/train/python
