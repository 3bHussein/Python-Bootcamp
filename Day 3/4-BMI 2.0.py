height = float(input("enter your height\n"))
weight = float(input("enter your weight\n"))
# BMI = weight/(height**2)
# 30 obese
# 25 ~ 30 overweight
# 18.5 ~ 25 normal
# under 18 underweight

bmi = round (weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")


print("your BMI is :", bmi)

 