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
	inputNums = "15275217996613369643172721682123315785815698496179798976913285366972876142616479915849833987811384156577122962271972971658196761372364219795357639692377138168857139699936929646259446571924941454262699"
	print(wordInterpret(inputNums))


if __name__ == '__main__':
	main()