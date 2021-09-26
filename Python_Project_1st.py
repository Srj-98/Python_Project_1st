class StringOperations:
	def reverse(to_be_reversed = None):
		return to_be_reversed[::-1]

class RversedString(StringOperations):
		def __init__(self, inputString):
			self.to_be_reversed = inputString
		def show (self):
			result = StringOperations.reverse(self.to_be_reversed)
			print(f"The input string is: {self.to_be_reversed} and the enversed is {result}")
if __name__ == '__main__':
		x=RversedString("Siraj")
		x.show()