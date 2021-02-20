# getting input
salary = int(input("Enter your salary: "))
year = int(input("Enter your year of service: "))

# checking years and printing bonus
if year >= 5:
    print("\nYour bonus is =",.05*salary)
else:
    print("\nSorry, You have just",year,"years of experience","\nSo No bonus for you")
    print("You need to work another",5-year,"years to get Bonus")
