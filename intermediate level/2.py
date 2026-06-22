import random
#function to choose a random word and hint
def get_word():
    words={
        "Python":"Programming language",
        "Computer":"Electronic device",
        "Elephant":"Largest land Animal",
        "School":"Place of learning",
        "Internet":"Global network",
        "Keyboard":"Input device",
        "Database":"Stores data",
        "Football":"Popular sport",
        "Hospital":"Place of treatment",
        "Library":"Collection of books"
        }
    word=random.choice(list(words.keys()))
    
    hint=words[word]
    return word,hint

#function to display the current progress
def display_word(word,guessed_letters):
    display=""
    for letter in word:
        if letter in guessed_letters:
            display+=letter+""
        else:
            display+="_"
    return display

#main hungman function
def play_hungman():
    word,hint=get_word()
    word=word.lower()
    guessed_letters=[]
    attempts=6

    print("======Hangman Game======")
    print("Hint:",hint)

    while attempts>0:
        current_word=display_word(word,guessed_letters)
        print("\nWord:",current_word)

        if "_" not in current_word:
            print("\n congratulation! you guessed the word",word)
            return
        guess=input("Enter a letter:").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print("Correct Guess!")
        else:
            attempts-=1
            print("Wrong guess!")
            print("Attempts remaining:",attempts)
    print("\n Game Over")
    print("The word was ",word)
play_hungman()
        
    
        
