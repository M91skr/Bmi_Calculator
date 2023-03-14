"""---------------------------------------- BMI Calculator ----------------------------------------
This project is a **BMI Calculator**.
In this program, the user enters his weight in meters and his weight in kilograms. The user's BMI is calculated and the
user's fitness status and normal weight range are displayed.
"""

# ---------------------------------------- Get Information ----------------------------------------

height = float(input("Height(m): "))
weight = int(input("Weight(kg): "))

""" ---------------------------------------- Height Data Accuracy Check ----------------------------------------
There is a high possibility that users enter their height in centimeters by mistake, 
so this parameter is exclusively checked.
"""

if height > 3:
    raise ValueError("Human Height(m) should not be over 3 meters.")

# ---------------------------------------- Output Calculation ----------------------------------------

bmi = weight / (height ** 2)
bmi_min = 18.5 * (height ** 2)
bmi_max = 25 * (height ** 2)

# ---------------------------------------- Display Output ----------------------------------------

print(round(bmi, 2))
if bmi < 16:
    print("Severe Thinness")
elif bmi < 17:
    print("Moderate Thinness")
elif bmi < 18.5:
    print("Mild Thinness")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese Class I")
elif bmi < 40:
    print("Obese Class II")
elif bmi >= 40:
    print("Obese Class III")
print(f"Healthy weight for the height: {round(bmi_min, 2)} Kgs - {round(bmi_max, 2)} Kgs")
