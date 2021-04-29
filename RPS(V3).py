import random
print("Welcome to the RockPaperScissors game.")
def algorithm():
    action = random.choice(["Rock", "Paper", "Scissors"])
    print('Menu.\n**************\nPress 1 to select Rock.\nPress 2 to select Paper.\nPress 3 to select Scissors.\n**************')
    decision = int(input('Choose an option(1/2/3):'))
    if action=='Rock' and decision==1:
        print('Draw.')
    elif action=='Paper' and decision==2:
        print('Draw')
    elif action=='Scissors' and decision==3:
        print('Draw')
    elif action=='Rock' and decision==2:
        print('You WON')
    elif action=='Rock' and decision==3:
        print('You LOST, better luck next time.')
    elif action=='Paper' and decision==1:
        print('You LOST, better luck next time.')
    elif action=='Paper' and decision==3:
        print('You WON')
    elif action=='Scissors' and decision==1:
        print('You WON')
    elif action=='Scissors' and decision==2:
        print('You LOST, better luck next time.')

algorithm()

def again():
    while True:
        q = input("Do you want to play again?(y/n)")
        if q == 'n':
            exit()
        elif q == 'y':
            algorithm()
again()
