def filter_long_words(sentence,n):
	splitted_sentence = sentence.split(" ")
	lst = []
	for x in splitted_sentence:
		if len(x) > n:
			lst.append(x)
	return lst

# solution for https://www.codewars.com/kata/5697fb83f41965761f000052/train/python
