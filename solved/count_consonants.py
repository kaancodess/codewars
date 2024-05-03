def consonant_count(s):
    s = s.replace(" ","")
    if len(s) == 0:
        return 0
    else:
        vowels = "aeiouAEIOU!@£$%^&*#_+1234567890"
        consonants = ""
        for x in s:
            if x not in vowels:
                consonants += x

        return len(consonants)

# solution for https://www.codewars.com/kata/564e7fc20f0b53eb02000106/train/python
