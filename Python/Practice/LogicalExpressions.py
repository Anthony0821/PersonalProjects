"""TV = [True, False]
for p in TV:
    for q in TV:
        print(not (p and q), (not p) or (not q))"""
    
TV = [True, False]   
exp1 = []
exp2 = []

'''print(exp1 == exp2)'''

def compare (f,g):
    TV = [True, False]
    exp1= []
    exp2 = []
    
    for p in TV:
        for q in TV:
            exp1.append(f(p,q))
            exp2.append(g(p,q))
            
    if exp1 == exp2:
        conclusion = " yes - equivalent"

    else: 
        conclusion = "no - not equivalent"
    
    return conclusion

def f1(a,b):
    return not a and not b

def f2(c,d):
    return not(c or d)

print(compare(f1,f2))