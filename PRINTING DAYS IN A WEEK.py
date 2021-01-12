# start of the program
print("\n==== PRINTING DAYS IN A WEEK")

def PDIW():
    # getting input
    code = int(input("\nENTER THE CODE: "))

    # checking condition
    if code == 1:
        print("\nMONDAY")
    elif code == 2:
        print("\nTUESDAY")
    elif code == 3:
        print("\nWEDNESDAY")
    elif code == 4:
        print("\nTHURSDAY")
    elif code == 5:
        print("\nFRIDAY")
    elif code == 6:
        print("\nSATURDAY")
    elif code == 7 or code == 0:
        print("\nSUNDAY")
        
    # for handling Errors
    else:
        print("\nENTER THE CORRECT CODE\nFROM 0 TO 7")
        PDIW()

PDIW()
print("\n==== PROGRAM ENDS")
