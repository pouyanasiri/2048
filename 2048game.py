import time
import random
from os import X_OK, stat, system, name

board = [[0,0,0,2],[0,2,2,2],[0,2,2,2],[2,0,0,2]]
score = 0
high_score = 0

def clear():
      
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')
  
def display_board():
    show_score()
    print("\t\t\t********************")
    for i in range(4) :
        print("\t\t\t",end ="")
        for j in range(4) :
            print(f"* {board[i][j]} *",end = "") 
        print()
    print("\t\t\t********************")
    
    
def check_free_space(i,j):
    return board[i][j] == 0

def add_element_board():
    row = 0 ; column = 0; flag = 0
    for i in range(4):
        for j in range(4):        
            column = random.randint(0,3)
            row = random.randint(0,3)
            if check_free_space(row,column) :
                return (i , j)
    
    return (4 , 4)
            
            
                
                
                            
def check_free_space(i,j):
    return board[i][j] == 0


def check_game_over():
    if add_element_board() == (4,4):
        print(" GAME OVER ")
        
    

def check_win():
    if score == 2048 :
        print("you are won \n")
        return input("do you want to continue ? (y/n) : ").lower()
    return

##############################################################
def add_elements_move_up() :                    
    for i in range(3):
        for j in range(4):
            if board[i][j] == board[i+1][j]:
                board[i][j] += board[i+1][j] 
                board[i+1][j] = 0
                 
def move_up():
    for countr in range(2):
        i = 1
        while i < 4 :
            j = 0
            while j < 4:
                temp_i = i
                while temp_i > 0 and check_free_space(temp_i-1,j) :
                    board[temp_i-1][j] = board[temp_i][j]
                    board[temp_i][j] = 0
                    temp_i-=1
                j+=1
            i+=1
        if countr == 1 :
            break
        add_elements_move_up()            
    display_board()
######################################################################################    
def add_elements_move_down() :                    
    i=3
    while i >0 :
        for j in range(4):
            if board[i][j] == board[i-1][j]:
                board[i][j] += board[i-1][j] 
                board[i-1][j] = 0
        i-=1    
def move_down():
    for countr in range(2):
        i = 2
        while i >-1 :
            j = 0
            while j < 4:
                temp_i = i
                while temp_i < 3 and check_free_space(temp_i+1,j) :
                    board[temp_i+1][j] = board[temp_i][j]
                    board[temp_i][j] = 0
                    temp_i+=1
                j+=1
            i-=1
        if countr == 1 :
            break
        add_elements_move_down()            
    display_board()

#################################################################################
def add_elements_move_left() :                    
    i=1
    while i < 4 :
        for j in range(4):
            if board[j][i-1] == board[j][i]:
                board[j][i-1] += board[j][i] 
                board[j][i] = 0
        i+=1        
def move_left():
    for countr in range(2):
        for ctr in range(3):
            i=1
            while i < 4 :
                j = 0 
                while j < 4:
                    if check_free_space(j,i-1) :
                        board[j][i-1] = board[j][i] 
                        board[j][i] = 0
                    j+=1
                i+=1        
        if countr == 1 :
            break
        add_elements_move_left()            
    display_board()
###################################################################################

def add_elements_move_right() :                    
    i=2
    while i > -1 :
        for j in range(4):
            if board[j][i+1] == board[j][i]:
                board[j][i+1] += board[j][i] 
                board[j][i] = 0
        i-=1        
        
def move_right():
    for countr in range(2):
        for ctr in range(3):
            i=2
            while i > -1 :
                j = 0 
                while j < 4:
                    if check_free_space(j,i+1) :
                        board[j][i+1] = board[j][i] 
                        board[j][i] = 0
                    j+=1
                i-=1   
        if countr == 1 :
            break
        add_elements_move_right()            
    display_board()
    
def get_choice():
    print("'D' or 'd' : Right\n'W' or 'w' : UP\n"+\
        "'A' or 'a' : Left\n'S' or 's' : Down")
    choice = input("please choose a choice : ").lower()
    if choice == 'a' :
        move_left()
        
    elif choice == 'd' :
        move_right()
        
    elif choice == 'w' :
        move_up()
        
    elif choice == 's' :
        move_down()
        
    else:
        print("wrong input !")
        time.sleep(2)
        clear()
        get_choice()
        
    if check_win() == 'n':
        pass
    check_game_over()
        
def show_score():
    global score
    for row in board:
        if score < max(row):
            score = max(row)
    print (f"score : {score}")
    

def main():
    print("\t****Welcome to 2048 Game***")
    while True :
        clear()
        display_board()
        get_choice()
        
        
    
if __name__ == '__main__':
    main()