import utils, SCCMaker, functions, scorer_single

def solve(file):
    if file.endswith('.in'):
        mat = utils.read_matrix(file)
        sccmaker = SCCMaker.SCCMaker(mat)
        sccDag = sccmaker.Kosarajus()
        sorted = functions.topological_sort(sccDag)
        solutionlist = []
        print(sorted)
        for s in sorted:
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
        
solve('/cygdrive/c/Users/sam.holladay/Downloads/phase1/instances/9.in')