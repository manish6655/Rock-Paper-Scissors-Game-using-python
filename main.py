while True:
    import random

    def gameWin(computer, you):
        if computer == you:
            return None
        elif computer == 's':
            if you == 'w':
                return False
            elif you == 'g':
                return True
        elif computer == 'w':
            if you == 'g':
                return False
            elif you == 's':
                return True
        elif computer == 'g':
            if you == 'w':
                return True
            elif you == 's':
                return False

    print("computernTurn: Snake(s) Water(w) Gun(g)?")
    randNo = random.randint(1, 3)
    if randNo == 1:
        computer = 's'
    elif randNo == 2:
        computer = 'w'
    elif randNo == 3:
        computer = 'g'
        

    you = input("Your Turn: Snake(s) Water(w) Gun(g)?")
    a = gameWin(computer, you)

    print(f"computer choose {computer}")
    print(f"you choose {you}")

    if a == None:
        print("The Game is Tie")
    elif a:
        print("You Win")
    else:
        print("You Loose")
            
