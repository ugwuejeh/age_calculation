#age calculation application


current_year = 2023 #global variable
average_age = 18
name_of_student = input("enter name: --")

print(name_of_student)
def age_cal():
    age_calculation = int(input("enter years of birth: "))
    if age_calculation < 2006 :
     final_age = current_year - age_calculation
     print("Hello Skyline, your age is", final_age, "years2")
    else: 
     final_age = current_year - age_calculation
     print("sory you are", final_age, "years old, expected year is 18 and above")


age_cal()
