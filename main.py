import obsidianCreator
import os
from anthropic import Anthropic
from collections import deque
from pathlib import Path
import json
from dotenv import load_dotenv
load_dotenv()
print(os.environ.get('ANTHROPIC_API_KEY'))

toWrite = deque()

stats = {
    'topics': set(),
    'newTopics': set(),
    'createdFiles': {}
}

#TODO WE SHOULD ADD A WHAT DO YOU WANT TO LEARN? (opening prompt to get the ball rolling)

client = Anthropic(
    api_key=os.environ.get('ANTHROPIC_API_KEY'),
)

while True:
    # path = input('where are the files that need to be process located? input -none- = terminate & save: ')
    path = r'C:\Users\Saad\Downloads\seed-vault-notes\01-CS-Programming'
    if path == '-none-':
        print('programmed stopped (user ended)')
        # TODO we need a lambda to convert the sets to lists
        # with open('savedStatus', 'w') as f:
            # f.write(json.dumps(stats))
        break

    given = Path(r"\Users\Saad\Downloads\seed-vault-notes\01-CS-Programming") # REAL VERSION: ASK FOR A FILEPATH
    # given = Path(path)
    if given.is_dir():
        files = [f.name for f in given.iterdir() if f.is_file()]
    for file in files:
        toWrite.append(file)

    stats["topics"] = list(toWrite)

    destPath = Path(r"C:\Users\Saad\Desktop\Brain\Brain") # REAL VERSION: ASK FOR A DEST PATH

    for file in stats["topics"]:
        if obsidianCreator.doesFileExist(destPath, file):
            continue
        document = obsidianCreator.parse(given / file)
        obsidianCreator.writeToFile(document)
        new_tags = {tag for tag in document.tags if not obsidianCreator.doesFileExist(destPath, tag)}
        stats["newTopics"].update(new_tags)

    print('wrote: ', stats["topics"])
    ans = input(f'recommend: {stats["newTopics"]} Write? (Y/N): ')
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

Output ONLY the note content (frontmatter + body). No preamble, no explanation, no markdown code fences around the whole thing."""

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
