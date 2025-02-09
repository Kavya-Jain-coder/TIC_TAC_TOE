import os

N = 13
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def tic_tac_toe():
    k = 0
    for i in range(N):
        for j in range(N):
            if i == 4 or j == 4 or i == 8 or j == 8:
                print("*", end=" ")
            elif (i == 2 or i == 6 or i == 10) and (j == 2 or j == 6 or j == 10):
                print(ls[k], end=" ")
                k += 1
            else:
                print(" ", end=" ")
        print()


def verify(x):
    a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if x not in a:
        return False
    x = int(x)
    if ls[x-1] == "X" or ls[x-1] == "O":
        return False
    return True


def update(x,i):
    if i%2 == 0:
        ls[x-1] = "X"
    else:
        ls[x-1] = "O"
    
    
def is_won():
    win_conditions = [ (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6) ]
    for a, b, c in win_conditions:
        if ls[a] == ls[b] == ls[c] and ls[a] in ["X", "O"]:
            return True
    return False

tic_tac_toe()
i = 0
while i < 9:
    if i%2 == 0:
        print("User1 Turn")
    else:
        print("User2 Turn")
    print("Enter your choice(1-9):", end=" ")
    z = input()
    y = verify(z)
    if y == False:
        tic_tac_toe()
        print("Invalid Choice. Please try again...")
        continue
    else:
        update(int(z),i)
        i+=1
        tic_tac_toe()
        
        if is_won():
            if i%2 == 0:
                print("User2 WON!")
            else:
                print("User1 WON!")
            break
if is_won() == False:
    print("It's a Tie..")