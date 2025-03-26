import os
import re

# Set the directory for the Odin project (adjust this to your project folder path)
odin_project_dir = '/path/to/your/odin/project'

# Define the function to search Odin files for TODO comments
def search_odin_files_for_todos(directory):
    todos = []
    # Regular expression to search for TODO comments in Odin files
    todo_regex = re.compile(r'#\s*TODO[:\-]?\s*(.*)', re.IGNORECASE)

    # Recursively search through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.odin'):  # Only look at Odin files
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_num, line in enumerate(f, start=1):
                        match = todo_regex.search(line)
                        if match:
                            # Store the TODO in a list along with file and line number
                            todos.append({
                                'file': file_path,
                                'line': line_num,
                                'todo': match.group(1).strip()
                            })
    return todos

# Function to write the todos to an Obsidian markdown file
def write_to_obsidian(todos, obsidian_file_path):
    with open(obsidian_file_path, 'w', encoding='utf-8') as f:
        f.write('# Odin Project To-Do List\n\n')
        for todo in todos:
            f.write(f'- [ ] {todo["todo"]} (File: {todo["file"]}, Line: {todo["line"]})\n')
    print(f"To-Do list written to {obsidian_file_path}")

# Function to write the todos to a VSCode markdown task list file
def write_to_vscode(todos, vscode_file_path):
    with open(vscode_file_path, 'w', encoding='utf-8') as f:
        f.write('# Odin Project To-Do List\n\n')
        for todo in todos:
            f.write(f'- [ ] {todo["todo"]} (File: {todo["file"]}, Line: {todo["line"]})\n')
    print(f"To-Do list written to {vscode_file_path}")

def main():
    # Search the Odin project directory for TODO comments
    todos = search_odin_files_for_todos(odin_project_dir)

    if not todos:
        print("No TODOs found in the project.")
        return

    # Define the file paths for Obsidian and VSCode task list markdown files
    obsidian_file = os.path.join(odin_project_dir, 'odin_project_todo.md')
    vscode_file = os.path.join(odin_project_dir, 'odin_project_vscode_todo.md')

    # Write the todos to both Obsidian and VSCode markdown files
    write_to_obsidian(todos, obsidian_file)
    write_to_vscode(todos, vscode_file)

# Run the main function
if __name__ == "__main__":
    main()
