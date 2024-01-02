def validate_usr(username):

	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,!"
	length = len(username)

	if length < 4 or length >= 16:
		return False

	for x in username:
		if x in uppercase:
			return False
			break

	else:
		return True

# solution for https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023/train/python
