import random



FILE_NAME = 'word-list.txt'
MISSES_ALLOWED = 6

# expects words to be seperated by newlines
def read_file(file_name):
    file = open(file_name, 'r')
    lines = file.read().splitlines()
    return lines

def update_letters_found(letters_found, guess, secretword):
    index = 0
    while index < len(secretword):
        index = secretword.find(guess, index)
        if index == -1:
            break
        letters_found = letters_found[:index] + guess + letters_found[index + 1:]
        index += 1
    return letters_found

def hangman(guesscount):
    if guesscount == 1: print "O"
    if guesscount == 2: print """ O
/
                                """
    if guesscount == 3: print """  O
 \/
"""
    if guesscount == 4: print """  O
 \|/
 """
    if guesscount == 5: print """  O
 \|/
 /
 """
    if guesscount == 6: print """

  +----------+
  |          |
  O          |
 \|/         |
 / \\        |
 ==============
 """


randomwords = read_file(FILE_NAME)
index = random.randint(0,len(randomwords)-1)

# letters_found starts off as empty, then gets filled with underscores (1 for each letter in secret_word)
# Then letters_found represents which letters the player has correctly guess.
letters_found = ""

guesscount = 0

secretword = randomwords[index]

print (secretword)

for i in secretword:
    letters_found = letters_found + "_"

guessed_letters = []

while True:
    print letters_found
    guess = raw_input("\nChoose a letter ")
    guess = guess[:1]

    if guess not in guessed_letters:
        guessed_letters.append(guess)

        if guess in secretword:
            letters_found = update_letters_found(letters_found, guess, secretword)
            if secretword == letters_found:
                print secretword
                print '\nYou win!'
                break
        else:
            guesscount += 1
            hangman(guesscount)
            if guesscount >= MISSES_ALLOWED:
                print "You Suck. GAME OVER"
                break



            print str(MISSES_ALLOWED - guesscount) + ' guesses left.'






    else:
        print "You already guessed that letter"


