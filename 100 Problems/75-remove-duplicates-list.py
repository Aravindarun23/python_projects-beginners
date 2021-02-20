my_list = [1,2,3,1,5,8,3,5,5,20,10,8,3,6,2,7]
org_list = []

for i in my_list:
    if i not in org_list:
        org_list.append(i)

print("My list:\n",my_list)
print("\nAfter removing Duplicates:\n",org_list)
