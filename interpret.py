##########################################################################
#
#    Tufts University, Comp 160 wordInterpret coding assignment
#
#    interpret.py
#    wordInterpret
#
#    includes function students need to implement
#
##########################################################################

# Memoizer for our recursive function calls. 
# O(n) space complexity
def memoizer(func):
	memo = {}
	def decorated_wordInterpret(*args):
		if args not in memo:
			memo[args] = func(*args)
		return memo[args]
	return decorated_wordInterpret

# Analysis of wordInterpret():
#
# 	- O(n) time complexity since we only scan through the input once.
#
#            		/ 
#			|   0 if inputNums[n] is 0 
#			|
#			|   1 if end of input
#	- T(n) =	|
#  		        |   T(n-1) if inputNums[n] is 1 or 2
#			|
#			|   T(n-1) + T(n-2) otherwise
#			 \
#
#  - Justification: We traverse through our input in pairs. If the current number
#    		    and it's right neighbor form a pair that is outside our range
#		    (aka >= 27), we know that those numbers can never be grouped 
#		    together, and should not be counted. We therefore must treat 
#		    the current number as an individual (inputNums[1:]) and try 
#		    our luck with the next pair.
#		    Conversely, if the pair is INSIDE our range (aka < 27), it
#		    is a valid pairing, and we consider that pair as individual
#		    numbers (inputNums[1:]) and as a pair (inputNums[2:]) using
#		    recursion. 
#		    Zeros are special, since they can never be the "units digit"
#		    of a pair UNLESS the "tens digit" is 1 or 2. Furthermore, 
#	            they can never be a "tens digit" and they can never be an
#		    individual, under any circumstances. As we recurse, if we 
#		    find a 0 "tens digit", we do NOT consider it, and return
#		    0 immediately. If the zero is the units digit of a 1 or 2,
#		    however, it is captured in our case <27, since 10 and 20
#		    are less than 27.
#					
#					
@memoizer
def wordInterpret(inputNums):
	if len(inputNums) <= 1: 	# if there is only one number (0-9) left, it must map to a letter
		return 1
	elif int(inputNums[0]) == 0:	# if the ORIGINAL number starts with a 0, return 0 immediately
		return 0
	elif 10*int(inputNums[0]) + int(inputNums[1]) < 27: 	# keep "good" numbers between 10-26 (only valid 2-digit mappings)
		return wordInterpret(inputNums[1:]) + wordInterpret(inputNums[2:])
	elif int(inputNums[1]) == 0: 	# if there is a zero inside the number NOT next to a "good" number, return 0 immediately
		return 0
	return wordInterpret(inputNums[1:]) 	# else, ignore "bad" numbers (3-9, since zeros have been dealt with)

