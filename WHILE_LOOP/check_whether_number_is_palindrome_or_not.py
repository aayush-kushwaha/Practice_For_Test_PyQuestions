# WAP to check whether the number is palindrome or not without using typecasting
a = input("Enter a number: ") # Taking input from user
i = 0 
rev = ""
while i < len(a):
    rev = a[i] + rev
    i += 1
if rev == a:
    print("Palindrome")
else:
    print("Not Palindrome")