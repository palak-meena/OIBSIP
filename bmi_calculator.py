
try:
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be greater than zero.")

    else:
        bmi = weight / (height * height)

        print("Your BMI is:", round(bmi, 2))

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Error: Please enter numbers only.")
