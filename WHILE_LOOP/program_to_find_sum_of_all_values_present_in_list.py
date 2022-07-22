'''
WAP to find the sum of all the values present in a given homogeneous list using while loop.
'''
k = [1,2,3,4,5] # given homogeneous list
i = 0 # Initialising a looping variable
sum = 0 # Taking a dummy variable "sum" to store the sum value here during loop
while i < len(k): # if i is less then the length of k then the loop runs
    sum += k[i] # Adding k[i] value to dummy variable "sum"
    i += 1 # Updation of looping variable. If it is not done then it will stuck in infinite loop
print(sum) # Printing Sum
