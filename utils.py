#this function reads the file into a matrix
def read_matrix(filename):
    f = open(filename, 'r')
    matrix = f.read().splitlines()
    matrix.pop(0)
    t = []
    for i in matrix:
       last = len(i)-1
       if i[last] == ' ':
           i = i[:-1]
       t.append(list(map(int, i.split(' '))))
    return t

def read_score(filename):
  f = open(filename, 'r')
  lst = f.read().splitlines()
  new_lst = [float(x) for x in lst]
  y = sum(new_lst)/(len(new_lst))
  return y

# print(read_score('scoreapollo.out'))