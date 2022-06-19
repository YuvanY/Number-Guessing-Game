import random

print("Welcome To our Number Guessing Game\n")
print("Hope You Will Have Fun\n")

print('You have 4 four modes: Easy Medium or Super_Hard')


Diffculty = input('In which mode you want to play?: ').lower().replace(' ', '')
if Diffculty != 'easy' or Diffculty != 'medium' or Diffculty != 'super_hard' or Diffculty != 'superhard':
    while Diffculty != 'easy' and Diffculty != 'medium' and Diffculty != 'super_hard' and Diffculty != 'superhard':
        print('Please answer from the options given above')
        Diffculty = input('In which mode you want to play?: ').lower().replace(' ', '')
        continue


Total_Try = 10

if Diffculty == 'easy':
    print('You have to choose a number between 1 - 100. If your number matchs with the computer\'s number \nwithn 10 trys, You Win, Else, You Loose\n')
    Hidden_Number = random.randint(1, 100)
    try:
        User_Number = int(input('Choose a number between 1 - 5000: '))
    except:
        print('ERROR :( Someting Went Wrong\n')
        print('may be you have exceedently typed something sole')
        exit()
        exit()



elif Diffculty == 'medium':
    print('You have choose a number between 1 - 1000. If your number match with the computer\'s number \nwithn 10 trys, You Win Else,You Loose\n')
    Hidden_Number = random.randint(1, 1000)
    try:
        User_Number = int(input('Choose a number between 1 - 5000: '))
    except:
        print('ERROR :( Someting Went Wrong\n')
        print('may be you have exceedently typed something sole')
        exit()


elif Diffculty == 'super_hard' or Diffculty == 'superhard':
    print('You have choose a number between 1 - 5000. If your number match with the computer\'s number \nwithn 10 trys, You Win Else,You Loose\n')
    Hidden_Number = random.randint(1, 5000)
    try:
        User_Number = int(input('Choose a number between 1 - 5000: '))
    except:
        print('ERROR :( Someting Went Wrong\n')
        print('may be you have exceedently typed something sole')
        exit()
    

print(Hidden_Number)



while True:
    if Hidden_Number == User_Number:
        print('Your Won')

        print(f'Your Won in {10 - Total_Try + 1} Trys')
        if Diffculty == 'super_hard' or Diffculty == 'superhard' and Hidden_Number == User_Number:
            print('OMG YOU WON IN HARD MODE')
        break
    elif Hidden_Number != User_Number:
        Total_Try -= 1
        if User_Number > Hidden_Number:
            print('Your number is Greater than the computer\'s\n')
        else:
            print('Your number is smaller than the computer\'s\n')

        print(f'You have {Total_Try} try left')
        try:
            User_Number = int(input('Choose a number between 1 - 100: '))
        except:
            print('ERROR :( Someting Went Wrong\n')
            print('may be you have exceedently typed something sole')
            exit()
    elif Total_Try == 0:
        break
        print('You Lose')
