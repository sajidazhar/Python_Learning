winning_number = 25
guess_number = input("enter the number")
guess_number = int(guess_number)
if winning_number == guess_number:
    print("you win")
else:
    if guess_number < winning_number:
        print("too low")
    else:
        print("too high")
