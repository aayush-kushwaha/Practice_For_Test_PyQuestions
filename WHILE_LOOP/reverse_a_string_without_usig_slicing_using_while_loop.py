# WAP to reverse  string without using slicing andby using while loop
st = input("Enter a string: ")
i = 0
out = ''
while i < len(st):
    out = st[i] + out
    i += 1
print(out)


# a = st[::-1]
# print(a)