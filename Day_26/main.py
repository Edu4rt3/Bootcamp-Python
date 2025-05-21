# NATO alphabet


import pandas 

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

name = input("What's your name?: ").upper()

result = [phonetic_dict[letter] for letter in name]
print(result)