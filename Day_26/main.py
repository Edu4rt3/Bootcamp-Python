# NATO alphabet


import pandas 

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    name = input("What's your name?: ").upper()
    try:
        result = [phonetic_dict[letter] for letter in name]
        
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)
generate_phonetic()