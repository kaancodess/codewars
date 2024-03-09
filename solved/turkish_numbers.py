def get_turkish_number(number):
    new_number = str(number)
    numbers = {
        0: "sıfır",
       1: "bir",
        2: "iki",
        3: "üç",
        4: "dört",
        5: "beş",
        6: "altı",
        7: "yedi",
        8: "sekiz",
        9: "dokuz"
    }
    second_numbers = {
        1: "on",
        2: "yirmi",
        3: "otuz",
        4: "kırk",
        5: "elli",
        6: "altmış",
        7: "yetmiş",
        8: "seksen",
        9: "doksan"
    }

    if len(new_number) == 2:
        first = new_number[0]
        second = new_number[1]
        x = second_numbers[int(first)]
        y = numbers[int(second)]
        if number % 10 == 0:
            return x
        else:
            return (x + " " + y)

    else:
        first = new_number[0]
        x = numbers[int(first)]
        return x

# solution for https://www.codewars.com/kata/5ebd53ea50d0680031190b96/train/python
