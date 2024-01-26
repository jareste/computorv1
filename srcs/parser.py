from .tokenizer import Tokenizer
import re
from sympy import symbols, Eq, solve, simplify


class ParserError(Exception):
    pass

class Parser():
	@staticmethod
	def parse(av):
		if not re.match("^[0123456789xX=^+\\-*/. ]*$", av): 		# check for invalid characters
			raise ParserError("Found an invalid character in the equation.")
		rmeq = av.split('=')
		if len(rmeq) != 2: # check for more than one equal sign
			raise ParserError("Found more than one equal sign.")
		rmeq[0] = rmeq[0].replace(' ', '')
		rmeq[1] = rmeq[1].replace(' ', '')
		if rmeq[0] == '' or rmeq[1] == '':	# check for empty sides
			raise ParserError("Found an empty side.")
		if re.search("[*/]{2,}", rmeq[0]) or re.search("[*/]{2,}", rmeq[1]): # check for more than one operator in a row
			raise ParserError("Found more than one operator in a row.")
		if len(rmeq[0]) == 1 and re.search("[+\-.\^*/]", rmeq[0]): # check for x = 0	
			raise ParserError("Found an invalid equation.")
		if len(rmeq[1]) == 1 and re.search("[+\-.\^*/]", rmeq[1]): # check for x = 0	
			raise ParserError("Found an invalid equation.")
		if rmeq[0][0] == '*' or rmeq[1][0] == '*' or rmeq[0][0] == '/' or rmeq[1][0] == '/': # check for x = 0
			raise ParserError("Found an invalid equation.")
		if rmeq[0][len(rmeq[0]) - 1] == '*' or rmeq[1][len(rmeq[1]) - 1] == '*' or rmeq[0][len(rmeq[0]) - 1] == '/' or rmeq[1][len(rmeq[1]) - 1] == '/': # check for x = 0
			raise ParserError("Found an invalid equation.")
		rmeq[0] = rmeq[0].replace('^', '**')
		rmeq[1] = rmeq[1].replace('^', '**')
		x = symbols('x')
		left_side = simplify(rmeq[0])
		right_side = simplify(rmeq[1])
		equation = simplify(left_side - right_side)
		print(left_side)
		print(right_side)
		print(equation)	
		test = str(equation).replace('**', '^')
		print(test)
		print(rmeq)
		
		print('fino')
		print("valid")
		return equation
		# validChars = set(['0','1','2','3','4','5','6','7','8','9','x','X','=','^','+','-','*','/','.',' '])
		# tokens = Tokenizer()
		# for char in av:
		# 	if char not in validChars:
		# 		raise ParserError("noooooooo")

