def square_num(numbers):
	lst = []
	
	if len(numbers) == 0:
		return 0

	for x in numbers:
		all_numbers = x**2
		lst.append(all_numbers)

	total_sum = sum(lst)
	return total_sum

# solution for https://www.codewars.com/kata/515e271a311df0350d00000f/solutions/python
