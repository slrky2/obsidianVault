import obsidianCreator
from collections import deque
# from collections import defaultdict
from pathlib import Path
import json

# this is the driver, will prompt multiple times and make multiple files  

toWrite = deque() # empty

#we need to setup a dict aswell as an external file that we retrieve and read from

# remember that the difference between a set and a list is the fact that a list allows duplicates

stats = {
    'topics': set(),
    'newTopics': set()
}
# provide some md files: this is AI's job

path = input('where are the files that need to be process located? input -none- = terminate & save: ')
# path = r'C:\Users\Saad\Downloads\seed-vault-notes\01-CS-Programming'
if path == '-none-':
    print('programmed stopped (user ended)')
else:
    # given = Path(r"\Users\Saad\Downloads\seed-vault-notes\01-CS-Programming") # REAL VERSION: ASK FOR A FILEPATH
    given = Path(path)
    if given.is_dir(): # check if its an actual folder/ location
        files = [f.name for f in given.iterdir() if f.is_file()]
    for file in files: # for each of the files
        toWrite.append(file) # add the written files to the queue

    stats["topics"] = list(toWrite) 

    destPath = Path(r"C:\Users\Saad\Desktop\Brain\Brain") # REAL VERSION: ASK FOR A DEST PATH

    for files in stats["topics"]:
        document = obsidianCreator.parse(given / files)
        obsidianCreator.writeToFile(document)
        # print(document.title, document.tags)
        for tag in document.tags:
            if not obsidianCreator.doesFileExist(destPath, tag): #if the topic doesnt exist
                stats["newTopics"].add(tag) #TODO there may come a time where we have to prioritize some topics over others
                # this could be done using a bst

print('wrote: ', stats["topics"])
print('recommend: ', stats["newTopics"])