#tells script to add argv for input
from sys import argv

#command line input is the script name and the file name
script, filename = argv

#txt variable is used to open the inputted files name
txt = open(filename)

#shows text with the filename inputted
print(f"Here's your file {filename}:")
#shows the text from the txt variable and uses read command to show all the contants of the file
print(txt.read())

txt.close()

#shows text on screen
print("Type the filename again:")

#creates input prompt
file_again = input("> ")

#tells script to open the inputted file name
txt_again = open(file_again)

#opens the file again and displays the contents
print(txt_again.read())

txt_again.close()
