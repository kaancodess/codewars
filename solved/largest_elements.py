def largest(n,xs):
	xs.sort()
	reverse_lst = xs[::-1] # reverse of a sorted list
	last_lst = reverse_lst[:n]
	return last_lst[::-1]

# solution for https://www.codewars.com/kata/53d32bea2f2a21f666000256/train/python
