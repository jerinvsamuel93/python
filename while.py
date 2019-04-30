i = 1
while i<=3:
    guess = input("guess")
    guess = int(guess)
    if( guess == 5):
        print('right')
        i = 4 # or break
    else :
        if i == 3:
            print("failed")
        else:
            print("try again")
        i=i+1