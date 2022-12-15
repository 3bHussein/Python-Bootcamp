print("welcome to the tip calculator")
total = float(input("what was the total bill?"))
tip = int(input("what is the percentage tip would you like to give ? 10,12,or 15 ?"))
person = int(input("how many people to splits the bill?"))
total_and_tip = (total*tip/100)+total
each_person_pay = round(total_and_tip/person, 2)
print(f"Each person should pay : ${each_person_pay}")
