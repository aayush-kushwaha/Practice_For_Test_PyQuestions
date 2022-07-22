# WAP to find the sum of integer values present only at even index in a given heterogeneous collection.
h = ['apple',1,4,3,4+5j,True,6,7,6.5]
sum = 0
for i in range(len(h)):
    if i % 2 == 0:
        if type(i) == int:
            sum += i
print(sum)

#OR
'''
sum = 0
for i in range(len(h)):
    if i % 2 == 0 and type(i) == int:
        sum += h[i]
print(sum)
'''