import re
from sympy import symbols, Eq, solve, simplify


class ParserError(Exception):
    pass

class Parser():

	@staticmethod
	def __checkValidChars(av):
		if not re.match("^[0123456789xX=^+\\-*/. ]*$", av): 		# check for invalid characters
			raise ParserError("Found an invalid character in the equation.")

	@staticmethod
	def __checkEqualSign(av):
		rmeq = av.split('=')
		if len(rmeq) != 2: # check for more than one equal sign
			raise ParserError("Found more than one equal sign.")
		rmeq[0] = rmeq[0].replace(' ', '')
		rmeq[1] = rmeq[1].replace(' ', '')
		if rmeq[0] == '' or rmeq[1] == '':	# check for empty sides
			raise ParserError("Found an empty side.")
		return rmeq

	@staticmethod
	def __checkOperators(rmeq):
		if re.search("[*/]{2,}", rmeq[0]) or re.search("[*/]{2,}", rmeq[1]): # check for more than one operator in a row
			raise ParserError("Found more than one operator in a row.")

	@staticmethod
	def __checkXeq0(rmeq):
		if len(rmeq[0]) == 1 and re.search("[+\-.\^*/]", rmeq[0]): # check for x = 0	
			raise ParserError("Found an invalid equation.")
		if len(rmeq[1]) == 1 and re.search("[+\-.\^*/]", rmeq[1]): # check for x = 0	
			raise ParserError("Found an invalid equation.")
		if rmeq[0][0] == '*' or rmeq[1][0] == '*' or rmeq[0][0] == '/' or rmeq[1][0] == '/': # check for x = 0
			raise ParserError("Found an invalid equation.")
		if rmeq[0][len(rmeq[0]) - 1] == '*' or rmeq[1][len(rmeq[1]) - 1] == '*' or rmeq[0][len(rmeq[0]) - 1] == '/' or rmeq[1][len(rmeq[1]) - 1] == '/': # check for x = 0
			raise ParserError("Found an invalid equation.")

	@staticmethod
	def __checkXposition(rmeq):
		for element in range(0, len(rmeq[0])):
			print(rmeq[0][element])
			if element > 0 and rmeq[0][element] == 'X' and (re.match("[0-9]", rmeq[0][element -1] or re.match("[0-9]", rmeq[0][element + 1]))):
				raise ParserError("Found an invalid equation.")
		for element in range(0, len(rmeq[1])):
			if element > 0 and rmeq[1][element] == 'X' and (re.match("[0-9]", rmeq[1][element -1] or re.match("[0-9]", rmeq[1][element + 1]))):
				raise ParserError("Found an invalid equation.")

	def __replacemultonX(rmeq):
		rmeq[0] = rmeq[0].replace('*X', 'X')
		rmeq[1] = rmeq[1].replace('*X', 'X')
		return rmeq

	@staticmethod
	def parse(av):
		print('First step: PARSE')
		
		av = av.replace('x', 'X')
		
		Parser.__checkValidChars(av)
		print('no')
		rmeq = Parser.__checkEqualSign(av)
		print('no')
		Parser.__checkOperators(rmeq)
		print('no')
		Parser.__checkXeq0(rmeq)
		print('no')
		Parser.__checkXposition(rmeq)
		print('Left side after parsing: ' + rmeq[0])
		print('Right side after parsing: ' + rmeq[1])
		print(rmeq[0] + ' = ' + rmeq[1])
		
		rmeq[0] = rmeq[0].replace('^', '**')
		rmeq[1] = rmeq[1].replace('^', '**')
		x = symbols('x')
		print('aqui' + rmeq[0])
		left_side = simplify(rmeq[0])
		right_side = simplify(rmeq[1])
		equation = simplify(left_side - right_side)
		rmeq = Parser.__replacemultonX(rmeq)
		print(rmeq)
		print('\n-----------------------------------\n')
		print('Second step: SIMPLIFY')
		print('Left side after simplyfing: ' + str(left_side).replace('**', '^') )
		print('Right side after simplyfing: ' + str(right_side).replace('**', '^'))
		print(str(equation).replace('**', '^') + ' = 0')
		return equation

