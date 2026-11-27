vehicle =int(input("enter vehicle type :"))
hour = float(input("enter no of hours:"))
if vehicle== 2:
    fee=hour*20
elif vehicle == 4:
    fee = hour * 50
elif vehicle>4:
    fee = hour *100
else :
    fee=0
    print("invalid vehicle")
print("Vechile type:",vehicle)
print("No of hour:",hour)
print("Total fees:",fee) 

print("Thank you for using our service")
