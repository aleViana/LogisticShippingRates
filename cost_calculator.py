#Shipping calculator

w = float(input("Enter the package weight in Kg: "))
rate = float(input("Enter rate per Kg: "))

#Calculation
shipping_cost = w * rate
#display
print(f"Cost: {shipping_cost} USD")
