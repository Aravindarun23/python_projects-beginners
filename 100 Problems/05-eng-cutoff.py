# getting input
phy = int(input("Physics mark: "))
chem = int(input("Chemistry mark: "))
mat = int(input("Maths mark: "))

# formula
cutoff = (phy+chem) / 2 + mat

# printing output
print("\nYour Engineering cutoff =",cutoff)
