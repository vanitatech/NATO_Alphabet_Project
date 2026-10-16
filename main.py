
import pandas

# Create a dictionary in this format:

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in alphabets.iterrows()}

#Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try: 
        phonetic_code_words = [nato_alphabet[letter] for letter in user_word]
    except KeyError:
        print(f"Sorry, only letters in the alphabet are allowed. Please try again.")
        generate_phonetic()
    else:
        print(phonetic_code_words)

generate_phonetic()
    