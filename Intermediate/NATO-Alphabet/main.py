import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    text = input("Enter a word: ").upper()
    try:
        result = [data_dict[letter] for letter in text]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(result)
        break









# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
#
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
