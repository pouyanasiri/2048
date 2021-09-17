import time
import random
from os import stat, system, name

with open("score.txt", "r") as file: 
    high_score = int(file.readline())
    
board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
score = 0
flag_ask_continue = 0

def clear():
      
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

  
  
def display_board():
    show_score()
    print("\t\t\t*************************************")
    
    for i in range(4) :
        print("\t\t\t* ",end = "")
        for j in range(4) :
            print("{0:6d}".format(board[i][j]), end=" ")
        print("      *")
        
        
    print("\t\t\t*************************************")
    
    
def check_free_space(i,j):
    return board[i][j] == 0

def check_game_over():
        global score
        print(" GAME OVER ")
        score = 0
        time.sleep(2)
        menu()

def add_element_board():
    find_room = 0
    
    for i in range(4) :
        for j in range(4) :
            
            if check_free_space(i,j):
                find_room = 1
                break
                
    if find_room == 1:
        
        while True :
            column = random.randint(0,3)
            row = random.randint(0,3)
            if check_free_space(row,column) :
                board[row][column] = 2
                break
    else :
        check_game_over()

def check_win():
    global score
    global flag_ask_continue
    
    if score == 2048 :
        high_score = score
        print("you are won \n")
        ans = input("do you want to continue ? (y/n) : ").lower()
        
        if ans == 'y':
            flag_ask_continue = 1
        
        elif ans == 'n':
            clear()
            show_score()
            print ("you finish the game !")
            time.sleep(2)
            score = 0
            menu()
            
        else :
            print("Incorrect input !\n try again")
            time.sleep(2)
            clear()
            check_win()

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
    global score

    print("'D' or 'd' : Right\n'W' or 'w' : UP\n"+\
        "'A' or 'a' : Left\n'S' or 's' : Down"+\
        "\nB or b : back to menu")
    
    choice = input("please choose a choice : ").lower()
    
    if choice == 'a' :
        move_left()
        
    elif choice == 'd' :
        move_right()
        
    elif choice == 'w' :
        move_up()
        
    elif choice == 's' :
        move_down()
    
    elif choice == 'b' :
        score = 0
        clear()
        menu()
        
    else:
        print("wrong input !")
        time.sleep(2)
        clear()
        display_board()
        get_choice()
    
        
def show_score():
    global score
    global high_score
    for row in board:
        if score < max(row):
            score = max(row)
    print (f"your score is : {score}        High Score is : {high_score}")
    if score > high_score :
        high_score = score
        with open("score.txt", "w") as file: 
            file.write(f"{score}") 
        
    
def menu():
    
    global board
    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    print ("1 : New game \n2 : Help \n3 : Exit")
    number = input("please enter your input : ")
    clear()
    
    if number == '1' :
        add_element_board()    
        game()    
    
    elif number == '2' :
        help_game()
    
    elif  number == '3' :
        exit()
        
    else :
        print("Wrong input : ")
        time.sleep(2)
        clear()
        menu()
    
def help_game():
    print("**********************************************************************************")
    time.sleep(1)
    print("*                      *** Description And Help ***                              *")
    time.sleep(1)
    print("* 2048 game in a project prepared by Pouya Nasiri                                *")
    time.sleep(1)
    print("* This game includes a 4 in 4 square.                                            *")
    time.sleep(1)
    print("* Victory condition : If you can obtain At least 2048 points , you win           *")
    time.sleep(1)
    print("* Equal condition : If all of room is full , you lost                            *")
    print("*\t\t\t\t\t\t\t\t\t\t *")
    time.sleep(1)
    print("**********************************************************************************")
    time.sleep(3)
    
    print("1 : Back   2 : Exit ")
    
    choice = input("please enter a choice : ")
    clear()
    
    if choice == '1' :
        menu()
        
    elif choice == '2':
        exit()
        
    else :
        help_game()


def game():
    global high_score
    
    while True :
        
        add_element_board()
        display_board()
        get_choice()
        if flag_ask_continue == 0 :
            check_win()
        clear()
        
def main():
    
    print("\t****Welcome to 2048 Game***")
    time.sleep(2)
    
    menu()
    game()        
        
    
if __name__ == '__main__':
    main()
    
    