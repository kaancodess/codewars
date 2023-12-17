def abbrev_name(name):
    n = name.split(" ",1)
    first = n[0]
    second = n[1]
    first_letter = first[0].upper()
    second_letter = second[0].upper()
    return f"{first_letter}.{second_letter}"

# solution for https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python
