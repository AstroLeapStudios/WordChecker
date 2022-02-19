from operator import truediv
import os
from termcolor import cprint
from pyfiglet import figlet_format

os.system("title Word Checker")
cprint(figlet_format('WrdChckr', font='big'),
       'blue', attrs=['bold'])
print("Add the .txt file to the directory of this code.\n ")

while True:
       fileName = input("Name of the .txt file (excluding the file extension): ")

       file = open(f"{fileName}.txt",encoding='latin-1')
       full_text = file.read()

       print(f"\nFile ({fileName}.txt) contains {len(full_text)} characters. \n")

       num = input("How many words would you like to check for?: ")
       print("\n")
       n = range(int(num))

       for i in n:
              word = input(f"Word {i + 1}: ")
              count = 0 
              l = full_text.split(" ")
              for c in l:
                     if(c.upper() == word.upper()):
                            count += 1
              print(f"{fileName}.txt includes the word {word} {count} times \n")