def sum_array(arr):
	if arr == None:
		return 0

	if len(arr) > 1:
		array_max = max(arr)
		array_min = min(arr)
		max_and_min = array_max + array_min
		total = sum(arr) - max_and_min
		return total
	else:
		return 0

# solution for https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python
