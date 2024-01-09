import sys
from srcs.solver import Solver

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Please introduce only 1 argument with correct format.')
		print('Format:')
		print('\"Equation to be solved in double quotes\"')
		exit(1)
	print(type(sys.argv[1]))
	Solver.solve(sys.argv[1])