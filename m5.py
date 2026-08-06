# input and out funtion for concatanation
boy_name = input("Enter boy name: ")
boy_age = int(input("Enter boy age: "))
girl_name = input("Enter girl name: ")
girl_age = int(input("Enter girl age: "))
age_diff =boy_age - girl_age
print(boy_name + " loves " + girl_name + " and there age difference " + str(age_diff))

# formated string
print(f"{boy_name} loves {girl_name} and ther age difference is {age_diff}")
