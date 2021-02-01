def distance(strand_a, strand_b):
    
 
	if len(strand_a) != len(strand_b):

		raise ValueError("The length of the strings do not match")

	result = len(strand_a) - (sum(strand_a == strand_b for strand_a, strand_b in zip(strand_a, strand_b)))

	return result