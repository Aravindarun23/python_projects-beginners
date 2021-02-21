#getting input
per = int(input("Your attendance percentage: "))

# checking conditions and printing results
if per >= 75:
    print("You're allowed to write exams")
elif per <= 75 and per >= 65:
    med = input("Do you have medical cause? ( Y / N ): ")
    if med == 'Y' or med == 'y':
        print("You're allowed to write exams")
    else:
        print("You're not allowed to write exams")
else:
    print("You're not allowed to write exams")
