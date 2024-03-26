def contamination(text, char):
    result = ""
    if len(text) == 0 or len(char) == 0:
        return ""
    else:
        for i in range(1,len(text) + 1):
            result += char
            
    return result

# solution for https://codewars.com/kata/596fba44963025c878000039/train/python
