my_tuple = tuple(range(1,11,1))
total = 0
i = 0
while i < len(my_tuple):
    total += my_tuple[i]
    i += 1

print("My tuple:\n",my_tuple)
print("\n Sum of My tuple=",total)

