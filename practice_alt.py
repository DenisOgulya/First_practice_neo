
def try_getting_number_from_user(prompt):
    while True:  
        try:
            weekly_budget = float(input(prompt))
           # print("Entered correct value")
            return weekly_budget
        except ValueError:
            print("Please enter a new value, this one is wrong")
        
print("end of programm")

# while True:  
#     try:
#         weekly_budget = float(input("Please enter budget for the week: "))
#         print("Entered correct value")
#         break
#     except ValueError:
#         print("Please enter a new value, this one is wrong")
        
# print("end of programm")


# weekly_budget = try_getting_number_from_user("Please enter budget for the week: ")
# print(f"Budget for the week is: {weekly_budget}")
# #Monday
# monday_spend = try_getting_number_from_user("Please enter budget for the Monday: ")
# print(f'Budget for the Monday is: {monday_spend}')
# #Tuesday
# tuesday_spend = try_getting_number_from_user("Please enter budget for the Tuesday: ")
# print(f'Budget for the Monday is: {tuesday_spend}')

#Wednesday
# wednesday_spend = try_getting_number_from_user("Please enter budget for the Wednesday: ")
# print(f'Budget for the Monday is: {wednesday_spend}')

money_spend_during_the_week = []
#Monday
money_spend_during_the_week.append(try_getting_number_from_user("Please enter budget for the Monday: "))
#Tuesday
money_spend_during_the_week.append(try_getting_number_from_user("Please enter budget for the Tusday: "))
#Wednesday
money_spend_during_the_week.append(try_getting_number_from_user("Please enter budget for the Wednesday: "))

print(money_spend_during_the_week)