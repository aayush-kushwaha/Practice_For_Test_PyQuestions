# WAP_to_check_whether_the_string_has_vowels_or_not
a = input("Enter String: ") # Asking input from user
i = 0 # Initialising a looping variable
while i < len(a): # if i < len(a) then the loop runs
    if a[i] in "AEIOUaeiou": # checking the character of string index by index. If any index value is in "AEIOUaeiou" then it will be a vowel
        print(a[i], "is a Vowel") # Printing a[i] index + "is a Vowel" till loop runs
    else:
        print(a[i],"is not a Vowel") # Printing a[i] index + "is not a Vowel" till loop runs
    i = i + 1 # Updation of looping variable. If it is not done then it will stuck in infinite loop