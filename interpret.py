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

#for i in range(len(inputNums)):
		#	if int(inputNums[i]) == 1 or int(inputNums[i]) == 2:
		#		group(inputNums, i)
		#print("--------------------------------")

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
	if len(inputNums) <= 1:
		return 1
	if int(inputNums[0]) == 1:
		return wordInterpret(inputNums[1:]) + wordInterpret(inputNums[2:])
	elif int(inputNums[0]) == 2:
		if int(inputNums[1]) < 7:
			return wordInterpret(inputNums[1:]) + wordInterpret(inputNums[2:])
	return wordInterpret(inputNums[1:])

def group(word, i):
	for x in range(len(word)-1):
		print(word[x], end="")
		if x != i:
			print("-", end="")
	print(word[len(word)-1])

def main():
	inputNums = "15275217996613369643"
	result = wordInterpret(inputNums)
	print(result)
	print(memo)


if __name__ == '__main__':
	main()

