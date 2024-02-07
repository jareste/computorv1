import re


class ParserError(Exception):
    pass

class Parser():

	@staticmethod
	def parse(av):
		equalFound = 1
		a = 0
		b = 0
		c = 0
		number = 0
		haveNumber = False
		sign = '+'
		for term in av:
			if term == ' ':
				continue
			if not re.match(r"^[Xx0-9*-^+=]", term):
				# print(term)
				raise ParserError("Invalid character in expression or invalid format")

		av_list = list(av) 

		i = 0
		sign = 1
		while i < len(av_list):
			term = av_list[i]
			# print('term', term)
			if term.isspace():
				i += 1
				continue
			if term == '=':
				equalFound = -1
				number = 0
				sign = 1
				i += 1
				continue
			if term.isdigit() or (term == '.' and i+1 < len(av_list) and av_list[i+1].isdigit()):
				number_str = term
				while i+1 < len(av_list) and (av_list[i+1].isdigit() or av_list[i+1] == '.'):
					i += 1
					number_str += av_list[i]
				number = float(number_str)
				haveNumber = True
			else:
				if number != 0 or term == '*' or haveNumber == True:
					if term == '*':
						if i+4 < len(av_list) and (av_list[i+2] == 'X' or av_list[i+2] == 'x') and av_list[i+3] == '^' and av_list[i+4].isdigit():
							i += 1
							continue
						else:
							raise ParserError("Invalid format after *")
					if term == 'X' or term == 'x':
						if i+1 < len(av_list) and av_list[i+1] == '^':
							if i+2 < len(av_list) and av_list[i+2].isdigit():
								if av_list[i+2] == '2':
									a += sign * number * equalFound
								elif av_list[i+2] == '1':
									b += sign * number * equalFound
								elif av_list[i+2] == '0':
									c += sign * number * equalFound
									# print(c, sign, number, equalFound)
								else:
									raise ParserError("Grade is greater than 2")
								number = 0
								i += 3
								haveNumber = False
								continue
							else:
								raise ParserError("Invalid format after X")

				# print('term2', term)
				if re.match(r"^[+-]$", term):
					if term == '-':
						sign = -1
					elif term == '+':
						sign = 1
					# print('term3', term, sign)
				else:
					raise ParserError("Invalid format")
				# else:
				# 	haveNumber = False
				if term == '^':
					raise ParserError("Missing an X before the ^")
			i += 1
		# print(a, b, c)
		return a, b, c

