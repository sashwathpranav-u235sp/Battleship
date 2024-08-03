#First Non graphical python based game


#This is to power the bot that the player would be battling against
import random as r

#For Game Loop
running=True

#Coordinates of the battlefield
Rows=["A","B","C","D","E","F"]
Colums=[1,2,3,4,5,6]

#List of choices for the enemy
EnemyChoices=list()
Rows2=["A","B","C","D","E","F"]
Colums2=[1,2,3,4,5,6]
for i in Rows2:
    for j in Colums2:
        EnemyChoices.append(i+str(j))


#For Storage
coordinates=dict()
PlayerCoordinates=dict()

def Start():
    global running
    ans = int(input("Select your desired option\n1.Play\n2.Quit\n"))
    if ans == 1:
        number = 6
        repeatp = list()
        repeatnumsp = list()
        for i in range(number):
            aa = input("Choose a row from A to F(the letters must be in capital letters)\n")
            bb = int(input("Enter a column from 1 to 6\n"))
            if aa in repeatp and bb in repeatnumsp:
                Rows.remove(aa)
                Colums.remove(bb)
                PlayerCoordinates[r.choice(Rows) + str(r.choice(Colums))] = i
                print("Repetitions are not allowed, current value replaced by a random coordinate")
            else:
                repeatp.append(aa)
                repeatnumsp.append(bb)
                PlayerCoordinates[aa + str(bb)] = i

        Rows1 = ["A", "B", "C", "D", "E", "F"]
        Colums1 = [1, 2, 3, 4, 5, 6]
        number = 6
        global coordinates
        repeat = list()
        repeatnums = list()
        for i in range(number):
            b = r.choice(Rows1)
            a = str(r.choice(Colums1))
            if a in repeatnums and b in repeat:
                Colums1.remove(int(a))
                Rows1.remove(b)
                coordinates[r.choice(Rows1) + str(r.choice(Colums1))] =i
            else:
                repeat.append(b)
                repeatnums.append(a)
                coordinates[b + a] = i
    else:
        print("Thanks for using me")
        running=False



#Starting the game
Start()


#GameLoop

while running:
    if running==False:
        break
    else:
        count = len(PlayerCoordinates)
        ecount = len(coordinates)
        ec = coordinates
        pc = PlayerCoordinates

        print("These are the coordinates of your ships\n", PlayerCoordinates)
        print()
        print()

        attack = input("Enter the coordinate of your enemy ship to attack\n(For example: C5)\n")
        print()
        print()

        if attack in ec:
            print("You sunk a ship")
            ecount = ecount - 1
            print("Number of enemy ships remaining:", ecount)
            print("Get ready for the bot's move")
            ec.pop(attack)
            print()
            print()

        else:
            print("You missed, try again")
            print("Number of enemy ships remaining:", ecount)
            print("Get ready for the bot's move")
            print()
            print()

        enemyattack = r.choice(EnemyChoices)
        print()
        print()
        if enemyattack in PlayerCoordinates:
            print("Your enemy sunk one of your ships")
            count -= 1
            print("Number of ships remaining", count)
            print("Get ready to attack him")
            pc.pop(enemyattack)
            print()
            print()

        else:
            print("Your enemy missed his target")
            print("Number of ships remaining", count)
            print("Get ready to attack him")
            EnemyChoices.remove(enemyattack)
            print()
            print()



        if ecount == 0:
            print("You won this match")
            print("Thank you for playing battleship")
            running=False
        elif count == 0:
            print("You lost this match")
            print("Thank you for playing battleship")
            running=False







































