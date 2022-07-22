a = input("Enter String: ")
i = 0
while i < len(a):
    if a[i] in "AEIOUaeiou":
        print(a[i], "is a Vowel")
    else:
        print(a[i],"is not a Vowel")
    i = i +1
