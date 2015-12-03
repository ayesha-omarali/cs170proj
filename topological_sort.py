import operator

def find_source_nodes(matrix):
	"""
	>>> find_source_nodes([])
	[]
	>>> find_source_nodes([[1, 0, 1], [1, 0, 0], [0, 0, 0]])
	[1]
	"""
	if(len(matrix) == 0):
		return []
	if(len(matrix[0]) == 0):
		return []
	else:
		x = len(matrix)
		y = len(matrix[0])
		if(x != y):
			return []
		sources = []
		j = 0
		while(j < x):
			i = 0
			while(i < y):
				if(matrix[i][j] != 0):
					break
				i += 1
			if(i == x):
				sources += [j]
			j += 1	
		return sources

number = 1
def topological_sort(matrix):
	if(len(matrix) > 0 and len(matrix[0]) > 0 and len(matrix) == len(matrix[0])):
		sources_list = find_source_nodes(matrix)
		pre_order = {}
		post_order = {}
		def visit(i):
			global number
			if i not in pre_order:
				pre_order[i] = number
				number += 1
				for j in range(0, len(matrix)):
					if(matrix[i][j] == 1):
						visit(j)
				post_order[i] = number
				number += 1
		for n in sources_list:
			visit(n)
		rev = {}
		for item in post_order:
			rev[post_order[item]] = item
		sorted_post_order = sorted(rev.items(), key=rev.get, reverse=True)
		sorted_post_order.reverse()
		top_sort = []
		for tup in sorted_post_order:
			top_sort += [tup[1]]
		return top_sort

# topological_sort([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
							
