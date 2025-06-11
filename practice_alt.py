
while True:  
    try:
        weekly_budget = float(input("Please enter budget for the week: "))
        print("Entered correct value")
        break
    except ValueError:
        print("Please enter a new value, this one is wrong")
        
print("end of programm")