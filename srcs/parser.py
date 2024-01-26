from .tokenizer import Tokenizer
import re

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
		
		print(rmeq)
		
		print('fino')
		print("valid")
		# validChars = set(['0','1','2','3','4','5','6','7','8','9','x','X','=','^','+','-','*','/','.',' '])
		# tokens = Tokenizer()
		# for char in av:
		# 	if char not in validChars:
		# 		raise ParserError("noooooooo")

