def getInp():
    # geting input
    gradeInp = int(input("\nEnter Grade Points: "))

    # checking condition
    if gradeInp == 10:
        print("\nYour Grade: O (Outstanding)")
    elif gradeInp == 9:
        print("\nYour Grade: A+ (Excellent)")
    elif gradeInp == 8:
        print("\nYour Grade: A (Very Good)")
    elif gradeInp == 7:
        print("\nYour Grade: B+ (Good)")
    elif gradeInp == 6:
        print("\nYour Grade: B (Average)")
    elif gradeInp <=5 and gradeInp > -1:
        print("\nYour Grade: RA (Fail)")

        
    # Additional (For handling Incorrect Inputs)
    elif gradeInp <0:
        print("\nYour input is less than 0\nEnter Correct Grade Points")
        getInp()
    else:
        print("\nYour input is higher than 10\nEnter Correct Grade Points")
        getInp()

getInp()
