#BMR

def bmr_bmi():
    name = input("Whats your name : ").upper()
    bmr_bmi = input("Whats you want to calculate : \n BMI/BMR: ").upper()
    gender = input("Your gender :\n M/F : " ).upper()

    if gender == "M" and bmr_bmi == "BMR":
        weight = float(input("Whats your  weight(KG) : "))
        height = float(input("whats your height(CM) : "))
        age = float(input("Whats your age :"))
        health_condition = input("Sedentary (little or no exercise) : (A) \n"
                                 "Lightly active (light exercise/sports 1-3 days a week):(B) \n"
                                 "Moderately active (moderate exercise/sports 3-5 days a week):(C)\n"
                                 "Very active (hard exercise/sports 6-7 days a week) :(D) \n"
                                 "Extra active (very hard exercise/sports and physical job or 2x training):(E) \n "
                                 "Choose A/B/C/D/E : ").upper()
        result = 66+(13.7*weight)+(5*height)-(6.8*age)
        if health_condition == "A":
            do = result*1.2
        elif health_condition == "B":
            do = result*1.375
        elif health_condition == "C":
            do = result*1.55
        elif health_condition == "D":
            do = result*1.725
        elif health_condition == "E":
            do = result*1.9
        else:
            print("Invalid input : ")
            return

        print(f"Hey {name}, your BMR result is {result} calories and you need {do}")
    elif gender == "F" and bmr_bmi == "BMR":
        weight = float(input("Whats your  weight(KG) : "))
        height = float(input("whats your height(CM) : "))
        age = float(input("Whats your age :"))
        health_condition = input("Sedentary (little or no exercise) : (A) \n"
                                 "Lightly active (light exercise/sports 1-3 days a week):(B) \n"
                                 "Moderately active (moderate exercise/sports 3-5 days a week):(C)\n"
                                 "Very active (hard exercise/sports 6-7 days a week) :(D) \n"
                                 "Extra active (very hard exercise/sports and physical job or 2x training):(E) \n "
                                 "Choose A/B/C/D/E : ").upper()
        result = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        if health_condition == "A":
            do = result*1.2
        elif health_condition == "B":
            do = result*1.375
        elif health_condition == "C":
            do = result*1.55
        elif health_condition == "D":
            do = result*1.725
        elif health_condition == "E":
            do = result*1.9
        else:
            print("Invalid input : ")
            return

        print(f"Hey {name}, your BMR result is {result} calories and you need {do} calories per day")
    elif bmr_bmi == "BMI":
        weight = float(input("Whats your  weight(kg) : "))
        height = float(input("whats your height(m) : "))
        bmi = weight/height**2
        if bmi < 18.5:
            print(f"Your BMI is {bmi} :\n"
                  "Underweight : BMI indicates below-normal body weight, which may warrant investigation into potential underlying health concerns")

        elif 18.5 < bmi > 24.9:
            print(f"Your BMI is {bmi} :\n"
                  "Normal weight: BMI falls within the healthy range, indicating a balanced body weight for height.")
        elif 25 < bmi > 29.9:
            print(f"Your BMI is {bmi} :\n"
                  "Overweight : BMI suggests excess body weight, highlighting the need for lifestyle changes to improve overall health.")
        elif 30 < bmi > 34.9:
            print(f"Your BMI is {bmi} :\n"
                  "First stage of obesity. Selective diet and exercise are necessary. ")

        elif 35 < bmi > 39.9:
            print(f"Your BMI is {bmi} :\n"
                  "2nd level of obesity. Moderate diet and exercise are necessary.")

        elif 40 < bmi :
            print(f"Your BMI is {bmi} :\n"
                  "Excess weight. Fear of death. A doctor's consultation is required.")
        else:
            print("Invalid Input")
            return
    else:
        print("Invalid Input")
        return

bmr_bmi()



