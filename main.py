# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close() #to free up some resources 

# #we might forget to add the close statement in the end 
# #another way to use a file is 
# # using the with keyword

# with open("my_file.txt", mode='a') as file_2:
#     # contents2=file_2.read()n
#     file_2.write("Eminem OP hai bhai ")
#     # print(contents2)
PLACEHOLDER = "[name]"
with open("Input/Names/names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("Input/LetterTemplate/letterbody.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"Output/letter_for_{stripped_name}",'w') as completed_letter:
            completed_letter.write(new_letter)
