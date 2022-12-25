height = float(input("enter your height in cm"))
age = int(input("enter your age "))
if height > 120:
    if age < 12:
        print('your age is ', age)
        print("you will pay 7$")
    elif age ==12 &age <18:
        print("you will pay 8$")
    
    elif age >=45 & age <55:
        print("you want pay 0$")
    else:
        print("you will pay 12$")
else:
    print("please try again ")
