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
        
solve('instances/9.in')