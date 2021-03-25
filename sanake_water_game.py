import random

#  function for user input 
def game(comp,you):
    if comp == you:
        return None
    elif comp == 's': 
        if you == 'w':
            return False
        elif you == 'g':
            return True
        elif comp == 'w':
            if you == 's':
                return False
            elif you =='g':
                return True
        elif comp == 'g':
            if you == 's':
                return False
            elif you =='w':
                return True
# print("comp trun: snake(s) water(w) or gun(g)?")

# generate random no
randNo = random.randint(1, 3)
print(randNo)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

# user input 
you = input  ("YOUR TURN: SNAKE(s) WATER(w) OR GUN(g) ?")

a = game(comp, you)

print(f"Comp choose {comp}")
print(f"You choose {you}")

if a == None:
    print ("The game is tie")
elif a:
    print ("You win!!!!")    
else:
    print ("You lose")