# this is going to be cool cal cilator so lets go 
# so basically i'm just creting a simple python calculator to refresh my memeoryu funny how
#i forgor somthings but im happy t have them back 
# i wanted to use two functions one for input and one for opperations but i just left out the one for opp because
# i felt it was not necessary and would make the thing just complex fo no reaso so im just keeping it simple
# i wanted to do my while loop outside my function before then i relized that the variabkes were not global so i can't
# everything including the while loop would be inside the my function 
# so putting everthing in the def function did not work so now i have to remove my while loop from there
# just lernt this get_number function really helpful 
# i use the while loop to lock in for if the opp is not correct instead of closing the code it will loop till
# the coorect opp 


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def run():
    print("HEY WELCOME!  \nENTER q TO END")

    while True:
        global opp
        opp = input("SELECT OPERATOR ( +  -  *  /  //  %  q ) : ").lower()
        if opp in ["+", "-", "*", "/", "//", "%", "q"]:
            break
        else:
            print("SYNTAX ERROR! Restarting...\n")

    if opp == "q":
        return
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))

    if opp == "+":
        ans = num_1 + num_2
        print (round(ans,2))
    elif opp == "-":
        ans = num_1 - num_2
        print (round(ans,2))
    elif opp == "*":
        ans = num_1 * num_2
        print (round(ans,2))
    elif opp == "/":
        ans = num_1 / num_2
        print (round(ans,2))
    elif opp == "//":
        ans = num_1 // num_2
        print (round(ans,2))
    elif opp == "%":
        ans = num_1 % num_2
        print (round(ans,2))
    else:
        print("SYNTAX ERROR !")

   
       
    return
    
while True:
    run()
    if opp.lower() == "q":
        print("CLOSING IV CLAC")
        break


