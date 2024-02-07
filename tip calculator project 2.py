print("welcome to tip calculator")
total_bill=int(input("enter total bill"))
tip=int(input("what percentage tip would you like to give?5,10,15 or 20 "))
person=int(input("How many people to split the bill"))
total_tip=(total_bill)*(tip/100)
final_bill=total_bill+total_tip
bill_per_person=final_bill/person
print(f"Each person should pay: {bill_per_person}")



