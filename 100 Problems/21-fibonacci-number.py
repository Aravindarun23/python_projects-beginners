n1 = 0
n2 = 1

# geetting input
num = int(input("How many: "))

for i in range(0,num):
    print(n1)
    t = n1 + n2
    n1 = n2
    n2 = t
