num1 =float(input("Number ._.: "))
opertion = input("Operation ._.: ")
num2 = float(input("Other Number ._.: "))

if opertion == "+":
    result = num1 + num2
elif opertion == "-":
    result = num1 - num2
elif opertion == "*":
    result = num1 * num2
elif opertion == "/":
    result = num1 / num2
else:
    print("Invalid operation fuckin stupid ._.")

print( "the result is :D: " + str(result))