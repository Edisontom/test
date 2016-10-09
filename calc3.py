number1=float(input("Please enter first number:"))
action=str(input("Enter '+', '-', '*' or '/':"))
number2=float(input("Please enter second number:"))

calc = {
    "+": number1 + number2,
    "-": number1 - number2,
    "*": number1 * number2,
    "/": number1/number2


}

if calc == "/" and number2 ==0:
    print ("Error,  divide to '0'")
else:
    print(calc.get(action))

    
