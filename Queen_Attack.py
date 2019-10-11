archive = open("input.txt", "r")


def board_and_obstacles():
	first_line = archive.readline()
	first_line = first_line.split("  ")
	if len(first_line) == 2:
		if int(first_line[0]) and int(first_line[0]):
			f_tuple = (int(first_line[0]), int(first_line[1]))
			return f_tuple
		else:
			print("error")
	else:
		print("error")


def validate2():
	print(archive.readline())


def validate3():
	for x in archive:
		print(x)


if __name__ == '__main__':
	first_input = board_and_obstacles()
	print(first_input)