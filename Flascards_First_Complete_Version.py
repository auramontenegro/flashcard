# Flaschards_First_Complete_Version.py

"""
This flashcard program allows the user to ask for a
glossary entry.
In response, the program randomly picks an entry from all
glosary entries. It shows the entry.
After the user presses return, the program shows the
definition of that particular entry.
The user can repeatedly ask for an entry and also
has the option to quit the program
"""
from random import *

def show_flashcard():
    """Show_flashcard
    it shows a glossary entry to the user, if the user presses
    return the corresponding definition is printed if the user presses
    'quit' it quits.
    """
    random_key = choice(list(glossary))
    print('define: ', random_key)
    
    input("Press return to see the definition ")
    print(glossary[random_key])
    
      

# Set up glossary
glossary = {'word1':'definition1',
            'word2':'definition2',
            'word3':'definition3'}

# The interactive loop
exit = False
while not exit:
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')


