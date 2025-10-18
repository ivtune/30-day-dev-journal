 # the game of rock paper scissors , rockes kills scissors, sicssors kills paper and paper kills rock 
# i commented out the first code that i did to show that if and elif could work but now i want to make it less long 
# so im using more of logic 
import random 

"""def play ():
    global pscore 
    global cscore
    pscore = 0 
    cscore = 0
    choices = ['r','p','s']
    print("WELCOME ! \nGAME ROCK PAPER SCISSORS")
    mpu=input("Enter your option \n'rock' 'paper' 'scissors'\n(R P S)\n").lower()
    cpu = random.choice(choices) 


    if mpu not in choices:
        print ("Enter R or P or S ")
        return
    
    if mpu == cpu :
        print ('draw!')
    elif mpu == 'r' and cpu =='s':
        print("ROCK SMASH!")
        pscore = +1
    elif mpu == 'p' and cpu == 'r':
        print('PAPER KILLS!')
        pscore = +1
    elif mpu == 's' and cpu == 'p':
        pscore = +1
        print ("SCISSORS CUT!")
    elif cpu == 'r' and mpu =='s':
        print("ROCK SMASH!")
        cscore =+1
    elif cpu == 'p' and mpu == 'r':
        print('PAPER KILLS!')
        cscore =+1
    elif cpu == 's' and mpu == 'p':
        print ("SCISSORS CUT!")
        cscore =+1
    else :
        print("WHAT IS WRONG!") 
    
    while True :
    
        if pscore >= 3 :
            print ("player wins!")
        elif cscore >=3 :
            print ("computer wins!")
        else :
            print(f"player score = {pscore}\ncomputer = {cscore}")
        break   

print ("welcome to R P S")
play() """

    
import random

def play():
    pscore = 0
    cscore = 0
    choices = ['r', 'p', 's']
    print("WELCOME!\nGAME: ROCK PAPER SCISSORS")

    while pscore < 3 and cscore < 3:
        mpu = input("Enter your option: 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
        cpu = random.choice(choices)

        if mpu not in choices:
            print("Invalid input! Enter 'r', 'p', or 's'.")
            continue

        print(f"You chose {mpu}, CPU chose {cpu}")

        if mpu == cpu:
            print("Draw!")
        elif (mpu == 'r' and cpu == 's') or (mpu == 'p' and cpu == 'r') or (mpu == 's' and cpu == 'p'):
            print("You win this round!")
            pscore += 1
        else:
            print("CPU wins this round!")
            cscore += 1

        print(f"Score → Player: {pscore}, CPU: {cscore}\n")

    if pscore == 3:
        print("🎉 Player wins the game!")
    else:
        print("💻 CPU wins the game!")

play()
