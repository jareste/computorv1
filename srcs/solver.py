from .parser import Parser

class Solver():
	@staticmethod
	def solve(av):
		try:
			Parser.parse(av)
		except Exception as e:
			print(f"An exception of type {type(e).__name__} occurred: {e}")
