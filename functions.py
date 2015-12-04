import operator
import itertools

#Given a matrix, the function returns the node ids of all of the source node 
#(or no id if no source node exists i.e. in a cycle)
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

#This does dfs of an inputted graph. The graph must be a DAG. 
number = 1
def dfs(matrix):
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
	return [pre_order, post_order]
	
#This returns a topological order sort of a DAG, and only a DAG
def topological_sort(matrix):
	if(len(matrix) > 0 and len(matrix[0]) > 0 and len(matrix) == len(matrix[0])):
		post_order = dfs(matrix)[1]
		rev = {}
		for item in post_order:
			rev[post_order[item]] = item
		sorted_post_order = sorted(rev.items(), key=rev.get, reverse=True)
		sorted_post_order.reverse()
		top_sort = []
		for tup in sorted_post_order:
			top_sort += [tup[1]]
		print(top_sort)
		return top_sort

# Step 1: For each node prepare the destination and predecessor
def initialize(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in range(0, len(graph)):
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if graph[node][neighbour] != 0 and d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour] = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in range(0, len(graph)):
            for v in range(0, len(graph[u])): #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it

    # Step 3: check for negative-weight cycles
    for u in range(0, len(graph)):
        for v in range(0, len(graph[u])): #For each neighbour of u
            assert d[v] <= d[u] + graph[u][v] or graph[u][v] == 0

    return d, p

def count_forward_paths(lst, matrix):
	count = 0
	i = 0
	while(i < len(lst)):
		j = i + 1
		while(j < len(lst)):
			count += matrix[lst[i]][lst[j]]
			j += 1
		i += 1
	return count

#
def flatten(lst_of_lsts):
	ret = []
	for lst in lst_of_lsts:
		ret += lst
	return ret

#gets all possible orderings of a particular list. It is slow for 8 nodes and above. s
def all_orderings(lst):
	if len(lst) <= 1:
		return [lst]
	else:
		all_lsts = []
		for i in range(0, len(lst)):
			a = lst[:i] + lst[(i+1):]
			b = lst[i]
			c = all_orderings(a)
			for sublst in c:
				all_lsts = all_lsts + [[b] + sublst]
		return all_lsts

# Works efficiently for up to 7 vertices
def brute_force_paths(lst, matrix):
	if len(lst) <= 8:
		a_o = all_orderings(lst)
		max_count = 0
		max_ordering = a_o[0]
		for ordering in a_o:
			count = count_forward_paths(ordering, matrix)
			if count > max_count:
				max_count = count
				max_ordering = ordering
		return max_count, ordering

#gives an approximation of the most efficient paths
#for lists of vertex orderings from sizes 7 to 49
def efficient_cycle_analysis_49(lst, matrix):
	#the first step is splitting up your original list into a bunch of lists of size 7
	lst_of_lsts = []
	i = 0
	while i < len(lst):
		lst_of_lsts.append(list(lst[i:(i + 7)]))
		i += 7
	#next we are going to find the optimal ordering for each sublist of size 7. 
	i = 0
	while i < len(lst_of_lsts):
		lst_of_lsts[i] = brute_force_paths(lst_of_lsts[i], matrix)
		i += 1
	#now, we will abstract away the groups of 7, and do all 7! orderings of our lists 
	j = 0
	orders = all_orderings(lst_of_lsts)
	max_ordering = flatten(orders[0])
	max_count = 0
	for order in orders:
		l = count_forward_paths(flatten(order), matrix)
		if l > max_count:
			max_count = l
			max_ordering = flatten(order)
	return max_ordering

def efficient_cycle_analysis(lst, matrix):
	if len(lst):
		return efficient_path_analysis(lst, matrix)
	else:
		lst_of_lsts = []
		i = 0
		while i < len(lst):
			lst_of_lsts.append(list(lst[i:(i + 49)]))
			i += 49
		i = 0
		while i < len(lst_of_lsts):
			lst_of_lsts[i] = brute_force_paths(lst_of_lsts[i], matrix)
			i += 1

















if __name__ == '__main__':
	# topological_sort([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
	# graph = [
	# 	[0, 1, 1, 1, 0],
	# 	[0, 0, 1, 0, 0],
	# 	[0, 0, 0, 1, 0],
	# 	[0, 0, 0, 0, 1],
	# 	[1, 0, 0, 0, 0]
	# ]
	# print(bellman_ford(graph, 0))
	# print(all_orderings([1,2, 3, 4, 5, 6, 7, 8]))
	# print(brute_force_paths([6,5,4,3,2,1,0], [[0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0]]))
	print(all_orderings_flatten([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]))
	# print(efficient_cycle_analysis_49([0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [[0, 0, 0, 1, 1, 0, 0], [0, 1, 0, 1, 1, 0, 1]]))
							
