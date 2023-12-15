#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def Main():
    with open("Input/Letters/starting_letter.txt", "r+") as file:
        invitation = file.read()
    with open("Input/Names/invited_names.txt", "r+") as file:
        names = file.read().splitlines()

    for name in names:
        with open("Output/ReadyToSend/" + name + "_letter.txt", "w") as file:
            file.write(invitation.replace('[name]', name))

if __name__ == '__main__':
    Main()