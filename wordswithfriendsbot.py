import math
import json


###Triple comments are debug lines

#Defaults
valuesWWF = {
    "a": 1,
    "b": 4,
    "c": 4,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 3,
    "h": 3,
    "i": 1,
    "j": 10,
    "k": 5,
    "l": 2,
    "m": 4,
    "n": 2,
    "o": 1,
    "p": 4,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 2,
    "v": 5,
    "w": 4,
    "x": 8,
    "y": 3,
    "z": 10
}
valuesScrabble = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10
}

board1 = [
    ['  ', '  ', '  ', 'tw', '  ', '  ', 'tl', '  ', 'tl', '  ', '  ', 'tw', '  ', '  ', '  '],
    ['  ', '  ', 'dl', '  ', '  ', 'dw', '  ', '  ', '  ', 'dw', '  ', '  ', 'dl', '  ', '  '],
    ['  ', 'dl', '  ', '  ', 'dl', '  ', '  ', '  ', '  ', '  ', 'dl', '  ', '  ', 'dl', '  '],
    ['tw', '  ', '  ', 'tl', '  ', '  ', '  ', 'dw', '  ', '  ', '  ', 'tl', '  ', '  ', 'tw'],
    ['  ', '  ', 'dl', '  ', '  ', '  ', 'dl', '  ', 'dl', '  ', '  ', '  ', 'dl', '  ', '  '],
    ['  ', 'dw', '  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'dw', '  '],
    ['tl', '  ', '  ', '  ', 'dl', '  ', '  ', '  ', '  ', '  ', 'dl', '  ', '  ', '  ', 'tl'],
    ['  ', '  ', '  ', 'dw', '  ', '  ', '  ', '++', '  ', '  ', '  ', 'dw', '  ', '  ', '  '],
    ['tl', '  ', '  ', '  ', 'dl', '  ', '  ', '  ', '  ', '  ', 'dl', '  ', '  ', '  ', 'tl'],
    ['  ', 'dw', '  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'dw', '  '],
    ['  ', '  ', 'dl', '  ', '  ', '  ', 'dl', '  ', 'dl', '  ', '  ', '  ', 'dl', '  ', '  '],
    ['tw', '  ', '  ', 'tl', '  ', '  ', '  ', 'dw', '  ', '  ', '  ', 'tl', '  ', '  ', 'tw'],
    ['  ', 'dl', '  ', '  ', 'dl', '  ', '  ', '  ', '  ', '  ', 'dl', '  ', '  ', 'dl', '  '],
    ['  ', '  ', 'dl', '  ', '  ', 'dw', '  ', '  ', '  ', 'dw', '  ', '  ', 'dl', '  ', '  '],
    ['  ', '  ', '  ', 'tw', '  ', '  ', 'tl', '  ', 'tl', '  ', '  ', 'tw', '  ', '  ', '  '],
]

#Debugging
board2 = [
    ['tl', '  ', 'tw', '  ', '  ', '  ', '  ', '  ', 'tw', '  ', 'tl'],
    ['  ', 'dw', '  ', '  ', '  ', 'dw', '  ', '  ', '  ', 'dw', '  '],
    ['tw', '  ', 'dl', '  ', 'dl', '  ', 'dl', '  ', 'dl', '  ', 'tw'],
    ['  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'tl', '  ', '  ', '  '],
    ['  ', '  ', 'dl', '  ', '  ', '  ', '  ', '  ', 'dl', '  ', '  '],
    ['  ', 'dw', '  ', '  ', '  ', '++', '  ', '  ', '  ', 'dw', '  '],
    ['  ', '  ', 'dl', '  ', '  ', '  ', '  ', '  ', 'dl', '  ', '  '],
    ['  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'tl', '  ', '  ', '  '],
    ['tw', '  ', 'dl', '  ', 'dl', '  ', 'dl', '  ', 'dl', '  ', 'tw'],
    ['  ', 'dw', '  ', '  ', '  ', 'dw', '  ', '  ', '  ', 'dw', '  '],
    ['tl', '  ', 'tw', '  ', '  ', '  ', '  ', '  ', 'tw', '  ', 'tl'],
]

#Scrabble
boardScrabble = [
    ['tw', '  ', '  ', 'dl', '  ', '  ', '  ', 'tw', '  ', '  ', '  ', 'dl', '  ', '  ', 'tw'],
    ['  ', 'dw', '  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'dw', '  '],
    ['  ', '  ', 'dw', '  ', '  ', '  ', 'dl', '  ', 'dl', '  ', '  ', '  ', 'dw', '  ', '  '],
    ['dl', '  ', '  ', 'dw', '  ', '  ', '  ', 'dl', '  ', '  ', '  ', 'dw', '  ', '  ', 'dl'],
    ['  ', '  ', '  ', '  ', 'dw', '  ', '  ', '  ', '  ', '  ', 'dw', '  ', '  ', '  ', '  '],
    ['  ', 'tl', '  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'tl', '  '],
    ['  ', '  ', 'dl', '  ', '  ', '  ', 'dl', '  ', 'dl', '  ', '  ', '  ', 'dl', '  ', '  '],
    ['tw', '  ', '  ', 'dl', '  ', '  ', '  ', '++', '  ', '  ', '  ', 'dl', '  ', '  ', 'tw'],
    ['  ', '  ', 'dl', '  ', '  ', '  ', 'dl', '  ', 'dl', '  ', '  ', '  ', 'dl', '  ', '  '],
    ['  ', 'tl', '  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'tl', '  '],
    ['  ', '  ', '  ', '  ', 'dw', '  ', '  ', '  ', '  ', '  ', 'dw', '  ', '  ', '  ', '  '],
    ['dl', '  ', '  ', 'dw', '  ', '  ', '  ', 'dl', '  ', '  ', '  ', 'dw', '  ', '  ', 'dl'],
    ['  ', '  ', 'dw', '  ', '  ', '  ', 'dl', '  ', 'dl', '  ', '  ', '  ', 'dw', '  ', '  '],
    ['  ', 'dw', '  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'tl', '  ', '  ', '  ', 'dw', '  '],
    ['tw', '  ', '  ', 'dl', '  ', '  ', '  ', 'tw', '  ', '  ', '  ', 'dl', '  ', '  ', 'tw'],
]

blanks = ['++', 'dl', 'tl', 'dw', 'tw', '  ']

board = board1
values = valuesWWF
scrabble_point_value = 35

board_height = len(board)
board_width = len(board[0])

#Functions
def check_letters(word, location_y, location_x, direction):

    availiable_hand = hand.copy()

    valid = False
    used_letter = False
    blank_indexes = []

    if direction == 'right':
        ends_valid = False

        if location_x == 0:
            ends_valid = True
        elif board[location_y][location_x - 1] in blanks:
            ends_valid = True
        else:
            ends_valid = False
        if ends_valid == True:
            if location_x + len(word) == board_width:
                ends_valid = True
            elif board[location_y][location_x + len(word)] in blanks:
                ends_valid = True
            else:
                ends_valid = False

        if ends_valid == True:
            for letter in range(len(word)):
                if board[location_y][location_x + letter] == word[letter]:
                    valid = True
                elif board[location_y][location_x + letter] in blanks:
                    if word[letter] in availiable_hand:
                        availiable_hand.remove(word[letter])
                        valid = True
                        used_letter = True
                    elif 'blank' in availiable_hand:
                        availiable_hand.remove('blank')
                        valid = True
                        used_letter = True
                        blank_indexes.append(letter)
                        crossed_blank = False
                        if location_y - 1 >= 0:
                            if not(board[location_y - 1][location_x + letter] in blanks):
                                crossed_blank = True
                        if location_y + 1 < board_width:
                            if not(board[location_y + 1][location_x + letter] in blanks):
                                crossed_blank = True
                        #if crossed_blank == True:
                            #score_subtract += values[word[letter]]
                    else:
                        valid = False
                        break
                else:
                    valid = False
                    break

    elif direction == 'down':
        ends_valid = False

        if location_y == 0:
            ends_valid = True
        elif board[location_y - 1][location_x] in blanks:
            ends_valid = True
        else:
            ends_valid = False
        if ends_valid == True:
            if location_y + len(word) == board_height:
                ends_valid = True
            elif board[location_y + len(word)][location_x] in blanks:
                ends_valid = True
            else:
                ends_valid = False

        if ends_valid == True:
            for letter in range(len(word)):
                if board[location_y + letter][location_x] == word[letter]:
                    valid = True
                elif board[location_y + letter][location_x] in blanks:
                    if word[letter] in availiable_hand:
                        availiable_hand.remove(word[letter])
                        valid = True
                        used_letter = True
                    elif 'blank' in availiable_hand:
                        availiable_hand.remove('blank')
                        valid = True
                        used_letter = True
                        blank_indexes.append(letter)
                        crossed_blank = False
                        if location_x - 1 >= 0:
                            if not(board[location_y + letter][location_x - 1] in blanks):
                                crossed_blank = True
                        if location_x + 1 < board_width:
                            if not(board[location_y + letter][location_x + 1] in blanks):
                                crossed_blank = True
                        #if crossed_blank == True:
                            #score_subtract += values[word[letter]]
                    else:
                        valid = False
                        break
                else:
                    valid = False
                    break
    if used_letter == False:
        valid = False

    if valid == True:
        check_crosswords(word, location_y, location_x, direction, availiable_hand, blank_indexes)

def check_crosswords(word, location_y, location_x, direction, hand_avail, blank_indexes):
    availiable_hand = hand_avail
    valid = False
    word_crossword_list = []
    if direction == 'right':
        for letter in range(len(word)):
            if board[location_y][location_x + letter] in blanks:
                crossword = word[letter]
                index = 1
                while location_y - index >= 0:
                    if not(board[location_y - index][location_x + letter] in blanks):
                        crossword = board[location_y - index][location_x + letter] + crossword
                        index += 1
                    else:
                        break
                index = 1
                while location_y + index < board_height:
                    if not(board[location_y + index][location_x + letter] in blanks):
                        crossword += board[location_y + index][location_x + letter]
                        index += 1
                    else:
                        break
                if (len(crossword) == 1) or ((crossword + '\n') in enable1):
                    valid = True
                    if (len(crossword) != 1) and not(letter in blank_indexes):

                        if board[location_y][location_x + letter] == 'dl':
                            crossword += word[letter]
                        elif board[location_y][location_x + letter] == 'tl':
                            crossword += word[letter]
                            crossword += word[letter]
                        elif board[location_y][location_x + letter] == 'dw':
                            crossword = 2 * crossword
                        elif board[location_y][location_x + letter] == 'tw':
                            crossword = 3 * crossword

                        word_crossword_list.append(crossword)
                else:
                    valid = False
                    break
    if direction == 'down':
        crossword_multiplier = 0
        crossword_addiplier = []
        for letter in range(len(word)):
            if board[location_y + letter][location_x] in blanks:
                crossword = word[letter]
                index = 1
                while location_x - index >= 0:
                    if not(board[location_y + letter][location_x - index] in blanks):
                        crossword = board[location_y + letter][location_x - index] + crossword
                        index += 1
                    else:
                        break
                index = 1
                while location_x + index < board_height:
                    if not(board[location_y + letter][location_x + index] in blanks):
                        crossword += board[location_y + letter][location_x + index]
                        index += 1
                    else:
                        break
                if (len(crossword) == 1) or ((crossword + '\n') in enable1):
                    valid = True
                    if (len(crossword) != 1) and not(letter in blank_indexes):

                        if board[location_y + letter][location_x] == 'dl':
                            crossword += word[letter]
                        elif board[location_y + letter][location_x] == 'tl':
                            crossword += word[letter]
                            crossword += word[letter]
                        elif board[location_y + letter][location_x] == 'dw':
                            crossword = 2 * crossword
                        elif board[location_y + letter][location_x] == 'tw':
                            crossword = 3 * crossword


                        word_crossword_list.append(crossword)
                else:
                    valid = False
                    break
    if valid == True:
        word_bank.append(word)
        directions.append(direction)
        locations.append(board_width * location_y + location_x)
        tiles_used.append(len(hand) - len(availiable_hand))
        crossword_list.append(word_crossword_list)
        #score_subtract_list.append(score_subtract)
        blank_indexes_list.append(blank_indexes)



#Access the dictionary
with open("enable1.txt", mode='r', encoding='utf-8') as enable:
    enable1 = enable.readlines()


while 1 == 1:
    #Edit board

    disable_board_print = 0

    while 1 == 1:
        print()
        print("Edit board:")
        print()
        #Print board for reference
        if disable_board_print == 0:
            print(" _____" * board_width)
            for row in range(board_height):
                print("|", end = ' ')
                for column in range(board_width):
                    if len(board[row][column]) == 1:
                        print("", end = ' ')
                    print(board[row][column], " |", end = ' ')
                print()
                print("|", end = ' ')
                for column in range(board_width):
                    if (board_width * row + column) < 10:
                        print("", end = ' ')
                    if (board_width * row + column) < 100:
                        print("", end = ' ')
                    print(board_width * row + column, "|", end = ' ')
                print()
                print("|", end = '')
                print("_____|" * board_width)



        #Inputs
        word = '!save'
        while (word[0:5] == '!save') or (word[0:5] == '!load'):
            print()
            print("[Leave blank to end]")
            print("[Type !save ____ to save]")
            print("[Type !load ____ to load]")
            word = input("Add word to board: ")
            if word == '':
                print("Done editing.")
                print()
                break
            elif word[0:5] == '!save':
                print("Board saved to file", word[6:])
                f = open(f"SAVEFILE_{word[6:]}", "w")
                json.dump(board, f)
                f.close()
            elif word[0:5] == '!load':
                print("Loading game", word[6:])
                f = open(f"SAVEFILE_{word[6:]}", "r")
                board = json.load(f)
                f.close()
                board_height = len(board)
                board_width = len(board[0])
                if disable_board_print == 0:
                    print(" _____" * board_width)
                    for row in range(board_height):
                        print("|", end=' ')
                        for column in range(board_width):
                            if len(board[row][column]) == 1:
                                print("", end=' ')
                            print(board[row][column], " |", end=' ')
                        print()
                        print("|", end=' ')
                        for column in range(board_width):
                            if (board_width * row + column) < 10:
                                print("", end=' ')
                            if (board_width * row + column) < 100:
                                print("", end=' ')
                            print(board_width * row + column, "|", end=' ')
                        print()
                        print("|", end='')
                        print("_____|" * board_width)
        if word == '':
            break
        print("1: down")
        print("2: right")
        direction = int(input("Direction: "))
        position = int(input("Location: "))
        #Edit board list to include new word (Overwrites dl tl dw and tw!)
        for letter in range(len(word)):
            if direction == 1:
                if (position // board_height) + letter < board_height:
                    board[(position // board_height + letter)][position % board_height] = word[letter]
            else:
                if (position + letter) // board_width == position // board_width:
                    board[position // board_width][position % board_width + letter] = word[letter]



    #Get hand
    valid = False
    while valid == False:
        print("[Leave blank for 7]")
        handSize = input("Enter hand size: ")
        if handSize == '':
            handSize = 7
            valid = True
        elif int(handSize) > 0:
            handSize = int(handSize)
            valid = True
    print()
    print("[Type blank for blank tile]")
    hand = []
    for i in range(handSize):
        valid = False
        while valid == False:
            letter = input(f"Enter letter {i + 1}: ")
            if letter == 'blank':
                hand.append('blank')
                valid = True
            elif len(letter) == 1:
                if 97 <= ord(letter) <= 122:
                    hand.append(letter)
                    valid = True
                elif 65 <= ord(letter) <= 90:
                    hand.append(chr(ord(letter) + 32))
                    valid = True
                else:
                    print("Enter a valid letter.")
            else:
                print("Enter a valid letter.")

    print("Your hand is:", end = ' ')
    for letter in hand:
        if letter == 'blank':
            print('[]', end = ' ')
        else:
            print(chr(ord(letter) - 32), end = ' ')
    print()
    print()


    #New Version

    #Only use words that contain a letter in your hand
    playable_enable1 = []
    if 'blank' in hand:
        playable_enable1 = enable1.copy()
    else:
        for word in enable1:
            word = word.strip()
            if any(letter in word for letter in hand):
                playable_enable1.append(word)


    tiles_to_check = 0
    for row in range(board_height):
        for column in range(board_width):
            playable_spot = False
            if (len(board[row][column]) == 1) or (board[row][column] == '++'):
                playable_spot = True
            if row + 1 < board_height:
                if len(board[row + 1][column]) == 1:
                    playable_spot = True
            if row - 1 >= 0:
                if len(board[row - 1][column]) == 1:
                    playable_spot = True
            if column + 1 < board_width:
                if len(board[row][column + 1]) == 1:
                    playable_spot = True
            if column - 1 >= 0:
                if len(board[row][column - 1]) == 1:
                    playable_spot = True
            if playable_spot == True:
                tiles_to_check += 1

    word_bank = []
    directions = []
    locations = []
    tiles_used = []
    crossword_list = []
    score_subtract_list = []
    blank_indexes_list = []

    print("Calculating availiable words...", end ='')
    playable_tiles_ran = 0
    percentage_completed = 0

    #Find all spots that are playable
    playable_locations = []

    for row in range(len(board)):

        for column in range(len(board[row])):

            playable_spot = False

            if (len(board[row][column]) == 1) or (board[row][column] == '++'):
                playable_spot = True
            if row + 1 < board_height:
                if len(board[row + 1][column]) == 1:
                    playable_spot = True
            if row - 1 >= 0:
                if len(board[row - 1][column]) == 1:
                    playable_spot = True
            if column + 1 < board_width:
                if len(board[row][column + 1]) == 1:
                    playable_spot = True
            if column - 1 >= 0:
                if len(board[row][column - 1]) == 1:
                    playable_spot = True

            if playable_spot == True:
                playable_locations.append([row, column])

    #Try every word at each playable location
    for location in playable_locations:

        playable_tiles_ran += 1
        if math.floor(10 * ((playable_tiles_ran - 1) / tiles_to_check)) > percentage_completed:
            percentage_completed = math.floor(10 * ((playable_tiles_ran - 1) / tiles_to_check))
            print(str(percentage_completed * 10) + '%', end=', ')

        for word in playable_enable1:

            word = word.strip()

            #For debugging one word, majorly speeds up process
            ###if word != 'hooey':
            ###    continue

            #Use offsets right
            if not([location[0], location[1] - 1] in playable_locations):

                for offset in range(len(word)):

                    #If left side is on the board
                    if location[1] - offset >= 0:

                        #If right side is on the board
                        if location[1] - offset + len(word) <= board_width:

                            check_letters(word, location[0], location[1] - offset, 'right')

            #Don't use offsets right
            else:

                #Left side is on board by default, check if right side is on the board
                if location[1] + len(word) < board_width:

                    check_letters(word, location[0], location[1], 'right')

            #Use offsets down
            if not([location[0] - 1, location[1]] in playable_locations):

                for offset in range(len(word)):

                    #If top is on the board
                    if location[0] - offset >= 0:

                        #If bottom is on the board
                        if location[0] - offset + len(word) <= board_height:

                            check_letters(word, location[0] - offset, location[1], 'down')

            #Don't use offsets down
            else:

                #Top is on board by default, check if bottom is on the board
                if location[0] + len(word) < board_height:

                    check_letters(word, location[0], location[1], 'down')



    print("done.")
    ###print("Availiable words:", word_bank)
    print("Calculating point values...", end = '')

    #Find most points
    best_score = 0
    perfect_words = []
    perfect_directions = []
    perfect_locations = []
    for word in range(len(word_bank)):


        word_score = []
        score_modifier = 1

        #Display word tested
        ###print("Calculating", word_bank[word])
        ###print("Facing", directions[word])
        ###print("At location", locations[word])
        for letter in range(len(word_bank[word])):
            if not(letter in blank_indexes_list[word]):
                if directions[word] == 'down':

                    board_square = board[(int(locations[word]) // board_width) + letter][int(locations[word]) % board_width]
                    #Display location
                    ###print("Row", (int(locations[word]) // board_width) + letter, "Column", int(locations[word]) % board_width)
                    ###print(">Letter", letter, "location currently:", int(locations[word]) + board_width * letter, "which is", board_square)
                    if board_square == 'dl':
                        word_score.append(2 * values[word_bank[word][letter]])
                    elif board_square == 'tl':
                        word_score.append(3 * values[word_bank[word][letter]])
                    elif board_square == 'dw':
                        word_score.append(values[word_bank[word][letter]])
                        score_modifier *= 2
                    elif board_square == 'tw':
                        word_score.append(values[word_bank[word][letter]])
                        score_modifier *= 3
                    else:
                        word_score.append(values[word_bank[word][letter]])
                    #Display cumulative value, letter by letter
                    ###print(">Value of" , word_bank[word][letter], "is", values[word_bank[word][letter]])
                    ###print(">After letter", str(letter) + ",", sum(word_score), "points")
                else:

                    board_square = board[int(locations[word]) // board_width][(int(locations[word]) % board_width) + letter]
                    #Display location
                    ###print("Row", int(locations[word]) // 15, "Column", (int(locations[word]) % 15) + letter)
                    ###print(">Letter", letter, "location currently:", int(locations[word]) + letter, "which is", board_square)
                    if board_square == 'dl':
                        word_score.append(2 * values[word_bank[word][letter]])
                    elif board_square == 'tl':
                        word_score.append(3 * values[word_bank[word][letter]])
                    elif board_square == 'dw':
                        word_score.append(values[word_bank[word][letter]])
                        score_modifier *= 2
                    elif board_square == 'tw':
                        word_score.append(values[word_bank[word][letter]])
                        score_modifier *= 3
                    else:
                        word_score.append(values[word_bank[word][letter]])
                    #Display cumulative value, letter by letter
                    ###print(">Value of" , word_bank[word][letter], "is", values[word_bank[word][letter]])
                    ###print(">After letter", str(letter) + ",", sum(word_score), "points")

        #Remove points if used blank letter
        #print("Subtracting", score_subtract_list[word], "points due to blank tiles")
        #word_score.append(-1 * score_subtract_list[word])
        #print("Score is now", sum(word_score))

        #Multiply by score modifier (For double and triple words)
        word_score *= score_modifier
        ###print(">>Score modifier is", score_modifier, "for a score of", sum(word_score))

        #Add 35 points if you used all your letters
        if tiles_used[word] == 7:
            word_score.append(scrabble_point_value)

        #Add crossword points
        ###print("Crosswords are:", crossword_list)
        for crossword_words in crossword_list[word]:
            for crossword_letter in crossword_words:
                word_score.append(values[crossword_letter])
        
        #Display final score
        ###print(">>Word score is", sum(word_score))
        if sum(word_score) > best_score:
            perfect_words = [word_bank[word]]
            perfect_directions = [directions[word]]
            perfect_locations = [locations[word]]
            best_score = sum(word_score)
        elif sum(word_score) == best_score:
            perfect_words.append(word_bank[word])
            perfect_directions.append(directions[word])
            perfect_locations.append(locations[word])

    print("done.")
    print()
    print("Best move", end = '')
    if len(perfect_words) > 1:
        print("s", end = '')
    print(": ", end = '')
    if len(perfect_words) > 0:
        for word in range(len(perfect_words) - 1):
            print(perfect_words[word], "facing", perfect_directions[word], "at tile number", str(perfect_locations[word]) + ",", end = ' ')
        print(perfect_words[len(perfect_words) - 1], "facing", perfect_directions[len(perfect_words) - 1], "at tile number", perfect_locations[len(perfect_words) - 1])

        print("Score:", best_score)
    else:
        print("No words availiable.")
    print()
    input("Press enter to continue.")