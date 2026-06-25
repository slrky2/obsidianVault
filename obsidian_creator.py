import os
import frontmatter 
# C:\Users\Saad\Desktop\Brain

# todo need a function that checks if a file exist

# WARNING THIS FUNCTION CAN DELETE PREVIOUSLY SAVED FOLDERS


def writeToFile(toBePublished):
    os.makedirs(path, exist_ok = True) # checks, else creates FOLDERS
    temp = f'{toBePublished.title}.md'
    with open(os.path.join(path, temp), 'w') as file:
        file.write(toBePublished.contents)

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

# path = 'Users\Saad\Desktop\Brain'

path = '/Users/saadkapadia/obsidian_Vault'
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

document = parse('prototype.yaml')
print(document.title)

writeToFile(document)

# document.contents