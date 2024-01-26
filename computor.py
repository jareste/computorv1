import sys
from srcs.parser import Parser
from sympy import symbols, Eq, solve

if __name__ == '__main__':

	# i'll start parsing the arguments and format them in the (args, 0) format converting each ^ to **.

	# x = symbols('x')
	# eq1 = Eq(x**2 -x - 6, 0)


	# sol = solve(eq1)

	# print(sol)
	if len(sys.argv) != 2:
		print('Please introduce only 1 argument with correct format.')
		print('Format:')
		print('\"Equation to be solved in double quotes\"')
		exit(1)
	try:
		equation = Parser.parse(sys.argv[1])
	except Exception as e:
		print(e)
	eq = Eq(equation, 0)
	sol = solve(eq, dict=True)
	print(sol)