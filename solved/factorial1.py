def factorial(n):
        result = 1
        if n >= 0 and n <= 12:
            for i in range(1, n + 1):
                result *= i
            return result
        else:
            raise ValueError

# solution for https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python
