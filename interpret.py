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
import math

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
	if int(inputNums[0]) == 1 or int(inputNums[0]) == 2: 					# good number
		return wordInterpret(inputNums[1:]) + wordInterpret(inputNums[2:]) 
	else:
		return wordInterpret(inputNums[1:])									# bad number