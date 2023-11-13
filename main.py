import random

user_win=0
computer_win=0

opt=["rock","paper","scissors"]

while True:
    u_input=input("Type Rock/Paper/Scissors or Q for Quit The Game: ").lower()
    if u_input =='q':
        break
    if u_input not in opt :
        continue

    ran_number=random.randint(0,2)
    #rock:0, paper:1,scissors:2

    com_pick=opt[ran_number]
    print("Computer Picked",com_pick + ".")
    if u_input =="rock" and com_pick =="scissors":
        print("you won")
        user_win+=1
        continue
    elif u_input =="paper" and com_pick =="rock":
        print("you won")
        user_win+=1
        continue
    elif u_input =="scissors" and com_pick =="paper":
        print("you won")
        user_win+=1
        continue
    else:
        print("you lost!!")
        computer_win+=1

print("you won",user_win, " Times")
print("The computer won",computer_win," Times")



print("Goodbye")
