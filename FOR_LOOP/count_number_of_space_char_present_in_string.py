# WAP to count the number of space characters present in a given string.
st = "East or West Python is the best"
space = 0
for i in st:
    if i == " ":
        space += 1
print(space)

# Another method
'''
st = "East or West Python is the best"
space = 0
for i in range(len(st)):
    if st[i] == " ":
        space += 1
print(space)
'''