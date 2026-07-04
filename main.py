import obsidianCreator
import os
from anthropic import Anthropic
from collections import deque
from pathlib import Path
import json
from dotenv import load_dotenv
load_dotenv()

toWrite = deque()
# difference between a set and list is set doesnt allow duplicates
stats = {
    'topics': set(),
    'newTopics': set(),
    'createdFiles': {}
}

def importNotes(filepath, destPath=None):
    if(destPath == None): destPath = filepath
    # first we open the given directory
    if filepath.is_dir():
        files = [f.name for f in filepath.iterdir() if f.is_file() and f.suffix == '.md']
    else:
        print(f'not a directory: {filepath}')
        return False

    # read the files we need to write
    for file in files:
        stats['topics'].add(file)
        print('found : ', filepath/file)
        if not obsidianCreator.doesFileExist(VAULT_DIR, file):
            document = obsidianCreator.parse(filepath/file, destPath)
            obsidianCreator.writeToFile(document)
            print('wrote: ', document.path)
            new_tags = document.tags
            stats['newTopics'].update(new_tags)
            print('found new tags: ', stats['newTopics'])

        else: print('file already exists!!!')

#TODO WE SHOULD ADD A WHAT DO YOU WANT TO LEARN? (opening prompt to get the ball rolling)
client = Anthropic(
    api_key=os.environ.get('ANTHROPIC_API_KEY'),
)
# dir = input('where do you want to store the vault?')
 

# single directory to both read from and write/update in place
VAULT_DIR = Path(r'C:\Users\Saad\Desktop\Brain\basic_test')

# user = input('do u want to import some notes? (Y/N)')

# if (user.casefold() == 'y'):


while True:
    # path = input('where are the files that need to be process located? input -none- = terminate & sa1ve: ')
    path = VAULT_DIR
    destPath = path # we are working in a single directory most of the time!
    if path == '-none-':
        print('programmed stopped (user ended)')
        # TODO we need a lambda to convert the sets to lists
        # with open('savedStatus', 'w') as f:
            # f.write(json.dumps(stats))
            # we likely dont need that aslong as we parse and check properly and startup
            # this approach would save us from another confusing overhead that we read from
        break
    
    test = Path(r'C:\Users\Saad\Downloads\webdev-vault-notes\webdev-vault\02-Learning')
    importNotes(test, VAULT_DIR)

    # given = Path(r"C:\Users\Saad\Downloads\seed-vault-notes\02-Learning") # REAL VERSION: ASK FOR A FILEPATH


    print(f'wrote {len(stats["topics"])} file(s): {stats["topics"]}')    
    ans = input(f'recommended {len(stats["newTopics"])} new topic(s): {stats["newTopics"]} — write them? (Y/N): ')
    if ans == 'Y' or ans == 'y':
        SCHEMA_PROMPT = """You are a notetaker for an Obsidian vault. For the given topic, write a single markdown note with YAML frontmatter followed by a markdown body.

Frontmatter format:
---
title:
type: concept | project | reference | log
domain: cs | general | football | meta
tags: []
status: seed | growing | mature
created: YYYY-MM-DD
related: ["[[Note Name]]", ...]
source:
---

Body: a # header matching the title, then sections: Key Points, Example (with real code if relevant), Why It Matters, Open Questions.

Output ONLY the note content (frontmatter + body). No preamble,  explanation, no markdown code fences around the whole thing."""

        for topic in stats['newTopics']:
            message = client.messages.create(
                model='claude-haiku-4-5',
                max_tokens=1024,
                system=SCHEMA_PROMPT,
                messages=[
                    {
                        "role": "user",
                        "content": f"Write a note on this topic: {topic}",
                    }
                ]
            )
            file_path = destPath / f'{topic}.md'
            with open(file_path, 'w', encoding='utf8') as f:
                f.write(message.content[0].text)
            stats['createdFiles'][topic] = file_path
    else:
        print('skipping AI generation')
        break
