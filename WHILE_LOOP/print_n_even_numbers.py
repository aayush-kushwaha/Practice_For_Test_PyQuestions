#WAP_to_print_the_series_of_n_even_numbers.
n = int(input("Enter number of series till where you want to print the square of number: ")) # Taking input from user
i = 0 # Initialising a looping variable
while i <= n: # if i is less than or equals to n then the loop will run
    if i % 2 == 0: # checking whether the number is even or not. In this case it will start with 0 as the value of i is 0
        print(i, "is even") # Printing even
    else:
        print(i, "is odd") # Printing odd
    i += 1 # Updation of looping variable. If it is not done then it will stuck in infinite loop