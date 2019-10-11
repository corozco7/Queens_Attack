import sys


archive = open("input.txt", "r")


def board_and_obstacles():
	first_line = archive.readline()
	first_line = first_line.rstrip("\n")
	first_line = first_line.split("  ")
	if _length(first_line):
		if _isdigit(first_line):
			first_line = _conversion(first_line)
			if first_line[0] > 0 and first_line[0] <= 100000:
				if first_line[1] >= 0 and first_line[1] <= 100000:
					if first_line[1] < first_line[0]**2:
						return first_line
					else:
						_error("There is no place for the queen")
				else:
					_error("The number of obstacles must be greater than or equal to 0 and less than or equal to 10^5")
			else:
				_error("The length of the board must be greater than 0 and less than or equal to 10^5")


def queen_position(board_length):
	second_line = archive.readline()
	second_line = second_line.rstrip("\n")
	second_line = second_line.split("  ")
	if _length(second_line):
		if _isdigit(second_line):
			second_line = _conversion(second_line)
			if second_line[0] <= board_length and second_line[1] <= board_length:
				return second_line
			else:
				_error("The queen is outside the board")
			

def validate3():
	pass


def _length(line):
	if len(line) == 2:
		return True
	else:
		_error("Only 2 numbers are accepted")


def _isdigit(line):
	if line[0].isdigit() and line[1].isdigit():
		return True
	else:
		_error("Only numbers are accepted")


def _conversion(line):
	return [int(line[0]), int(line[1])]


def _error(error):
	print(error)
	sys.exit()


if __name__ == '__main__':
	first_input = board_and_obstacles()
	print(first_input)
	second_input = queen_position(first_input[0])
	print(second_input)
