import sys
from srcs.parser import Parser
from sympy import symbols, Eq, solve
from srcs.solver import solve_equation

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Please introduce only 1 argument with correct format.')
		print('Format:')
		print('\"Polinomial equation to be solved with grade up to three\"')
		print('Example:')
		print('\"x^2 -X = 6\"')
		exit(1)
	try:
		equation = Parser.parse(sys.argv[1])
	except Exception as e:
		print(e)
		exit(1)
	print('\n-----------------------------------\n')
	print('Third step: SOLVE')
	try:
		degree = equation.as_poly().degree()
	except Exception as e:
		print('This equation has no solution as each side is equal to the other. Or it has infinite solutions. Try at least with grade 1.')
		exit(1)
	print('Polinomial degree: ' + str(degree))
	if degree > 3:
		print('The polynomial degree is stricly greater than 3, I can\'t solve.')
		exit(1)
	print('Solution: ')
	print(equation)
	equation = str(equation).replace('**2', '')
	equation = str(equation).replace('*X', '')
	equation = str(equation).replace('X', '1')
	print(equation)
	if degree == 2 and len(equation) == 5:
		a, b, c = equation.split(' ')
		equation = a + '+0' + b + c
	equation = equation.replace(' ', '')
	print(solve_equation(equation))




	# eq = Eq(equation, 0)
	# sol = solve(eq, dict=True)
	# i = 0
	# for s in sol:
	# 	s_str = str(s)
	# 	s_str = s_str.replace('{', '').replace('}', '')
	# 	print(f'Solution {i} = {s_str}')
	# 	i += 1
	# Test the function
	# print(solve_equation("2x + 3 = 0"))  # Linear equation
	# print(solve_equation("x^2 + 5x + 6 = 0"))  # Quadratic equation