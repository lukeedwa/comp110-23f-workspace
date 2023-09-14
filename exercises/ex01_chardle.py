"""EX01 - Chardle -First Step Towards Wordle"""
__author__ = "730661236"


user_word: str = input("Enter a 5-character word: ")
word_length: int = len(user_word)
if word_length != 5:
    exit(print("Error: Word must contain 5 characters"))

user_letter: str = input("Enter a single character: ")
letter_length: int = len(user_letter)
if letter_length != 1:
    exit(print("Error: Character must be a single character."))
print("Searching for " + user_letter + " in " + user_word)

total_number: int = 0
if user_word[0] == user_letter:
    print(user_letter + " found at index 0")
    total_number = (total_number + 1)
if user_word[1] == user_letter:
    print(user_letter + " found at index 1")
    total_number = (total_number + 1) 
if user_word[2] == user_letter:
    print(user_letter + " found at index 2")
    total_number = (total_number + 1)
if user_word[3] == user_letter:
    print(user_letter + " found at index 3")
    total_number = (total_number + 1) 
if user_word[4] == user_letter:
    print(user_letter + " found at index 4")
    total_number = (total_number + 1)

if 0 == int(total_number):
    print("No instances of " + user_letter + " found in " + user_word)
if 1 == int(total_number):
    print(str(total_number) + " instance of " + user_letter + " found in " + user_word)
if 1 < int(total_number):
    print(str(total_number) + " instances of " + user_letter + " found in " + user_word)
