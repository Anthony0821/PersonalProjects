import math


a = 3 * math.pow(8, 2)



s  = "Hello, World!"
hardcode = (1 * 2 ** 7) + (1 * 2 ** 6) + (1 * 2 ** 5) + (1 * 2 ** 4) + (0 * 2 ** 3) + (1 * 2 ** 2) + (0 * 2 ** 1) + (1 * 2 ** 0)
print(hardcode)
def calcdecval(x):
    lenghtofx = len(x)
    int(lenghtofx)
    sum = 0
    for i in x:
        sum += int(i * (math.pow(2,len(x) - i)))
        
    print(sum)
    
calcdecval("11110101")