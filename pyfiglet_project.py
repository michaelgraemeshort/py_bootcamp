from pyfiglet import figlet_format
from termcolor import colored

text = input("What would you like to print?: ")
colour_chosen = input("What colour?: ")
spam = figlet_format(text)
eggs = colored(spam, colour_chosen)
print(eggs)