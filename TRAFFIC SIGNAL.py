# start of the program
print("\n==== TRAFFIC SIGNAL")

# getting input
def Taffic():
    getInp = int(input('''
The available signs

1) RED
2) ORANGE
3) GREEN

Choose your option: '''))

    # checking condition
    if getInp == 1:
        print("\nSTOP")
    elif getInp == 2:
        print("\nWAIT")
    elif getInp == 3:
        print("\nGO")
    else:
        print("\nChoose the correct option!!")
        Taffic()


Taffic()
print("\n==== PROGRAM ENDS")
