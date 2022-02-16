from doctest import Example


hello = [1,2,3,4,5,6,7,1,2,2,2]
print(hello.count(2))



possibilities = []
i = 0 
for NH in "AC":
    for MN in "ABC":
        for WI in "AB":
            for CA in "ABC":
                i += 1
                outcome = (i,NH,MN,WI,CA)
                possibilities.append(outcome)
for i in possibilities:
    print(i)

Universe = set(possibilities)
Universe = sorted(Universe)



        

def counter(cand, outcome):
    result = outcome.count(cand)
    return result

test = ["A", "B", "C"]
result = []


def counter1(cand, outcome):
    count = 0
    for winner in outcome:
        if winner == cand:
            count += 1
    return count

Example1 = set()
for oc in Universe:
    if (counter1("B", oc) > counter("A", oc)) and (counter1("B",oc) > counter("C", oc)):
        Example1.add(oc)

for oc in sorted(Example1):
    print(oc)

Ex1a = set()
for OC in Universe:
    if counter("A", OC) == counter("C", oc):
        Ex1a.add(OC)

for OC in sorted(Ex1a):
    print(OC)