
# Calculate Health Standards
def start():
    print("""
\nI will now be calculating your Body Mass Index (BMI),
the ideal weight for your age and gender, and also
approximating your Basic Metabolic Rate.
    """)

start()

# User Data
print("""
For the next 2 prompts, the 1st will ask for your height
in feet and then again in inches. ex) If I'm 5ft 9in, I
will first respond '5' and then '9' for the next prompt.\n
""")

height_ft = input("Height in feet: ")
height_in = input("Inches tall: ")
weight = input("Weight: ")
age = input("Age: ")
gender = input("Gender (M or F): ")
height = (int(height_ft)*12) + int(height_in)


# Body Mass Index
print("\n******RESULTS******")
bmi = 703*(int(weight)/int(height)**2)
bmi_output = round(bmi, 1)
if bmi <= 16:
    print(f"BMI: {bmi_output} = Severe thinness")

elif bmi <= 17:
    print(f"BMI: {bmi_output} = Moderate thinness")

elif bmi <= 18.5:
    print(f"BMI: {bmi_output} = Mild thinness")

elif bmi <= 25:
    print(f"BMI: {bmi_output} = Normal")

elif bmi <= 30:
    print(f"BMI: {bmi_output} = Obese: Class I")

elif bmi <= 35:
    print(f"BMI: {bmi_output} = Obese: Class II")

else:
    print(f"BMI: {bmi_output} = Obese: Class III")


# Ideal Weight
if gender == "M":
    male = 110.2+5*(int(height) % 12)
    print(f"Ideal Weight: {male}")

else:
    female = 100.3+5*(int(height) % 12)
    print(f"Ideal Weight: {female}")


# Basic Metabolic Rate
if gender == "M":
    male_bmr = round(10*int(weight)+6.25*int(height)-5*int(age)+5)
    print(f"BMR: {male_bmr}")

else:
    female_bmr = round(10*int(weight)+6.25*int(height)-5*int(age)-161)
    print(f"BMR: {female_bmr}")


print("\nThank you for using the Health Calculator!\n")
import accounts
accounts.options()
