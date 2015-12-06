import os, random, scorer_single, utils, SCCMaker


"""randsol=[]
for i in range(8000):
    randsol=random.sample(randlist,len(randlist))
    #reverselist = list(reversed(randlist))
    solname='soltrywa'
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
"""

"""mat_ordered = {}
# Fill a dictionary with the total number of outgoing edges 
for i in range(len(mat)):
    total = 0
    for j in mat[i]:
        total += j
    mat_ordered[i] = total
sorted_x = sorted(mat_ordered.items(), key=operator.itemgetter(1))
solutions = [i[0] for i in list(reversed(sorted_x))]"""
def solve(filename):
    filenum = filename[:-3]
    stringsol = '0'
    score = 0.0
    try:
        mat = utils.read_matrix(filename)
        #randlist = range(1, len(mat)+1)
        #top_score = -1
        #top_score_sol=''
        sccmaker = SCCMaker.SCCMaker(mat)
        solutions = sccmaker.do_dfs()
        stringsol = ' '.join(map(str,solutions))
        solname='soltrywa'
        solfile = open(solname, 'wb')
        solfile.write(stringsol)
        solfile.close()
        scorestring = scorer_single.processTest(filename, solname)
        score=float(scorestring[18:])
        if score <0.5:
            solutions = list(reversed(solutions))
            stringsol = ' '.join(map(str,solutions))
            score = 1-score
    except ValueError: 
        print filename 
    except ZeroDivisionError: 
        print filename
    return (stringsol, score)
   
def solve_all_files():
    instancedir = 'instances'
    files = os.listdir(instancedir)
    notopened = []
    lengthf = len(files) +1
    bestfiles = ['0']*lengthf
    bestfiles_score = ['0']*lengthf
    count = 0.0
    for f in files:
        filenum = f[:-3]
        (stringsol, score) = solve(os.path.join(instancedir, f))
        bestfiles[int(filenum)] = stringsol
        bestfiles_score[int(filenum)] = str(score)
        count += score
    average_count = count/len(files)
    finalsol = open('solutions_greedy.out', 'wb')
    newline = "\n"
    for b in bestfiles:
        finalsol.write(b.encode('utf-8'))
        finalsol.write(newline.encode('utf-8'))
    finalsol.close()
    finalsol_score = open('score_greedy.out', 'wb')
    for b in bestfiles_score:
        bstr = str(b)
        finalsol_score.write(bstr.encode('utf-8'))
        finalsol_score.write(newline.encode('utf-8'))
    finalsol_score.close()
    return average_count
        
#print solve_all_files()
#print solve('instances/613.in')

def get_solutions(mat):
    ln = len(mat)+1
    scorelist = ['0']*ln
    for i in range(len(mat)):
        solname='soltrywa'
        solfile = open(solname, 'wb')
        solfile.write(mat[i])
        solfile.close()
        instance = 'instances/' + str(i+1) + '.in'
        try:
            scorestring = scorer_single.processTest(instance, solname)
            score=float(scorestring[18:])
            scorelist[i] = str(score)
        except ZeroDivisionError:
            scorelist[i] = '0'
    return scorelist
        

def merge_files():
    f1 = open('TeamApolloJainEyre.out', 'rb')
    f2 = open('solutions_greedy.out', 'rb')
    f3 = open('score_greedy.out', 'rb')
    oldsol = f1.read().splitlines()
    newsol = f2.read().splitlines()
    new_scores = f3.read().splitlines()
    old_scores = get_solutions(oldsol)
    print old_scores[107]
    print old_scores[204]
    print old_scores[441]
    
    ln = len(oldsol)+1
    bestsol = ['0']*ln
    bestscore = ['0']*ln
    count = 0.0
    for i in range(len(oldsol)):
        if new_scores[i] > old_scores[i]:
            bestsol[i] = newsol[i]
            bestscore[i] = new_scores[i]
        else:
            bestsol[i] = oldsol[i]
            bestscore[i] = old_scores[i]
        count += float(bestscore[i])
    average_count = (count+ float(old_scores[107]) + float(old_scores[204]) + float(old_scores[441]))/len(oldsol)
    """finalsol = open('solutions_merged.out', 'wb')
    newline = "\n"
    for b in bestsol:
        finalsol.write(b.encode('utf-8'))
        finalsol.write(newline.encode('utf-8'))
    finalsol.close()
    finalsol_score = open('score_merged.out', 'wb')
    for b in bestscore:
        finalsol_score.write(b.encode('utf-8'))
        finalsol_score.write(newline.encode('utf-8'))
    finalsol_score.close()"""
    return average_count
    
print merge_files()