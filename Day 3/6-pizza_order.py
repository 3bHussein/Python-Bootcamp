print("Welcome to python pizza order Deliverers")

size = input("what is size do you want ?S ,M ,L")
add_pepperoni = input("Do you want add pepperoni?Y ,N")
extra_cheese = input("Do you want to add Extra Cheese?Y ,N")
Bill=0
if size == "S":
    Bill += 7
elif size == "M":
    Bill += 12
elif size == "L":
    Bill += 15



if add_pepperoni == "Y":
    if size == "S":
     Bill += 2
    else:
         Bill += 3
if extra_cheese== "Y" :
  Bill += 1


else:
    print("please Try Again ")

print(f"your total bill is :{Bill} :)")
