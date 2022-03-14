import sys
import random

print('Welcome to Hangman.')

topic_dict = {
  '1': 'books',
  '2': 'movies',
  '3': 'words',
  '4': 'cosmere'
}
 
print('1. Books\n2. Movies\n3. Dictionary Words\n4. Cosmere')

index = input('Select the index of your topic of choice: ')
print('\n')

if index not in topic_dict.keys():
  print('Invalid Topic Index.')
  sys.exit()    #kills process

#parses required file for words
topic = topic_dict[index]+".txt"
topic_wrds = []
file = open(topic, "r")
for i in file:
  topic_wrds.append(i)
file.close()

#picks random word from list
word = list(random.choice(topic_wrds))
word.pop()
word = ''.join(word)

word_l = []
word_gsd = []
word_strp = word
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~ 1234567890'''
forb = '''!()-[]{};:'"\,<>./?@#$%^&*_~ 1234567890aeiou'''

#for length of word, disregarding punctuations and whitespace
for ele in word_strp:
    if ele in punc:
        word_strp = word_strp.replace(ele, "")

#initializing required variables with chosen word
for i in word:
  word_l.append(i)
  if i not in forb:
    word_gsd.append('_')
  else:
    word_gsd.append(i)

#lives lost tracker
counter = 0

print('Your word is', len(word_strp), 'letters long.')
print(''.join(word_gsd))
print('\n')

#main game loop
while counter < 8:
  guess = str(input('Guess a letter: '))
  
  if guess not in alph:
    print('\n')
    print('Invalid Input. Try Again.')
  elif guess in word_l:
    if guess in word_gsd:
      print('\n')
      print("You have already guessed this word.\nNote that all vowels are already revealed.")
    else:
      for i in range(len(word_l)):
        if word_l[i] == guess:
          word_gsd[i] = guess
      print('\n')
      print('Correct')
  else:
    counter += 1
    print('\n')
    print('Incorrect')
  
  print(''.join(word_gsd))
  print(8 - counter, 'lives left')
  print('\n')

  if '_' not in word_gsd:
    print("You Win! The word was:", word)
    break
  elif counter == 8:
    print("You Lost... The word was:", word)
    break