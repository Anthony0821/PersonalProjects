ASet = {
    "cat",
    "dog",
    "parrot"
}
AList = [
    "cat",
    "dog",
    "parrot"
]
ATuple = (
    "cat",
    "dog",
    "parrot"
)
print(type(AList))
print(type(ATuple))
print(type(ASet))
#print(AList[0])
#print(ASet[0])
#print(ATuple[0])

BSet = {
    
    "dog",
    "parrot",
    "cat"
}
BList = [
    
    "dog",
    "parrot",
    "cat"
]
BTuple = (
    
    "dog",
    "parrot",
    "cat"
)
print(AList == BList)
print(ASet == BSet)
print(ATuple == BTuple)
CSet = {
    
    "dog",
    "parrot",
    "cat",
    "dog"
}
CList = [
    
    "dog",
    "parrot",
    "cat",
    "dog"
]
CTuple = (
    
    "dog",
    "parrot",
    "cat",
    "dog"
)
print(len(CSet))
print(len(CTuple))
print(len(CList))

Pets_dict  = {"Dog": 2, "cat" : 1, "parrot": 0}
Pets_Set = { "Fido", "Rover", "Felix"}

Pets_dict["python"] = 1
Pets_Set.add("Cool guy")

Pets_Set.discard("Felix")
Pets_dict.pop("cat")
sorted_pets = sorted(Pets_Set)
print(type(sorted_pets))
print(Pets_dict)
print(Pets_Set)

def undup(list):
    unduplicated = set(list)
    return(unduplicated)

test = [1,1,2,3,4,4,5,1,2,6]
print(undup(test))



    