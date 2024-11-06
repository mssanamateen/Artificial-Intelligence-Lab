import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word=random.choice(word_list)
guess=input("Guess a letter:")
for i in range(len(chosen_word)):
  
	if guess in chosen_word[i]:
    
		print("correct guess")
  
	else:
    
		print("wrong guess")