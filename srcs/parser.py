from .tokenizer import Tokenizer


class ParserError(Exception):
    pass

class Parser():
	@staticmethod
	def parse(av):
		validChars = ['0','1','2','3','4','5','6','7','8','9','x','X','=','^','+','-','*','/','.',' ']
		tokens = Tokenizer()
		for char in av:
			if char not in validChars:
				raise ParserError("noooooooo")
			else:
				tokens.addToken(char)
		tokens.expand()

