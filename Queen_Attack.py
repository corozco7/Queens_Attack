import sys


archive = open("input.txt", "r")


def board_and_obstacles():
	"""Returns a list with the size of board and number of obstacles.

	Extract the first line of a file that contains two space-separated integers, validated as follows:
	
	-Only 2 numbers
	-Only Integers
	-The board size (n) must be 0 < n <= 100000
	-The amount of obstacles (k) must be 0 <= k <= 100000
	-There should be no obstacles when the board size is 1
	-The amount of obstacles must be k < n^2

	"""
	first_line = archive.readline()
	first_line = first_line.rstrip("\n")
	first_line = first_line.split(" ")
	if _length(first_line):
		if _isdigit(first_line):
			first_line = _conversion(first_line)
			if first_line[0] > 0 and first_line[0] <= 100000:
				if first_line[1] >= 0 and first_line[1] <= 100000:
					if first_line[0] == 1 and first_line[1] > 0:
						_error("There is no place for the queen")
					elif first_line[1] < first_line[0]**2:
						return first_line
					else:
						_error("There is no place for the queen")
				else:
					_error("The number of obstacles must be greater than or equal to 0 and less than or equal to 10^5")
			else:
				_error("The length of the board must be greater than 0 and less than or equal to 10^5")


def queen_position(board_length):
	"""Returns a list with the position of the queen.
	
	Extract the second line of a file that contains two space-separated integers, validated as follows:

	-Only 2 numbers
	-Only Integers
	-Queen's position must inside the board (rq <= n, cq <= n)

	"""
	second_line = archive.readline()
	second_line = second_line.rstrip("\n")
	second_line = second_line.split(" ")
	if _length(second_line):
		if _isdigit(second_line):
			second_line = _conversion(second_line)
			if _board_out(second_line, board_length, "The queen is outside the board"):
				return second_line
			

def obstacle_position(board_length, obstacles, queen_position):
	"""Returns a list of arrays with the positions of the obstacles.


	Extract from the third line onwards from a file, two space-separated integers in each line, validated as follows:

	-Returns an empty array if k = 0
	-Only 2 numbers in each line
	-Only Integers in each line
	-Obstacle's position must be inside the board (rk <= n, ck <= n)
	-Obstacle's position should not be the same as the queen
	-The length of the returned list must be the same as the number of obstacles

	"""
	lines = []
	if obstacles > 0 :	
		for line in archive.readlines():
			line = line.rstrip("\n")
			line = line.split(" ")
			if _length(line):
				if _isdigit(line):
					line = _conversion(line)
					if _board_out(line, board_length, "The obstacle is outside the board"):
						if line == queen_position:
							_error("The obstacle cannot have the same position as the queen")
						elif len(lines) == obstacles:
							break
						else:
							lines.append(line)
		if obstacles > len(lines):
			_error("Missing obstacles")
		return lines
	else:
		return lines


def up(queen_position, board_length, obstacles):
	"""Returns the amount of squares that the queen can move towards up, stop counting when an obstacle is found."""
	count = 0
	rq = queen_position[0] + 1
	while rq <= board_length:
		if _isObstacles(rq, queen_position[1], obstacles):
			rq += 1
			count += 1
		else:
			break
	return count


def down(queen_position, obstacles):
	"""Returns the amount of squares that the queen can move towards down, stop counting when an obstacle is found."""
	count = 0
	rq = queen_position[0] - 1
	while rq >= 1:
		if _isObstacles(rq, queen_position[1], obstacles):
			rq -= 1
			count += 1
		else:
			break
	return count


def left(queen_position, obstacles):
	"""Returns the amount of squares that the queen can move towards left, stop counting when an obstacle is found."""
	count = 0
	cq = queen_position[1] - 1
	while cq >= 1:
		if _isObstacles(queen_position[0], cq, obstacles):
			cq -= 1
			count += 1
		else:
			break
	return count


def right(queen_position, board_length, obstacles):
	"""Returns the amount of squares that the queen can move towards right, stop counting when an obstacle is found."""
	count = 0
	cq = queen_position[1] + 1
	while cq <= board_length:
		if _isObstacles(queen_position[0], cq, obstacles):
			cq += 1
			count += 1
		else:
			break
	return count


def up_right(queen_position, board_length, obstacles):
	"""Returns the amount of squares that the queen can move to the right diagonal up, stop counting when an obstacle is found."""
	count = 0
	rq = queen_position[0] + 1
	cq = queen_position[1] + 1
	while rq <= board_length and cq <= board_length:
		if _isObstacles(rq, cq, obstacles):
			rq += 1
			cq += 1
			count += 1
		else:
			break
	return count


def up_left(queen_position, board_length, obstacles):
	"""Returns the amount of squares that the queen can move to the left diagonal up, stop counting when an obstacle is found."""
	count = 0
	rq = queen_position[0] + 1
	cq = queen_position[1] - 1
	while rq <= board_length and cq >= 1:
		if _isObstacles(rq, cq, obstacles):
			rq += 1
			cq -= 1
			count += 1
		else:
			break
	return count


def down_right(queen_position, board_length, obstacles):
	"""Returns the amount of squares that the queen can move to the right diagonal down, stop counting when an obstacle is found."""
	count = 0
	rq = queen_position[0] - 1
	cq = queen_position[1] + 1
	while rq >= 1 and cq <= board_length:
		if _isObstacles(rq, cq, obstacles):
			rq -= 1
			cq += 1
			count += 1
		else:
			break
	return count


def down_left(queen_position, obstacles):
	"""Returns the amount of squares that the queen can move to the left diagonal down, stop counting when an obstacle is found."""
	count = 0
	rq = queen_position[0] - 1
	cq = queen_position[1] - 1
	while rq >= 1 and cq >= 1:
		if _isObstacles(rq, cq, obstacles):
			rq -= 1
			cq -= 1
			count += 1
		else:
			break
	return count


def _length(line):
	"""Validate if there are only 2 numbers on the line."""
	if len(line) == 2:
		return True
	else:
		_error("Only 2 numbers are accepted")


def _isdigit(line):
	"""Validate if the numbers are integers"""
	if line[0].isdigit() and line[1].isdigit():
		return True
	else:
		_error("Only integers are accepted")


def _conversion(line):
	"""Turn the strings into integers"""
	return [int(line[0]), int(line[1])]


def _board_out(line, board_length, error):
	"""Validate if the piece is off the board"""
	if line[0] <= board_length and line[1] <= board_length:
		return True
	else:
		_error(error)


def _isObstacles(rq, cq, obstacles):
	"""Validate if an obstacle is found"""
	var = True
	compare = [rq, cq]
	for x in obstacles:
		if compare == x:
			var = False
			break
	return var


def _error(error):
	"""Print an error and close the program"""
	print(error)
	sys.exit()


if __name__ == '__main__':
	first_input = board_and_obstacles()
	second_input = queen_position(first_input[0])
	third_input = obstacle_position(first_input[0], first_input[1], second_input)
	queen_attack = up(second_input, first_input[0], third_input) + down(second_input, third_input) + left(second_input, third_input) + right(second_input, first_input[0], third_input) + up_right(second_input, first_input[0], third_input) + up_left(second_input, first_input[0], third_input) + down_right(second_input, first_input[0], third_input) + down_left(second_input, third_input)
	print(queen_attack)
	archive.close()