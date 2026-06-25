import os
import frontmatter 
# C:\Users\Saad\Desktop\Brain

# todo need a function that checks if a file exist

# WARNING THIS FUNCTION CAN DELETE PREVIOUSLY SAVED FOLDERS


def writeToFile(toBePublished):
    os.makedirs(path, exist_ok = True) # checks, else creates FOLDERS
    with open(os.path.join(toBePublished.path, toBePublished.title), 'w') as file:
        file.write(toBePublished.contents())

class md_file:

    def __init__ (self, path, topic, tags, blurb):
        self._path = path
        self._topic = topic
        self._tags = tags
        self._blurb = blurb

    @property
    def path(self):
        return self.path
    
    @property
    def title(self):
        return self.title

    def contents(self):
        print(self.path, self.topic, self.tags, self.blurb, sep='\n')

path = 'Users\Saad\Desktop\Brain'

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
document.contents()

#C:\Users\Saad\Desktop\stupid
