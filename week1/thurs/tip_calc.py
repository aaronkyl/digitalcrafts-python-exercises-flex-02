quality_of_service = ["good", "fair", "bad"]
level_of_service = ""

total = float(input("Total bill amount? "))

while not level_of_service:
    level_of_service = input("Level of service? ").lower()
    if level_of_service not in quality_of_service:
        level_of_service = ""

if level_of_service == "good":
    tip = total * .2
elif level_of_service == "fair":
    tip = total * .15
else:
    tip = total * .1
    
print("Tip amount: ${:.2f}".format(tip))
print("Total amount: ${:.2f}".format(total + tip))
