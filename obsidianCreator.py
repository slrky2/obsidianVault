import os
import frontmatter 
from pathlib import Path
# C:\Users\Saad\Desktop\Brain

# todo need a function that checks if a file exist

# WARNING THIS FUNCTION CAN DELETE PREVIOUSLY SAVED FOLDERS

def writeToFile(toBePublished):
    os.makedirs(toBePublished.path, exist_ok = True) # checks, else creates FOLDERS
    temp = f'{toBePublished.title}.md'
    with open(Path(path) / temp, 'w') as file:
        file.write(toBePublished.contents)
        for tag in toBePublished.tags:
            fix = '[[' + tag + ']]'
            file.write(fix)
            file.write(' ')

def doesFileExist(path, tag):
    tag = f'{tag}.md'
    file_path = Path(path) / tag
    if file_path.exists():
        #check if the file is empty / or maybe if it doesnt contain any links
        # print('path exists! : checking contents')
        content = file_path.read_text()
        if content == '':
            return False
        else:
            return True
    else: 
        return False

# we need to add a deque

class md_file:
    def __init__(self, path, topic, tags, blurb):
        self._path = path
        self._topic = topic
        self._tags = tags
        self._blurb = blurb

    @property
    def path(self):
        return self._path

    @property
    def title(self):
        return self._topic

    @property
    def tags(self):
        return self._tags
    
    @property
    def contents(self):
        return self._blurb

path = r'C:\Users\Saad\Desktop\Brain\Brain' # Windows
# path = '/Users/saadkapadia/obsidian_Vault' # MAC

#if post is empty then dont run this method
def parse(filename):
    with open(filename) as f:
        data, contents = frontmatter.parse(f.read())
        Document = md_file(
            path,
            data['title'],
            data['tags'],
            contents,
        )
    return Document


if __name__ == '__main__':
    document = parse('prototype.yaml')
    writeToFile(document)
    print('successfulyl written:', document.title)
