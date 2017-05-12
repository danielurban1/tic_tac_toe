# -*- coding: utf-8 -*-
'''Gra kółko i krzyżyk'''
import random
 

def board(markers):
    print(markers[0]+"|"+markers[1]+"|"+markers[2])
    print("-----")
    print(markers[3]+"|"+markers[4]+"|"+markers[5])
    print("-----")
    print(markers[6]+"|"+markers[7]+"|"+markers[8])


def avalible_moves(markers):
    legal_moves = [" "]*9
    move = 0
    while move <=9 :
        
        if markers[move-1]==" ":
            legal_moves[move-1]=str(move)
        elif markers[move-1]=="x":
            legal_moves[move-1] ="x"
        else:
            legal_moves[move-1] = "o"
        move +=1
    print("Możesz wykonać następujące ruchy")
    print(legal_moves[0]+"|"+legal_moves[1]+"|"+legal_moves[2])
    print("-----")
    print(legal_moves[3]+"|"+legal_moves[4]+"|"+legal_moves[5])
    print("-----")
    print(legal_moves[6]+"|"+legal_moves[7]+"|"+legal_moves[8],"\n")       
    
    
def player_move(markers, to_move):
    while True:
        player_move = input("Wybierz swój ruch"+"("+to_move+"):")
        try:
            player_move = int(player_move)
            if int(player_move) in range(1,10) and not (markers[player_move-1]=="o" or markers[player_move-1]=="x"):
                markers[player_move-1]=to_move
                return markers
            else:
                print("Niewłaściwy ruch, spróbuj jescze raz!")
        except:
            print("Niewłaściwy ruch, możesz wybierać tylko liczby!") 
    return markers

def change_player(to_move):
    if to_move =="o":
        to_move ="x"
    else:
        to_move ="o"
    return to_move


def play_vs_ai():
    while True:
        choice = input("Czy chcesz grać przeciwko komputerowi: (t)ak (n)ie")
        if choice == "t":
            return True
        elif choice == "n":
            return False
        else:
            print("Niewłaściwa wartość. Spróbuj ponownie.")
def win_check(markers, to_move):
    check = 0
    while check <9:
        if markers[check] == to_move and markers[check+  1] == to_move and markers[check +2] == to_move:
            print(player, "wygrał.")
            return 1
        check += 3
    check = 0
    while check <3:
        if markers[check] == to_move and markers[check+  3] == to_move and markers[check +6] == to_move:
            print(player, "wygrał.")
            return 1
        check +=1
    if markers[0] == to_move and markers[4] == to_move and markers[8] == to_move or markers[2] == to_move and markers[4] == to_move and markers[6] == to_move:
        print(player, "wygrał.")
        return 1  

    if " " not in markers:
        print("Remis")
        return 2        
    return 0 

def ai_difficulty():
    while True:
        ai = input("Wybierz poziom trudności (l)atwy, (t)rudny:")
        if ai == "l":
            return True
        elif ai == "t":
            return False
        else:
            print("Podana wartość jest nieprawidłowa. Spróbuj jeszcze raz.")
def ai_move(markers, to_move, ai):
    if ai is False:
        possible_moves = []
        player_moves = []
        ai_moves = []
        for move in range (0, 9):
            if markers[move] == " ":
                possible_moves.append(int(move))
            elif markers[move] == "o":
                player_moves.append(int(move))
            else:
                ai_moves.append(int(move))
        print(possible_moves)
        for i in possible_moves:
            markers[i] = to_move
            if win_check(markers, to_move) == 1:
                markers[i] = to_move
                return markers[i]
            else:
                markers[i] = " "
        for i in possible_moves:
            to_move = "o"
            markers[i] = to_move
            if win_check(markers, to_move) == 1:
                markers[i] = "x"
                return markers
            else:
                markers[i] = " " 
        to_move = "x"
        if 4 in possible_moves:
            markers[4] = to_move
            return markers
        for i in possible_moves:
            if 0 or 2 or 6 or 8 in possible_moves:
                markers[i] = to_move                                        
                return markers[i]
        for i in possible_moves:
            if 1 or 3 or 5 or 7 in possible_moves:
                markers[i] = to_move                                        
                return markers[i]            
    else:
        possible_moves = []
        for move in range (0, 9):
            if markers[move] == " ":
                possible_moves.append(int(move))
        markers[random.choice(possible_moves)] = to_move
        return markers

def play_again():
    while True:
        again = input("Czy chcesz zagrać ponownie? (t)ak (n)ie:")
        if again == "t":
            return True
        elif again == "n":
            return False
        else:
            print("Niewłaściwa wartość. Spróbuj ponownie.")

while True:
    list_of_markers = [" "]*9
    player = "o"
    comp = play_vs_ai()
    if comp is True:
        random_ai = ai_difficulty()
    while True:
        board(list_of_markers)
        avalible_moves(list_of_markers)
        player_move(list_of_markers, player)
        board(list_of_markers)
        if win_check(list_of_markers, player) != 0:  
            board(list_of_markers)
            break    
        if comp is True:
            player = change_player(player)
            print("Ruch komputera")
            ai_move(list_of_markers, player, random_ai)
            if win_check(list_of_markers, player) != 0:  
                board(list_of_markers)
                break                
        player = change_player(player)
    play = play_again()
    if play is True:
        continue
    else:
        break