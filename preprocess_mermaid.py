import re
import sys
from pathlib import Path

def convert_mermaid_blocks(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to find ```mermaid blocks and replace them with divs
    converted_content = re.sub(
        r'```mermaid(.*?)```',
        r'<div class="mermaid">\1</div>',
        content,
        flags=re.DOTALL
    )

    # Write the converted content back to the file or to a new file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(converted_content)

if __name__ == "__main__":
    # Specify the directory or file to process
    directory = Path(sys.argv[1])
    for markdown_file in directory.rglob("*.md"):
        convert_mermaid_blocks(markdown_file)
