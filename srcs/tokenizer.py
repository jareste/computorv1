class Tokenizer():
	def __init__(self):
		self.tokens = []
		self.expansions = []
		self.eqFound = False
		self.degree = 0
		self.xFound = False
		print('started')

	def checkEq(self, token):
		from parser import ParserError
		if token == '=' and self.eqFound == False:
			self.eqFound = True
		elif token == '=' and self.eqFound == True:
			raise ParserError('More than one equal found.')
		

	def addToken(self,token):
		self.checkEq(token)
		self.tokens.append(token)
		print('added', self.tokens)

	def expand(self):
		current_number = ''
		validChars = ['x','X','=','^','+','-','*','/','.',' ']

		for self.tokens in self.tokens:
			if self.tokens.isdigit():
				current_number += self.tokens
			elif self.tokens in validChars or self.tokens.isspace():
				if current_number:
					self.expansions.append(current_number)
					current_number = ''
				if not self.tokens.isspace() and self.tokens not in ['+', '-']:
					self.expansions.append(self.tokens)
		if current_number:
			self.expansions.append(current_number)
		
		print(self.expansions)

		print(self.expansions[3])
		for i in range(len(self.expansions)):
			expansion = self.expansions[i]
			from parser import ParserError
			if i < len(self.expansions) - 1 and expansion in validChars and self.expansions[i + 1] in validChars:
				print(expansion, self.expansions[i + 1])
				raise ParserError('Two incompatible operands ' + expansion + ' ' + self.expansions[i + 1] + ' together.')