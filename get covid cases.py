from covid import Covid

corona = Covid()
cont = input("Enter the country name: ")
case = corona.get_status_by_country_name(cont)

for cont in case:
    print(cont,":",case[cont])
