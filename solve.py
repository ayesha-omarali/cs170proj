import utils, SCCMaker, functions, scorer_single

def solve(file):
    if file.endswith('.in'):
        mat = utils.read_matrix(file)
        sccmaker = SCCMaker.SCCMaker(mat)
        sccDag = sccmaker.Kosarajus()
        print("BRO")
        print(sccDag)
        sorted = functions.topological_sort(sccDag)
        solutionlist = []
        if(sorted is None):
            sorted = sccDag
        for s in sorted:
            print(s)
            ordering = functions.efficient_cycle_analysis(s, mat)
            print(ordering)
            solutionlist.extend(ordering)
        filenum = file[:-3]
        solname='solcheck'
        sol = open(solname, 'wb')
        stringsol = ' '.join(map(str,solutionlist))
        sol.write(input(stringsol))
        sol.close()
        scorestring = scorer_single.processTest(file, solname)
        print(scorestring)
        
solve('instances/9.in')