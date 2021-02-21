# getting input
a = int(input("\nEnter a: "))
b = int(input("\nEnter b: "))
c = int(input("\nEnter c: "))

# formula
D = (b**2) - (4*(a*c))

print("\nD =",D)

# checking conditions
if D == 0:
    print("\nTwo real solutions")
elif D > 0:
    print("\nOne real solution")
else:
    print("\nComplex solution")
