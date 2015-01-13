import random

randomwords = ["red", "blue", "black", "orange"]
index = random.randint(0,len(randomwords)-1)
s = ""

guesscount = 0

secretword = randomwords[index]

print (secretword)

for i in secretword:
	s = s + "_"

guessedletters = []

while True:
	print s
	guess = raw_input("Choose a letter ")

	if guess not in guessedletters:
		guessedletters.append(guess)

		if guess in secretword:
			index = secretword.find(guess)
			s = s[:index] + guess + s[index + 1:]
			if secretword == s:
				print 'You win!'
				break


		else:
			guesscount = guesscount + 1
			if guesscount > 6:
				print "You Suck"
				break

	else:
		print "You already guessed that letter"


