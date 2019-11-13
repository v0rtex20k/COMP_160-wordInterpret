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

memo = {}
def memoizer(func):
	def decorated_wordInterpret(*args):
		if args not in memo:
			memo[args] = func(*args)
		return memo[args]
	return decorated_wordInterpret

# inputNums is a string
# function returns an int
@memoizer
def wordInterpret(inputNums):
	if int(inputNums[0]) == 0:
		return -math.inf
	if len(inputNums) <= 1:
		return 1
	if int(inputNums[0]) == 1 or int(inputNums[0]) == 2: 					# good number
		return wordInterpret(inputNums[1:]) + wordInterpret(inputNums[2:]) 
	else:
		return wordInterpret(inputNums[1:])									# bad number


def main():
	inputNums = "04164106885502258532"
	result = wordInterpret(inputNums)
	print(max(result, 0))

	print(memo)


if __name__ == '__main__':
	main()