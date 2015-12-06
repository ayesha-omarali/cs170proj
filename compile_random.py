"""f1= open('finalsol.out', 'r')
final = f1.read().splitlines()
f2 = open('finalsol_score.out', 'r')
finalsol_score = f2.read().splitlines()
f3 = open('finalsol2.out', 'r')
finalsol2 = f3.read().splitlines()
f4= open('finalsol_score2out', 'r')
finalsol_score2 = f4.read().splitlines()
bestfiles = ['0']*len(final)
bestfiles_score = ['0']*len(final)
print len(bestfiles)
for i in range(len(final)):
    if finalsol_score[i] > finalsol_score2[i]:
        bestfiles[i] = final[i]
        bestfiles_score[i] = finalsol_score[i]
    else:
        bestfiles[i] = finalsol2[i]
        bestfiles_score[i] = finalsol_score2[i]
f5= open('random_sol.out', 'wb')
f6= open('random_solscore.out', 'wb')
for b in bestfiles:
    f5.write(b)
    f5.write("\n")
for b in bestfiles_score:
    f6.write(str(b))
    f6.write("\n")
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
"""
import random, os

import utils, scorer_single
t = {18:27, 100:100}
bestfiles = ['0']*102
bestfiles_score = ['0']*102
for key, value in t.iteritems():
    randlist = range(1, value+1)
    # Try random list 100 times
    top_score = -1
    top_score_str=''
    randsol=[]
    for i in range(400):
        randsol=random.sample(randlist,len(randlist))
        #reverselist = list(reversed(randlist))
        solname='sol'+str(key)
        sol = open(solname, 'wb')
        stringsol = ' '.join(map(str,randsol))
        sol.write(stringsol)
        sol.close()
        instance = '/cygdrive/c/Users/sam.holladay/Documents/GitHub/cs170proj/instances/' + str(key) + '.in'
        score = 0.0
        try:
            scorestring = scorer_single.processTest(instance, solname)
            score=float(scorestring[18:])
        except: pass
        if score<0.2:
            randsol=list(reversed(randsol))
            score=1-score
            stringsol = ' '.join(map(str,randsol))
        if score>top_score:
            top_score=score
            top_score_str = stringsol
        # Save time
    bestfiles[key] = top_score_str
    bestfiles_score[key] = top_score
    os.remove(solname)
finalsol = open('finalsolforget.out', 'wb')
for b in bestfiles:
    finalsol.write(b)
    finalsol.write("\n")
finalsol.close()
finalsol_score = open('finalsol_scoreforget.out', 'wb')
for b in bestfiles_score:
    finalsol_score.write(str(b))
    finalsol_score.write("\n")
finalsol_score.close()