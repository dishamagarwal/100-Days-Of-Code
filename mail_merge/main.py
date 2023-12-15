#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

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