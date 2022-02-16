personWeight = {
    "Joe":175,
    "Tom":190,
    "Dick": 150
}

personWeight["Harry"] = 180
personWeight.pop("Joe")


sum = 0
for x in personWeight.values():
    sum = x + sum
    #print(sum)
    
rti = personWeight.items()
#print(rti)
#print(type(rti))


    #print(x)
    


rti_1 = list(rti)
print(rti_1)
print(rti_1[0])
        