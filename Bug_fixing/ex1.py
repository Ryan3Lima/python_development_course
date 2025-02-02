## ex1

#while True:
#    print("hello")

## ex2

#greeting = "hello"
#print(greeting.upper())

## ex3

countries = []
ask = True

while ask == True:
    country = input("Enter Country: ")
    countries.append(country)
    cont = input("would you like to enter another country? (Y/N)")
    cont1 = cont.capitalize()
    if cont1 == 'Y':
        ask = True
    elif cont1 == 'N':
        ask = False
    else:
        print("I did not understand that input please type 'Y' or 'N':   ")
        ask = True


print(countries)