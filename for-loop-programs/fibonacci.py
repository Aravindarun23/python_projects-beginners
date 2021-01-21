# START OF THE PROGRAM
# fibonacci series first 10 numbers
first_num = 0
second_num = 1

for i in range(1,11):
    next_num  = first_num + second_num
    print(next_num)
    first_num = second_num
    second_num = next_num
    
# END OF THE PROGRAM


