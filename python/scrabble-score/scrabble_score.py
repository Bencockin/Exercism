def score(word):

	result = 0

	one = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
	two = ["D","G"]
	three = ["B", "C", "M", "P"]
	four = ["F", "H", "V", "W", "Y"]
	five = ["K"]
	eight = ["J", "X"]
	ten = ["Q", "Z"]

	string = word.upper()

	for letter in string:

	    if letter in one:
	        
	    	result += 1
	    
	    if letter in two:
	        
	    	result += 2
	        
	    if letter in three:
	        
	    	result += 3
	        
	    if letter in four:
	        
	    	result += 4
	        
	    if letter in five:
	        
	    	result += 5
	        
	    if letter in eight:
	        
	    	result += 8
	        
	    if letter in ten:
	        
	    	result += 10

	return result