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

# inputNums is a string
# function returns an int

# O(n) time complexity since we only scan through the input once
@memoizer
def wordInterpret(inputNums):
	if len(inputNums) == 1: 	# if there is only one number (0-9) left, it must map to a letter
		return 1
	elif int(inputNums[0]) == 0:	# if the ORIGINAL number starts with a 0, return 0 immediately
		return 0
	elif int(inputNums[1]) == 0:	# if there zeros inside the number, transform them into 9's to ignore them
		inputNums = inputNums[0] + '9' + inputNums[2:]
	elif 10*int(inputNums[0]) + int(inputNums[1]) < 27: 	# if the current first two numbers are between 10-26 (only valid 2-digit mappings), keep "good" numbers
		return wordInterpret(inputNums[1:]) + wordInterpret(inputNums[2:])
	return wordInterpret(inputNums[1:]) 	# else, ignore "bad" numbers (3-9, since zeros have been transformed)

