##########################################################################
#
#    Tufts University, Comp 160 wordInterpret coding assignment
#
#    main.py
#    wordInterpret
#
#    simple main to test wordInterpret
#    NOTE: this main is only for you to test wordInterpret. We will compile
#          your code against a different main in our autograder directory
#
##########################################################################

from interpret import wordInterpret


def main():
	inputNums = "04164106885502258532"
	result = wordInterpret(inputNums)
	print(result)


if __name__ == '__main__':
	main()