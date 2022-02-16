def romanToInt(s: str) -> int:
    
    romandict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
                }
    sum = 0
    for x in s:
        if romandict.get[x] >= romandict.get[x]:
            sum += romandict.values[x]
        
    return sum

print(romanToInt("III"))