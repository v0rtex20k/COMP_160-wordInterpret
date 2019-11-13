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

def memoizer(func):
	memo = {}
	def decorated_wordInterpret(*args):
		if args not in memo:
			memo[args] = func(*args)
		return memo[args]
	return decorated_wordInterpret

# inputNums is a string
# function returns an int
@memoizer
def wordInterpret(inputNums):
	if len(inputNums) <= 1:
		return 1
	elif int(inputNums[0]) == 0:
		return 0
	elif int(inputNums[1]) == 0:
		inputNums = inputNums[0] + '9' + inputNums[2:]
	elif 10*int(inputNums[0]) + int(inputNums[1]) < 27:
		return wordInterpret(inputNums[1:]) + wordInterpret(inputNums[2:])
	return wordInterpret(inputNums[1:])

