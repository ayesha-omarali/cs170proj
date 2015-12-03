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



topological_sort([[0, 0, 1], [0, 0, 0], [0, 0, 0]])
graph = [
	[0, 1, 1, 1, 0],
	[0, 0, 1, 0, 0],
	[0, 0, 0, 1, 0],
	[0, 0, 0, 0, 1],
	[1, 0, 0, 0, 0]
]
print(bellman_ford(graph, 0))
							
