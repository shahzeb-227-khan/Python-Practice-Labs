# code 1
def cal():
    cal = int(input("enter the number of calories: "))
    fats = int(input("enter the fats in your food: "))
    cal_from_fats = fats * 9
    per_cal = cal_from_fats / cal
    if cal<0 or fats<0:
        print("Invalid input: calories or fats can not be less than 0: ")
    elif cal < cal_from_fats:
        print("Invalid input: calories from fats cannot be greater than total calories")
    elif per_cal < 0.3:
        print("your food is low in fats which is",per_cal*100,"%")
    else:
        print("Percentage of calories from fats is: ",per_cal*100,"%")
x = input("enter your food:")
cal()
