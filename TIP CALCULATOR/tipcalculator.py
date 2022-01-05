print("Welcome to Tip Calculator")
bill = input("What is the total bill amount? $")
tip = input("What percentage tip would you like to give? 10% , 12% , 15% ?") 
tip_2 = (float(tip) / 100) * float(bill)
tip_1 = float(bill) + tip_2
num = input("How many people are gonna split the bill? ")
share =(tip_1 / float(num))
share_1 = round(share,2)
print("Each person should pay: $" + str(share_1))