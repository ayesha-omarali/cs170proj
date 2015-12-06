#this function is now useless. It was used to build our instances
import random
def random_num():
	i = random.randint(1, 4)
	if i == 4:
		return "0 "
	else:
		return "1 "
def random_mat(n, numba):
	ret = str(n) + "\n"
	for i in range(0, n):
		for j in range(0, n):
			if i == j:
				ret += "0 "
			else:
				ret += random_num()
		ret += "\n"
	text_file = open("matrix" + str(numba) + ".txt", "w")
	text_file.write(ret)
	text_file.close()
	return ret

def random_num_2():
	i = random.randint(1, 3)
	if i == 3:
		return 0
	else:
		return 1

def random_matrix_constructor(n):
	res = []
	for i in range(n):
		index = []
		for j in range(n):
			if i == j:
				index.append(0)
			else:
				index.append(random_num_2())
		res.append(index)
	return res




random_mat(100, 1)
random_mat(100, 2)
random_mat(100, 3)
