import random




graphics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  ,----..      ,---,               ,'  , `.    ,---,.           /   /   \                  ,---,.,-.----.    
 /   /   \    '  .' \           ,-+-,.' _ |  ,'  .' |          /   .     :        ,---.  ,'  .' |\    /  \   
|   :     :  /  ;    '.      ,-+-. ;   , ||,---.'   |         .   /   ;.  \      /__./|,---.'   |;   :    \  
.   |  ;. / :  :       \    ,--.'|'   |  ;||   |   .'        .   ;   /  ` ; ,---.;  ; ||   |   .'|   | .\ :  
.   ; /--`  :  |   /\   \  |   |  ,', |  '::   :  |-,        ;   |  ; \ ; |/___/ \  | |:   :  |-,.   : |: |  
;   | ;  __ |  :  ' ;.   : |   | /  | |  ||:   |  ;/|        |   :  | ; | '\   ;  \ ' |:   |  ;/||   |  \ :  
|   : |.' .'|  |  ;/  \   \'   | :  | :  |,|   :   .'        .   |  ' ' ' : \   \  \: ||   :   .'|   : .  /  
.   | '_.' :'  :  | \  \ ,';   . |  ; |--' |   |  |-,        '   ;  \; /  |  ;   \  ' .|   |  |-,;   | |  \  
'   ; : \  ||  |  '  '--'  |   : |  | ,    '   :  ;/|         \   \  ',  /    \   \   ''   :  ;/||   | ;\  \ 
'   | '/  .'|  :  :        |   : '  |/     |   |    \          ;   :    /      \   `  ;|   |    \:   ' | \.' 
|   :    /  |  | ,'        ;   | |`-'      |   :   .'           \   \ .'        :   \ ||   :   .':   : :-'   
 \   \ .'   `--''          |   ;/          |   | ,'              `---`           '---" |   | ,'  |   |.'     
  `---`                    '---'           `----'                                      `----'    `---'  
''']


def greet_user():  # greet user with a hangman message
    print('H A N G M A N')


def play_game():
    play_or_exit = input('Type "play" to play the game, "exit" to quit: ').strip()
    print()
    if play_or_exit == 'play':
        start_game()
        return True
    else:
        quit()


def picking_word():
    word = ['python', 'java', 'kotlin', 'javascript']  # list of words to be picked
    random_word = random.choice(word)  # from the random module, picks random item from list
    return list(random_word)


def setup_empty_game():
    global chosen_word  # global variable so that the return value from picking_word can be used in another function without calling it again (if it is called again, word could change)
    chosen_word = picking_word()  # each time setup_empty_game is called, new word will be picked
    empty_game = []
    empty_game[:] = '-' * len(chosen_word[:])  # take the length of the letters in chosen word and create a list only
    # showing dashes
    return empty_game


def start_game():
    used_letters = set()  # set instead of a list so it only shows one instance of the duplicated value
    empty_slots = setup_empty_game()  # empty slots will be updated as user inputs guesses
    counter = 0  # set up a counter to make sure user does go over 8 attempts (for wrong letters picked)
    while counter < 8:
        print(''.join(empty_slots))  # show the how the slots are looking after each input
        if empty_slots == chosen_word:  # if the empty slots matches the chosen word, user has won, break out of while
            print('You guessed the word!')  # this goes before input so that if user has won early, no need to cont.
            print('You survived!')
            print()
            play_game()
            print()
        letter = input('Input a letter: ')
        if letter.islower() and letter.isalpha() and len(letter) == 1:  # this entire if statement checks for proper input
            pass
        elif len(letter) > 1:  # should be 1 character long
            print('You should input a single letter')
            print()
            continue
        else:
            print("Please enter a lowercase English letter")  # should be a lowercase alphabetic character
            print()
            continue
        if letter in used_letters:
            print("You've already guessed this letter")
            print()
            continue
        if letter not in ''.join(chosen_word):  # if the letter input is not in the str(chosen_word)
            print("That letter doesn't appear in the word")  # tell user that it does not appear
            used_letters.add(letter)
            if counter == 7:  # if the counter has reached 7 and the first if did not execute, user has lost
                print('You lost!')
                print(graphics[len(graphics)-1])
                print()
                play_game()
                print()
            print(graphics[counter])
            counter += 1  # each time user enters letter that is not in the chosen word, add an attempt to the counter
            print()
            continue
        else:
            used_letters.add(letter)
        for i in range(0, len(chosen_word)):  # loops over each index in the chosen word
            if letter == chosen_word[i]:  # if the input letter is found in any index
                empty_slots[i] = letter  # in the identical indexes inside of empty_slots, replace those '-', with letter
                print()


greet_user()
play_game()
