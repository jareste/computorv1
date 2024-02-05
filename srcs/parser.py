import re


class ParserError(Exception):
    pass

class Parser():

	@staticmethod
	def parse(av):
		equalFound = False
		a = 0
		b = 0
		c = 0
		number = 0
		sign = '+'
		if not re.match(r"^[Xx0-9*-+=]", av):
			raise ParserError("Invalid character in expression or invalid format")

		av_list = list(av) 

		i = 0
		sign = 1
		while i < len(av_list):
			term = av_list[i]
			if term.isspace():
				i += 1
				continue
			if term == '=':
				equalFound = True
				number = 0
				sign = -1
				i += 1
				continue
			if term.isdigit() or (term == '.' and i+1 < len(av_list) and av_list[i+1].isdigit()):
				number_str = term
				while i+1 < len(av_list) and (av_list[i+1].isdigit() or av_list[i+1] == '.'):
					i += 1
					number_str += av_list[i]
				number = float(number_str)
			else:
				if number != 0:
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
									a += sign * number
								elif av_list[i+2] == '1':
									b += sign * number
								elif av_list[i+2] == '0':
									c += sign * number
								else:
									raise ParserError("Grade is greater than 2")
								number = 0
								i += 3
								continue
							else:
								raise ParserError("Invalid format after X")
				if number == 0 and i != 1:
					if re.match(r"^[+-]$", term):
						if term == '-' and equalFound == False:
							sign = -1
						elif term == '+' and equalFound == False:
							sign = 1
						elif term == '-' and equalFound == True:
							sign = 1
						elif term == '+' and equalFound == True:
							sign = -1
					else:
						raise ParserError("Invalid format")
				if term == '^':
					raise ParserError("Missing an X before the ^")
			i += 1
		print(a, b, c)
		return a, b, c

