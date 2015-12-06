import utils, SCCMaker, functions, scorer_single

def solve(file):
    if file.endswith('.in'):
        mat = utils.read_matrix(file)
        sccmaker = SCCMaker.SCCMaker(mat)
        sccDag = sccmaker.Kosarajus()
        sorted = functions.topological_sort(sccDag)
        solutionlist = []
        if(sorted is None):
            sorted = sccDag
        for s in sorted:
            ordering = functions.efficient_cycle_main(s, mat)[1]
            solutionlist.extend(ordering)
        filenum = file[:-3]
        solname='solcheck'
        sol = open(solname, 'wb')
        stringsol = ' '.join(map(str,solutionlist))
        sol.write(stringsol.encode('utf-8'))
        sol.close()
        scorestring = scorer_single.processTest(file, solname)
        return (stringsol, scorestring)
        
#solve('instances/489.in')
import os

def solutions():
    instancedir = 'instances'
    files = os.listdir(instancedir)
    notopened = []
    bestfiles = ['0']*len(files)
    bestfiles_score = ['0']*len(files)
    for f in files:
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