print("interation assignment")
sumsq  = 0
integer = 4
while integer <=8:
    integer = integer + 1
    sumsq = sumsq + integer ** 2
    print(integer, sumsq)
print(sumsq)
   
print("Problem 2")
sumsq = 0
index = 5
end = 10
for index in range(end):
    if (index > 4 and index <10):
        sumsq = (index ** 2) + sumsq
        print(index, sumsq)
        index+= 1
    print(sumsq) 

print("Problem 3")
sumsq = 0
index = 5
end = 10
for index in range(index,end):
    sumsq = (index ** 2) + sumsq
    print(index, sumsq)
    index+= 1 
print(sumsq)

print("Problem 4")
sumsq = 0
index = 5
end = 10
for index in range(index,end):
    if index == 7:
        continue
    sumsq = (index ** 2) + sumsq
    print(index, sumsq)
    index+= 1 
print(sumsq)

print("Problem 5") 
sumsq = 0
index = 5
end = 100
for index in range(index,end):
    if index == 10:
        break
    sumsq = (index ** 2) + sumsq
    print(index, sumsq)
    index+= 1 
print(sumsq)