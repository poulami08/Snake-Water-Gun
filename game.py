import random

def game(computer,player):
    if computer ==player:
        return None
    elif computer =="snake":
        if player =="water":
            return False
        elif player =="gun":
            return True
    elif computer =="water":
        if player =="gun":
            return False
        elif player =="snake":
            return True
    elif computer =="gun":
        if player =="snake":
            return False
        elif player =="water":
            return True
        


print("Hey! Welcome to snake, water, gun game")
print("Player 1- choose an object : snake , water or gun? ")
rand = random.randint(1,3)
if rand == 1:
    computer ="snake"
elif rand == 2:
    computer = "water"
elif rand == 3:
    computer = "gun"
print("Player 2- choose an object : snake , water or gun?")
m=input()
player =m.lower()



# if( m== "snake" or m=="water" or m=="gun" ):
#     if(m==)

print(f"Player 1 choose {computer}")
print(f"Player 2 choose {player}")

a= game(computer,player)

if a == None:
    print("the game is a tie")
elif a == True:
    print("You win")
else:
    print("You lose")