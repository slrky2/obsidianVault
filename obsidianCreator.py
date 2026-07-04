import os
import frontmatter 
import yaml
from pathlib import Path
# C:\Users\Saad\Desktop\Brain

# todo need a function that checks if a file exist

# WARNING THIS FUNCTION CAN DELETE PREVIOUSLY SAVED FOLDERS

def writeToFile(toBePublished):
    os.makedirs(toBePublished.path, exist_ok = True) # checks, else creates FOLDERS
    temp = f'{toBePublished.title}.md'
    with open(Path(toBePublished.path) / temp, 'w', encoding='utf-8') as file:
        file.write('---\n')
        yaml.dump(toBePublished.data, file, sort_keys=False )
        file.write('---\n')

        file.write(toBePublished.contents)

        #COMMENTED OUT FOR NOW
        # for tag in toBePublished.tags:
        #     fix = '[[' + tag + ']]'
        #     file.write(fix)
        #     file.write(' ')

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

#deprecated
def getNewTags(path, tags):
    return {tag for tag in tags if not doesFileExist(path, tag)}

# we need to add a deque

class md_file:
    def __init__(self, data, path, topic, tags, blurb):
        self._data = data
        self._path = path
        self._topic = topic
        self._tags = tags
        self._blurb = blurb

    @property
    def data(self):
        return self._data

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

#if post is empty then dont run this method
def parse(filename, dest_path=None):
    filename = Path(filename)
    # default: write back into the same directory the file was read from (in-place)
    if dest_path is None:
        dest_path = filename.parent
    with open(filename, encoding='utf-8') as f:
        data, contents = frontmatter.parse(f.read())
        title = data.get('title', filename.stem)
        tags = data.get('tags', [])
        Document = md_file(data, dest_path, title, tags, contents)
    return Document


if __name__ == '__main__':
    document = parse('prototype.yaml')
    writeToFile(document)
    print('successfulyl written:', document.title)
