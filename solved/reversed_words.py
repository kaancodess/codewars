def reverse_words(s):
    x = s.split()
    lst = x[::-1]
    y = " ".join(map(str,lst))
    return str(y)

# solution for https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python
