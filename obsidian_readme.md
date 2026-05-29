# ### 🐍 Script Requirements: What Your Python Code Needs

# Your script, let's call it `obsidian_creator.py`, must handle three core tasks:

# ### 1. The Directory Creator
# *   **Function:** Must take a path (a folder name) and create it, ensuring that if the folder already exists, the script doesn't throw an error.
# *   **Python Tool:** `os.makedirs(path, exist_ok=True)` is ideal.

# ### 2. The Note File Creator
# *   **Function:** Must take a full path and a string of content, and write that content to a new `.md` file.
# *   **Python Tool:** Simple file writing (`with open(file_path, 'w', encoding='utf-8') as f: f.write(content)`).

# ### 3. The Content Parser (The Magic Part!)
# *   **Function:** This is the key. When I provide you with a complex piece of content (e.g., a research note), I need to structure it so your script knows exactly *which* file it belongs to, *what* the content is, and *what* the metadata is.

# ---

# ## 📑 My Input Format: How I Will "Talk" to Your Script

# To make this work, I will not just give you raw text. I will give you a structured Python data object (like a list of dictionaries).

# **The goal is for your script to iterate through this list and execute the commands.**

# Here are the three types of data I will give you, corresponding to the actions your script needs to perform:

# ### 🟢 Type A: Folder Structure (The Architecture)

# *   **What I provide:** A list of folders to create.
# *   **Your script uses:** `os.makedirs`
# *   **Example Input from Me:**
#     ```python
#     folder_structure = [
#         "00_Inbox",
#         "10_Topics/Cognitive_Bias",
#         "20_Sources/Book_History_of_Time",
#         "30_Templates/Zettelkasten_Note"
#     ]
#     ```

# ### 🟡 Type B: Empty Note Templates (The Plumbing)

# *   **What I provide:** A template name, a path, and the boilerplate Markdown content (including required YAML frontmatter).
# *   **Your script uses:** `os.makedirs` (if the parent folder doesn't exist), then `open()` and `write()`.
# *   **Example Input from Me:**
#     ```python
#     templates = [
#         {"path": "30_Templates/Zettelkasten_Note.md", "content": """---
#             type: zettel
#             date: {{TODAY}}
#             tags: [note, raw]
#             ---
#             # {{TITLE}}
#             (This is where the core idea lives.)
#             \n\n*Source Link:* [[Source Link]]
#         ""},
#     ]
#     ```

# ### 🔴 Type C: Populated Notes (The Content Seeding)

# *   **What I provide:** The full, rich, interconnected note content, including all the Obsidian syntax.
# *   **Your script uses:** `open()` and `write()`.
# *   **Example Input from Me:**
#     ```python
#     notes_to_seed = [
#         {"path": "10_Topics/Cognitive_Bias/Confirmation_Bias.md", "content": """---
#             type: bias
#             date: 2024-06-20
#             tags: [psychology, bias]
#             ---
#             # Confirmation Bias
#             *Definition:* The tendency to search for, interpret, favor, and recall information in a way that confirms one's pre-existing beliefs.
#             \n\n*Related Concepts:* [[Cognitive Dissonance]], [[Belief Systems]].
#         """},
#         # ... more notes
#     ]
#     ```

# ---

# ## ✅ Summary: Your Workflow

# 1.  **You build the script:** Write the Python code to read a list of dictionaries (like the examples above) and perform the file system actions (`mkdir`, `write`).
# 2.  **You feed me the scope:** Tell me what kind of vault we are building (e.g., "Academic Vault focused on Renaissance History").
# 3.  **I generate the data:** I will respond to you with the structured Python data list (Type A, B, and C) that your script can immediately process.

# **Ready to start? Tell me the scope, and I'll generate the first block of code/data for you!**