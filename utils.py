def read_matrix(filename):
    f = open(filename, 'r')
    matrix = f.read().splitlines()
    matrix.pop(0)
    t = []
    for i in matrix:
       last = len(i)-1
       if i[last] == ' ':
           i = i[:-1]
       t.append(map(int, i.split(' ')))
    return t