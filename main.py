import obsidianCreator
from collections import deque
from pathlib import Path

# this is the driver, will prompt multiple times and make multiple files  

toWrite = deque() # empty

#we need to setup a dict aswell as an external file that we retrieve and read from

stats = {}

# provide some md files: this is AI's job

# path = input('where are the files that need to be process located? input -none- = terminate & save: ')
# path = r'C:\Users\Saad\Downloads\seed-vault-notes\01-CS-Programming'

#term for this is globbing i think??
given = Path(r"\Users\Saad\Downloads\seed-vault-notes\01-CS-Programming") # REAL VERSION: ASK FOR A FILEPATH
if given.is_dir():
   files = [f.name for f in given.iterdir() if f.is_file()] 
   for file in files:
      toWrite.append(file) # add to the queue

stats["todo"] = list(toWrite)

destPath = Path(r"C:\Users\Saad\Desktop\Brain\Brain") # REAL VERSION: ASK FOR A DEST PATH

for files in stats["todo"]:
    document = obsidianCreator.parse(given / files)
    obsidianCreator.writeToFile(document)
    print(document.title, document.tags)
    for tag in document.tags:
        if not obsidianCreator.doesFileExist(destPath, tag): #if the topic doesnt exist 
            print(tag, 'does not exist!')
            #TODO ADD TO DEQEUE!!!

#given that we have got this stuff down just make this loopable aswell as adding the json conversion of the dictionary
