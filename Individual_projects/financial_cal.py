#ES 1 RPG manageer prject 

# make a funtion called check(digit)
def check(digit):
    #if digit is a digit make it true AND make it digit be a float > 0
    if digit.replace(".", "", 1).isdigit():
        #make digit equals a float 
        digit = float(digit)
        #return to the other funtion as true 
        if digit > 0:
            return True, digit
        #else print plase select a number grater than 0
        else:
            print("Please enter a number greater than 0")
            return False, digit
    else:
        print("Please enter a valid number")
        return False, digit
    
#make a funtion named goal_reach 
def goal_reach():
    # Make a while True loop
    while True:
        # Ask the user what the goal is as an input as a variable called goal
        goal = input("What would you like your goal to be?: ").strip()
        # test goal by calling check(goal)
        test, goal = check(goal)
        # if the test is true, print nice job and continue
        if test == True:
            print(f"{goal} is a great number to save, keep it up!")
            #make a while true loop
            while True:
                #make a variable called contribution and ask how much they safe 
                contribution = input("How much will you save each month?: ").strip()
                #check if the input is valid and is a number
                test, contribution = check(contribution)
                #make it if test is true break
                if test == True:
                    break
            #define calculate months and all things it need to acces 
            def calculate_months(goal, contribution):
                #make a variable named months = 0
                months = 0
                #make another named remaining be goal_amount
                remaining = goal
                #make a while loop be if reminging is grater than 0 it will subtract from contribution and add 1 to the months
                while remaining > 0:
                    remaining -= contribution
                    months += 1
                    #return months 
                return months
            #make months needed = calculate monts
            months_needed = calculate_months(goal, contribution)
            #print with f string so it shows amount with 2 decimal points 
            print(f"It will take {months_needed} months to save ${goal:.2f}")
            #break
            break
        #else continue
        else:
            continue

#make a funtion named compund interest 
def compound_interest():
    #make a while loop
    while True:
        #make choice = input what is the starting amount 
        choice = input("Enter the starting amount: ").strip()
        #check by calling check(choice)
        test, principal = check(choice)  # use your check function
        #if test is true break else continue 
        if test == True:
            break
        else:
            continue
    # Ask the user for interest rate inside another while loop 
    while True:
        rate = input("Enter the interest rate (percent): ").strip()
        #check if it checks the requirements from the check(rate) funtions
        test, rate = check(rate)
        #if test is True break else continue        
        if test == True:
            break
        else:
            continue
    # Ask the user for number of years inside another while loop
    while True:
        years = input("Enter how many years you will leave it to compound: ").strip()
        #check if it checks the requirements from the check(rate) funtions
        test, years = check(years)
        #if test is True break else continue
        if test == True:
            break
        else:
            continue
   #define calculate_compound put everything from the outside you need indise of the parenthesis 
    def calculate_compound(choice, rate, years):
        #mak total = choice time 1 +rate divided by 100, all to the power of years
        total = choice * (1 + rate / 100) ** years
        #return the total
        return total
    #make the total equals the calculate compund funtion
    total_amount = calculate_compound(principal, rate, years)
    # Print the result with f strings for clarification
    print(f"At the end of {years} years you will have ${total_amount:.2f}")

#make a funtion named buget allocator
def budget_allocator():
    # make a while loop asking how many categories there are 
    while True:
        choice = input("How many budget categories do you have?: ").strip()
        #check if is more than 0 and a num by using the check funtion
        test, choice = check(choice)
        #If test is true make choice be a integer and break
        if test == True:
            choice = int(choice)  # we need it as an integer for the loop
            break
        #else continue 
        else:
            continue
    #make a list for the categories names and another for the percentage
    category_names = []
    category_percentage = []

    #make a loop in i for the range for the choice
    for i in range(choice):
        #make name equals input category # plus one, then append the answer
        name = input(f"Category {i+1}: ").strip()
        category_names.append(name)
    #make a while true loop 
    while True:
        #make become an imput what is the montly income
        income = input("What is your monthly income?: ").strip()
        #check if is more than 0 and a num by using the check funtion
        test, income = check(income)
        #if test is true break
        if test == True:
            break
        #else continue
        else:
            continue

    #make the toatal percent 0
    total_percent = 0
    #make i in range choice
    for i in range(choice):
        #make a while loop making percent input what percent going to category name i
        while True:
            percent = input(f"What percent of your income goes to {category_names[i]}?: ").strip()
            #check if is more than 0 and a num by using the check funtion
            test, percent = check(percent)
            #if the test and percent is less than or equal to 100
            if test and percent <= 100:
                #if the total + the percent is grater than 100 print you cant go above 100 and continue
                if total_percent + percent > 100:
                    print("The percentages cant go above 100")
                    continue
                #append that to percentage category percent
                category_percentage.append(percent)
                #and add percent to it, break
                total_percent += percent
                break
    #make a funtion called calculate amount and put all things you need inside the parenthesis
    def calculate_amount(income, percent):
        #return the income times percent divided by 100
        return income * (percent / 100)
    print("Your budget allocation is:")
    for i in range(choice):
        amount = calculate_amount(income, category_percentage[i])
        print(f"{category_names[i]} is {amount:.2f}")

