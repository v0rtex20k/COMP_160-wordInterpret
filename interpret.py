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
	elif int(inputNums[0]) == 0:
		return 0
	elif int(inputNums[1]) == 0:
		inputNums[1] = '9'
	elif 10*int(inputNums[0]) + int(inputNums[1]) < 27:
		return wordInterpret(inputNums[1:]) + wordInterpret(inputNums[2:])
	return wordInterpret(inputNums[1:])

def main():
	#inputNums = "15275217996613369643"
	inputNums = "15275217996613369643172721682123315785815698496179798976913285366972876142616479915849833987811384156577122962271972971658196761372364219795357639692377138168857139699936929646259446571924941454262699"
	result = wordInterpret(inputNums)
	print(result)

if __name__ == '__main__':
	main()

