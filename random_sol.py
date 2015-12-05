import random, os
import utils, scorer_single

def randsolutions(instancedir):
    files = os.listdir(instancedir)
    notopened = []
    bestfiles = ['0']*len(files)
    bestfiles_score = ['0']*len(files)
    for f in files:
        if f.endswith('.in'):
            try:
                mat = utils.read_matrix(os.path.join(instancedir, f))
                filenum = f[:-3]
                length = len(mat)
                randlist = range(1, length+1)
                # Try random list 100 times
                top_score = -1
                top_score_str=''
                randsol=[]
                for i in range(150):
                    randsol=random.sample(randlist,len(randlist))
                    #reverselist = list(reversed(randlist))
                    solname='sol'+filenum
                    sol = open(solname, 'wb')
                    stringsol = ' '.join(map(str,randsol))
                    sol.write(stringsol)
                    sol.close()
                    scorestring = scorer_single.processTest(os.path.join(instancedir,f), solname)
                    score=float(scorestring[18:])
                    if score<0.2:
                        randsol=list(reversed(randsol))
                        score=1-score
                        stringsol = ' '.join(map(str,randsol))
                    if score>top_score:
                        top_score=score
                        top_score_str = stringsol
                    # Save time
                    if score>0.92:
                        break
                bestfiles[int(filenum)] = top_score_str
                bestfiles_score[int(filenum)] = top_score
                os.remove(solname)
            # Couldn't read the input file; error with utils.read_matrix
            except:
                notopened.append(f)
    finalsol = open('finalsol.out', 'wb')
    for b in bestfiles:
        finalsol.write(b)
        finalsol.write("\n")
    finalsol.close()
    finalsol_score = open('finalsol_score.out', 'wb')
    for b in bestfiles_score:
        finalsol_score.write(str(b))
        finalsol_score.write("\n")
    finalsol_score.close()
    return notopened
  
t = randsolutions('/cygdrive/c/Users/sam.holladay/Downloads/phase1/instances')
print t


def readlist(instancedir):
    files = os.listdir(instancedir)
    bestfiles_score = ['0']*len(files)
    finalsol = open('finalsol.out', 'wb')
    bestfiles = f.read().splitlines()
    for f in files:
        if f.endswith('.in'):
            try:
                mat = utils.read_matrix(os.path.join(instancedir, f))
                filenum = f[:-3]
                length = len(mat)
                solname='solcheck'
                sol = open(solname, 'wb')
                sol.write(bestfiles[int(filenum)])
                sol.close()
                scorestring = scorer_single.processTest(os.path.join(instancedir,f), solname)
                score=float(scorestring[18:])
                bestfiles_score[int(filenum)] = score
            except:raise
    finalsol_score = open('finalsol_score.out', 'wb')
    for b in bestfiles_score:
        finalsol_score.write(str(b))
        finalsol_score.write("\n")
    finalsol_score.close()
    
#x=readlist('/cygdrive/c/Users/sam.holladay/Downloads/phase1/instances')