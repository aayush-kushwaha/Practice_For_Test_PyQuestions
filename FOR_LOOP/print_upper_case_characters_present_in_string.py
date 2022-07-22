# WAP to print all the uppercase character present in a given string
s = 'pRogRAMmIng'
for i in s:
    if "A" <= i <= "Z":
        print(i)



# Another method
'''
for i in range(len(s)):
    if "A" <= s[i] <= "Z":
        print(s[i])
'''


# Extracting(It will give output in 1 line)
'''
st = ''
for i in s:
    if "A" <= i <= "Z":
        st += i
print(st)
'''