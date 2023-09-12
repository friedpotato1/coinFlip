import random,pyinputplus as pyip,sys,time
try:
    while True:
        choice = random.randint(0,1)
        option = pyip.inputMenu(['Heads','Tails'],numbered='True')
        print('\n')
        if choice == 0:
            coinSide = 'Heads'
        elif choice == 1:
            coinSide = 'Tails'
        if coinSide == option:
            print(f'You won the coin flipped to {coinSide}'.center(50,'*'),'\n')
        elif coinSide!=option:
            print(f'Coin didnt flip to ur choosen side {option}'.center(50,'*'),'\n')
        
        #time.sleep(5)
except KeyboardInterrupt:
    sys.exit()