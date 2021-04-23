import random
action = random.choice(['Rock','Paper','Scissors'])
decision = input('Hello. Would you like to play a Rock paper scissors with me?(y/n):')
if decision=='n':
    print('Okay bye, take care.')
if decision=='y':
    print('Great! Now lets have a look at our menu.\n**************\nPress 1 to select Rock.\nPress 2 to select Paper.\nPress 3 to select Scissors.\n**************')
    decision2 = int(input('Choose an option(1/2/3):'))
    if action=='Rock' and decision2==1:
        print('Draw')
    elif action=='Paper' and decision2==2:
        print('Draw')
    elif action=='Scissors' and decision2==3:
        print('Draw')
    elif action=='Rock' and decision2==2:
        print('You WON')
    elif action=='Rock' and decision2==3:
        print('You LOST')
    elif action=='Paper' and decision2==1:
        print('You LOST')
    elif action=='Paper' and decision2==3:
        print('You WON')
    elif action=='Scissors' and decision2==1:
        print('You WON')
    elif action=='Scissors' and decision2==2:
        print('You LOST')
