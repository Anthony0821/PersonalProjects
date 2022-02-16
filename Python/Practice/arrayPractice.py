li1 = ['hello']
li2 = ['world']
li3 = li1 + li2
li1.append(li2)

def undup(i):
    sep = list(dict.fromkeys(i))
    return(sep)

test = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
undup(test)

def numres(nl):
    conum = len(nl)
    sum = 0
    for x in nl:
        sum = sum + x
        print(x)
    avg = sum / conum
    return(conum, sum, avg)


xlist = [1,["a", "b",["x","y"]]]
print(xlist[1][2][1])