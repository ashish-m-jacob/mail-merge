# Getting base letter
with open("Input/Letters/starting_letter.txt") as base_letter:
    template = base_letter.read().split(" ")

# Getting list of names to send the letters to
with open("Input/Names/invited_names.txt") as invited_names:
    names = invited_names.read().split("\n")


# Creating all letters
for i in range(len(names)):
    with open(f"Output/ReadyToSend/letter_for_{names[i]}", mode="w") as letter:
    # Replacing placeholder with name from the list
        template[1] = f"{names[i]},\n\nYou"
        new_letter = " ".join(template)

        letter.write(new_letter)
