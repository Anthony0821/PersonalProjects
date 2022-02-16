from re import T


t1 = 1,2,3
t2 = (1,2,3)
z = t1[-1] #Negative values start at the end of the variable 
t3 = ("a", 'b', 'c,')

List1 = [1,2,3]
list2 = [4, 5, 6]
l1 = list(t1)
l1.append(23)

tt = tuple(l1)


def tsort(t):
    temp = list(t)
    temp.sort()
    tout = tuple(temp)
    return(tout)

ta = (5,4,12,11)


first, second, third,forth = ta

def  LCDV(x , y):
    minVal,maxVal = None, None
    
    for i in range(2, min(x, y) + 1):
        
        if x % i == 0 and y % i == 0:
            
            if minVal == None or i < minVal:
                minVal = i
                
            if maxVal == None or i > maxVal:
                maxVal = i
                
    return(minVal, maxVal)

lcd, gcd = LCDV(27, 18)
print(lcd)

   