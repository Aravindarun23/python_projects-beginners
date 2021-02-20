# generating  positive and negative numbers in a list
my_list = list(range(-10,11,1))
print("My list:\n",my_list)

# removing negative numbers
pos_num = []

for i in my_list:
    if i > 0:
        pos_num.append(i)

# converting list into tuple
pos_tuple = tuple(pos_num)

print("\nPositive numbers:\n",pos_tuple)
