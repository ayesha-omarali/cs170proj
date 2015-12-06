import utils, functions, scorer_single, random

def solve(filename):
    if filename.endswith('.in'):
        print(filename)
        mat = utils.read_matrix(filename)
        ordering_intermediate = functions.efficient_cycle_main(range(0, len(mat)), mat)[1]
        ordering = [x + 1 for x in ordering_intermediate]
        print(ordering)
        solutionlist= ordering
        # filenum = file[:-3]
        # solname ='solcheck'
        # sol = open(solname, 'wb')
        # stringsol = ' '.join(map(str,solutionlist))
        # a = stringsol.encode('utf-8')
        # sol.write(a)
        # sol.close()

        print("im 1")
        filenum = filename[:-3]
        randlist = range(1, len(mat)+1)
                # Try random list 100 times
        top_score = -1
        top_score_sol=''
        randsol=[]
        for i in range(2000):
            randsol=random.sample(randlist,len(randlist))
            #reverselist = list(reversed(randlist))
            solname='solcheck'
            sol = open(solname, 'wb')
            stringsol = ' '.join(map(str,randsol))
            sol.write(stringsol)
            sol.close()
            scorestring = scorer_single.processTest(filename, solname)
            score=float(scorestring[18:])
            # if score<0.2:
            #     randsol=list(reversed(randsol))
            #     score=1-score
            #     stringsol = ' '.join(map(str,randsol))
            if score>top_score:
                top_score=score
                top_score_sol = stringsol
            # # Save time
            # if score>0.92:
            #     break

            randomsol_reverse = list(reversed(randsol))
            sol = open(solname, 'wb')
            stringsol_reverse = ' '.join(map(str,randomsol_reverse))
            sol.write(stringsol_reverse)
            sol.close()

            reverse_scorestring = scorer_single.processTest(filename, solname)
            reverse_score=float(scorestring[18:])

            if reverse_score > top_score:
                top_score > reverse_score
        print("im 3")
        solname='solcheck'
        sol = open(solname, 'wb')
        stringsol = ' '.join(map(str,solutionlist))
        sol.write(stringsol.encode('utf-8'))
        sol.close()
        print("checkpoint 5")
        scorestring = scorer_single.processTest(filename, solname) #messes up at this line
        score=float(scorestring[18:])
        if(score > top_score):
            top_score_sol = stringsol
            top_score = score
        final_scorestring = "solution value is %.4f" % top_score
        print((top_score_sol, final_scorestring))
        return (top_score_sol, final_scorestring)

        # print("HELP")
        # print(stringsol)
        # scorestring = scorer_single.processTest(file, solname)
        # print("HELP ME2")
        
        # return (stringsol, scorestring)
        

import os

def solutions():
    instancedir = 'instances'
    files = os.listdir(instancedir)
    notopened = []
    bestfiles = ['0']*len(files)
    bestfiles_score = ['0']*len(files)
    for f in ['101.in', '103.in', '108.in', '151.in', '169.in', '173.in', '196.in', '205.in', '218.in', '257.in', '272.in', '278.in', '280.in', '303.in', '324.in', '329.in', '339.in', '346.in', '358.in', '397.in', '409.in', '415.in', '421.in', '442.in', '533.in', '569.in', '571.in', '583.in', '613.in', '621.in', '66.in']:
        # f = str(i) + '.in'
        if f.endswith('.in'):
            try:
                intermediate = solve(os.path.join(instancedir,f))
                (stringsol, scorestring) = intermediate
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
