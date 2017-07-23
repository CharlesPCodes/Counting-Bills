dollar = int(input ("How many $1 bills do you have?: ")or "0")
five = int(input ("How many $5 dollar bills do you have?: ")or "0")
ten = int(input ("How many $10 dollar bills do you have?: ")or "0")
twenty = int(input("How many $20 dollar bills do you have?: ")or "0")
fifty = int(input ("How many $50 dollar bills do you have?: ") or "0")
hundred = int(input("How many $100 dollar bills do you have?: ") or "0")

total = dollar * 1 + five * 5 + ten * 10 + twenty * 20 + fifty * 50 + hundred * 100
print ("Your total is: %s" %total)