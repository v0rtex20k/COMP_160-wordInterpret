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
	#inputNums = "152752179966133696431727216821233157858156984961797989769132853669728761426164799158498339878113841565771229622719729716581967613723642197953576396923771381688571396999369296462594465719249414542626990"
	#inputNums = "70458739895068689786"
	inputNums = "53108684246528581296"
	print(wordInterpret(inputNums))


if __name__ == '__main__':
	main()