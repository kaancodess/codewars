def find_needle(haystack):
    for x in haystack:
        if x == "needle":
            y = haystack.index(x)
            
            return f"found the needle at position {y}" 

# solution for https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python 
