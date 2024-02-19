# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
placeholder = "[name]"

with open("../Mail Merge Project Start/Input/Names/invited_names.txt", "r") as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_content = letter_file.read()  # Read the entire content as a single string
    for name in names:
        st_name = name.strip()
        new_letter = letter_content.replace(placeholder, st_name)  # Strip newline characters from name
        with open(f"./Output/ReadyToSend/Letter_for_{st_name}.txt", "w") as complete_letter:
            complete_letter.write(new_letter)