#make a funtion for sale price calculator
def sale_price_cal():
    #make a while loop 
    while True:
        #make choice input how much the item cost
        choice = input("How much does the item originally cost?: ").strip()
        #check if is more than 0 and a num by using the check funtion
        test, choice = check(choice)
        #if test true break
        if test == True:
            break

    #make another while true and make discount input what is the pecet of the discount
    while True:
        discount = input("What percent is the discount?: ").strip()
        #check if is more than 0 and a num by using the check funtion
        test, discount = check(discount)
        #if the test and discount is less than or equal to 100 break
        if test and discount <= 100:
            break
        #else print that the dicount cannot be more than 100%
        else:
            print("Discount cannot be more than 100%")
    #def calculate_sale and inside the parenthesis use the things you need 
    def calculate_sale(price, percent):
        #return the price times 1- the percent divided by 100
        return price * (1 - percent / 100)
    #make the sale price the equation before 
    sale_price = calculate_sale(choice, discount)
    # Print the results
    print(f"The item now costs ${sale_price:.2f}")

#make tip calculator funtion
def tip_calculator():
    #make a while loop
    while True: 
        #make the bill equals input how much is the bill 
        bill = input("How much is the bill?: ").strip()
        #check if is more than 0 and a num by using the check funtion
        test, bill = check(bill)
        #if the test is True break
        if test == True:
            break
    #make another while loop make the tip percentage input what percent of a tip are giving
    while True:
        tip_percent = input("What percent of a tip are you giving?: ").strip()
        #check if is more than 0 and a num by using the check funtion
        test, tip_percent = check(tip_percent)
        #if the test and tip percentege is less than or equal to 100 break
        if test and tip_percent <= 100:
            break
        #else print tip percentage cannot be more than 100%
        else:
            print("Tip percentage cannot be more than 100%")
    # make a funtion called calculate tip and have things you need inside of the parenthesis 
    def calculate_tip(amount, percent):
        #make tip amount equals amount time percent divided by 100
        tip_amount = amount * (percent / 100)
        #make the total equal amount + tip amount and return tip amount and total
        total = amount + tip_amount
        return tip_amount, total
    #make tip amount and total bill equal caculate tip
    tip_amount, total_bill = calculate_tip(bill, tip_percent)
    # Print the result with f strings 
    print(f"The tip amount is ${tip_amount:.2f} and your total is ${total_bill:.2f}")

#make a while true loop 
while True:
    #print welcome line 
    print("Welcome to your financial calculator")
    #make choice equals integer input to choose a number from the options 
    choice= int(input("Enter the number so select an option \n " 
    "1. Savings Time Calculator \n" 
    "2. Compound Interest Calculator \n" 
    "3. Budget Allocator \n"
    "4. Sale Price Calculator \n"
    "5. Tip Calculator\n"))
    #if choice is 1, call goal reach
    if choice == 1:
        goal_reach()
    #if choice is 2, call compound_interest
    elif choice == 2:
        compound_interest()
    #if choice is 3, call budget_allocator
    elif choice == 3:
        budget_allocator()
    #if choice is 4, call sale_price_cal
    elif choice == 4:
        sale_price_cal()
    #if choice is 5, call tip_calculator
    elif choice == 5:
        tip_calculator()
    #else print please select a actial option
    else:
        print("please select a actial option")
        continue
    