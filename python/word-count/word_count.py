def count_words(sentence):

	d = {}

	sen = sentence.lower()

	for word in sen.split():
	    
		d[word] = sen.count(word)

	return d
