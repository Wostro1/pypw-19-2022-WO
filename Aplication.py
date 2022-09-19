def calculate_bmi(weight, height):
    bmi = weight/height**2

    result = None
    if bmi < 18.5:
        result = "Underweight"
    elif bmi > 25:
        result = "Overweight"
    return "Normal"

if __name__ == "__main__":
    weight = float(input("weight: "))
    height = float(input("height: "))
    result = calculate_bmi(weight,height)
    print(result)

