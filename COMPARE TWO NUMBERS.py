# starting of the program
print("\n==== COMPARING TWO NUMBERS")

# geting input
getInp1 = int(input("\nENTER FRIST NUMBER: "))
getInp2 = int(input("\nENTER SECOND NUMBER: "))

# checking condition
if getInp1 == getInp2:
    print("\n",getInp1, "and", getInp2, "are EQUAL")
    
elif getInp1 > getInp2:
    print("\n",getInp1, "is greater than", getInp2)
    
else:
    print("\n",getInp1, "is less than", getInp2)
    
print("==== PROGRAM ENDS")
