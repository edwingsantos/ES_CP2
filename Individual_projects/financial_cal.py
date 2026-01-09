#ES 1 RPG manageer prject 

# make a funtion called check(digit)
def check(digit):
    #if digit is a digit make it true AND make it digit be a float > 0
    if digit.isdigit() == True and float(digit) >0:
        #make digit equals a float 
        digit = float(digit)
        #return to the other funtion as true 
        return True, digit
    #else print plase select a number grater than 0
    else:
        print("You jobles monkey")
        #return to the other funtion as false 
        return False, digit

#make a funtion named savings 
def goal_reach():
#Make a while true loop
    while True:
        # ask the user what the goal is as an input as a varable called goals
        goal= input("What would you like your goal to be?: ").strip()
        #tes,goal make it call check(goal)
        test,goal = check(goal)
        #if the test is true print nice job and break
        if test == True:
            print(f"{goal} is a great number to safe, keep it up! ")


#REMEBER TO GO BACK AND SAY HOW MUCH TIME IT TAKES THE USER TO REACH THAT GOALLLLL


            break
        else:
            continue
goal_reach()
#test,variable = check(variable)
