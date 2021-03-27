import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

user_word = input("Enter a word: ")
nato_code_user_word = [nato_alphabet_dict[letter.upper()] for letter in user_word]
print(nato_code_user_word)
