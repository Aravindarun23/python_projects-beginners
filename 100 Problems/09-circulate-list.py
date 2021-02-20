# creating a list
my_list = list(range(10,101,10))
print("My list:",my_list)

# getting input
n = int(input("\nEnter number of times: "))

# formula
cir = my_list[n:] + my_list[:n]

# printing output
print("\nCirculated list:",cir)
