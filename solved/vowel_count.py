def get_count(sentence):
    result = 0
    vowels = "aeiou"
    for x in sentence:
        if x in vowels:
            result += 1
    return result

# solution for https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
