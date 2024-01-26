# import sys
# from srcs.Parser import Parser
from sympy import symbols, Eq, solve

if __name__ == '__main__':

	# i'll start parsing the arguments and format them in the (args, 0) format converting each ^ to **.

	x = symbols('x')
	eq1 = Eq(x**2 -x - 6, 0)


	sol = solve(eq1)

	print(sol)
	# if len(sys.argv) != 2:
	# 	print('Please introduce only 1 argument with correct format.')
	# 	print('Format:')
	# 	print('\"Equation to be solved in double quotes\"')
	# 	exit(1)
	# print(type(sys.argv[1]))
	# Solver.solve(sys.argv[1])