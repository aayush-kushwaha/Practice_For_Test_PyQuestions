''' 
WAP to find sum of values present in a given list only if the values are even.
'''
k = [5,6,7,8,9,10] # Given list
i = 0 # Initialising a looping variable
sum = 0 # Taking a dummy variable "sum" to store the sum value here during loop
while i < len(k): # if i is less then the length of k then the loop runs 
    if k[i] % 2 == 0: # If k[i] index has remainder 0 or if it is even then the below True Statement Block will run
        sum += k[i] # Adding k[i] value to dummy variable "sum"
    else:
        pass # pass is a keyword used to keep empty block as a valid block without any error
    i += 1 # Updation of looping variable. If it is not done then it will stuck in infinite loop
print(sum) # Printing sum