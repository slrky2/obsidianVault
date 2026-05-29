#Copyright Saad Kapadia 2026

import os # Needed to manage files and os level things
# C:\Users\Saad\Desktop\Brain

# todo need a function that checks if a file exists

def check_file(path, filename, contents):
    os.makedirs(path, exist_ok = True) # checks/creates FOLDERS! 

    with open(os.path.join(path, filename), 'w') as file:
        file.write(contents)
    
#driver here!! this is what make it works
path = input('this is a driver: now give me a filename ! >:) : ')
file = input('what do you wanna call the file? ')
q = input('what you want to put in it? ')
check_file(path, file, q)

