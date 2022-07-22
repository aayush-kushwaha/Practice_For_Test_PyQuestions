'''
WAP to get the following output:
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
'''
m = 5 # Taking variable with value 5
i = 1 # Initialising a looping variable
while i <= m: # If i is less than or equals to m (i.e. 5) then the loop runs 
    print("5","*",i,"=",m*i) # Here, print("5","*",i,"=",m*i) means printing 5 * i = m*i and it will execute till loop condition satisfies
    i += 1 # Updation of looping variable. If it is not done then it will stuck in infinite loop
