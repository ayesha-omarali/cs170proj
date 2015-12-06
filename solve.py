import utils, SCCMaker, functions, scorer_single

def solve(file):
    if file.endswith('.in'):
        mat = utils.read_matrix(file)
        ordering = functions.efficient_cycle_main(range(0, len(mat)), mat)[1]
        print("ORDERING")
        print(ordering)
        print("END ORDERING")
        solutionlist= ordering
        filenum = file[:-3]
        solname ='solcheck'
        sol = open(solname, 'wb')
        stringsol = ' '.join(map(str,solutionlist))
        print(stringsol)
        sol.write(stringsol.encode('utf-8'))
        sol.close()
        scorestring = scorer_single.processTest(file, solname)
        

import os

def solutions():
    instancedir = 'instances'
    files = os.listdir(instancedir)
    notopened = []
    bestfiles = ['0']*len(files)
    bestfiles_score = ['0']*len(files)
    for i in range(20):
        f = str(i) + ".in"
        if f.endswith('.in'):
            try:
                (stringsol, scorestrin) = solve(os.path.join(instancedir,f))
                filenum = f[:-3]
                score=float(scorestring[18:])
                bestfiles[int(filenum)] = stringsol
                bestfiles_score[int(filenum)] = score
            except:
                notopened.append(f)
    finalsol = open('finalsolapollo.out', 'wb')
    newline = "\n"
    for b in bestfiles:
        finalsol.write(b.encode('utf-8'))
        
        finalsol.write(newline.encode('utf-8'))
    finalsol.close()
    finalsol_score = open('scoreapollo.out', 'wb')
    for b in bestfiles_score:
        bstr = str(b)
        finalsol_score.write(bstr.encode('utf-8'))
        finalsol_score.write(newline.encode('utf-8'))
    finalsol_score.close()
    return notopened
    
t= solutions()
print(t)
