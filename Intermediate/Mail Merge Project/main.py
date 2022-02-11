#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
name_list = []

with open("../Mail Merge Project Start/Input/Names/invited_names.txt", "r") as names:
    for name in names.readlines():
        name_list.append(name.rstrip("\n"))

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter = starting_letter.read()

for name in name_list:
    with open(f"../Mail Merge Project Start/Output/ReadyToSend/{name}.txt", "w") as invitation:
        new_letter = letter.replace("[name]", name)
        invitation.write(new_letter)

    



