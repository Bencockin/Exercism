def abbreviate(words):

	ex = "!/?><-=+_"

	for l in words:
		if l in ex:
			words = words.replace(l,' ')

	x = words.split()

	result = ""

	for words in x:

		result += words[0]

	return result.upper()
