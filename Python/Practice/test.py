from random import randint


a_list = []
b_list = []
c_list = []
for x in range(50):
    a_list.append(randint(0,250))
    b_list.append(randint(0,250))
    c_list.append(randint(0,250))
print(a_list)
print(b_list)
print(c_list)
set1 = set(a_list)
set2 = set(b_list)
set3 = set(c_list)

set4 = set1.union(set2)
print(set4)