import pandas


def generate_phonetic():
    nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
    user_word = [*input("Enter a word: ").upper()]
    row = {row.letter: row.code for (index, row) in nato_phonetic.iterrows()}
    try:
        res = [row[res] for res in user_word]
    except KeyError:
        print("Sorry? but NATO doesn't have symbols you did input")
        generate_phonetic()
    else:
        print(res)


generate_phonetic()
