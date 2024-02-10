class ParserError(Exception):
	pass

class Parser():

	@staticmethod
	def check_equal(av):
		equalfound = False
		for i in range(len(av)):
			if av[i] == '=':
				if equalfound:
					raise ParserError("Found more than one equal sign.")
				equalfound = True
		if not equalfound:
			raise ParserError("No equal sign found.")

	@staticmethod
	def parse(av):
		Parser.check_equal(av)
		i = 0
		number = 0
		sign = 1
		equal = 1
		grades = {'1': 0, '2': 0, '0': 0}
		if av[0] == '-':
			sign = -1
			i += 1
		while i < len(av) and av[i] == ' ':
			i += 1
		if i == len(av):
			raise ParserError("No number found.")
		while i < len(av):
			print('i:',i, av[i], 'len', len(av))
			while i < len(av) and av[i] == ' ':
				i += 1
			# parse after equal
			if av[i] == '=':
				equal = -1
				i += 1
				while i < len(av) and av[i] == ' ':
					i += 1
				if i == len(av):
					raise ParserError("No number found after equal sign.")
				if av[i] == '-':
					sign = -1
					i += 1
				if av[i] == '+':
					i += 1
				while i < len(av) and av[i] == ' ':
					i += 1
				if i == len(av):
					raise ParserError("No number found after equal sign.")
			#get number
			if av[i].isdigit():
				print('entro')	
				dot = False
				grade = 0
				# get the number
				while i < len(av) - 1 and av[i].isdigit() or av[i] == '.':
					if av[i] == '.':
						if dot:
							raise ParserError("Found more than one dot in a single number.")
						dot = True
						
					else:
						if dot:
							number += float(av[i]) / 10
						else:
							number = number * 10 + float(av[i])
					i += 1
				if i == len(av) - 1 and av[i].isdigit():
					number = number * 10 + float(av[i])
					# print(i, len(av), av[i])
				# remove spaces after it
				while i < len(av) and av[i] == ' ':
					i += 1
				# check if there is a grade
				if i < len(av) and av[i] == 'x':
					i += 1
					print('xgrade', av[i])
					print('entrooooo')
					if i < len(av) and av[i] != ' ' and av[i] != '+' and av[i] != '-' and av[i] != '=':
						if i < len(av) and av[i] == '^':
							i += 1
							if i < len(av) and av[i].isdigit():
								while i < len(av) and av[i].isdigit():
									grade = grade * 10 + int(av[i])
									i += 1
							else:
								raise ParserError("Invalid grade.")
						else:
							raise ParserError("Invalid grade format.")
					if grade == 0:
						grade = 1
				print('number: ', number, grade, sign, equal)
				grades[str(grade)] = grades.get(str(grade), 0) + number * sign * equal
				sign = 1
				grade = 0
				number = 0
			# check if there is a sign
			if av[i] == '+' or av[i] == '-':
				if av[i] == '-':
					sign = -1
				else:
					sign = 1
				i += 1
			if i == len(av) - 1:
				break
		
		# Sort the dictionary by key
		sorted_grades = {k: v for k, v in sorted(grades.items(), key=lambda item: int(item[0])) if v != 0}
		# Format the dictionary to the desired string
		formatted_grades = " + ".join([f"{v}x^{k}" if int(k) != 0 else str(v) for k, v in sorted_grades.items()])

		# Initialize highest_key to None
		highest_key = None

		# Iterate over the items in the dictionary
		for key, value in grades.items():
			# Check if the value is greater than 0
			if value > 0:
				# If highest_key is None or the current key is greater than highest_key
				if highest_key is None or int(key) > int(highest_key):
					# Update highest_key
					highest_key = key

		# Print the highest key with a relevant value
		if highest_key is not None:
			print(f"The highest key with a relevant value is: {highest_key}")
		else:
			print("No key with a relevant value found.")


		print(formatted_grades)
		print(grades)


if __name__ == "__main__":
	try:
		Parser.parse("1.0 * x^0 +   2.0x  - 09.0x^2  = -3")
	except Exception as e:
		print(e)
		
		
		
		
	
