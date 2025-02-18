body_weight = float(input("enter your body weight:\n"))
conversion = body_weight / 2.2
rounding = conversion.__round__(3)
print(f"your body weight is:{body_weight} lbs and the equivalent in kg is {rounding} kg")
