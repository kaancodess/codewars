def maskify(cc):
	if len(cc) <= 4:
		return cc
	else:
		length = len(cc)
		last = cc[-4:]
		rest = cc[0:length-4]
		privacy = ''
		privacy += '#'*len(rest)
		return privact + last
