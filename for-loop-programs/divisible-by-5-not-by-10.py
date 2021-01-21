# START OF THE PROGRAM
# print numbers divisible by 5 not by 10

# ===[ upto 100 ]===
print("Numbers Divisible by 5 and not by 10 (from 1 to 100)")
for i in range(1,101):
    if i % 5 == 0 and i % 10 != 0:
        print(i)
        
# END OF PROGRAM
