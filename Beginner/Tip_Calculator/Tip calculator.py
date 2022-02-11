print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would like to give? 10, 12 or 15? "))
num_people = int(input("How many people to split the bill? "))

tip = total_bill*(tip_percentage/100)
total_result = total_bill + tip
result = "{:.2f}".format(total_result/num_people,2)

print(f"Each person should pay: ${result}")