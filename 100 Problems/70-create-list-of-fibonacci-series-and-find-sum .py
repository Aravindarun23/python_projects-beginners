my_list = []
n1 = 0
n2 = 1
count = 0
sum = 0

num = int(input("How many: "))

# storing in a list
while count < num:
    my_list.append(n1)
    t = n1 + n2
    n1 = n2
    n2 = t
    count += 1
    
print("\nFibonacci series:",my_list)

# adding all numbers
for i in my_list:
    sum += i

print("\nSum of Fibonacci series is =",sum)


