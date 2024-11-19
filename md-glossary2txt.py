import os
import markdown
from bs4 import BeautifulSoup

input_dir = "./docs/"
for file_name in os.listdir(input_dir):
        if (file_name == 'figures' or file_name == 'index.md'):
            continue
        print('-----' + file_name)
        with open(input_dir + file_name, 'r', encoding='utf-8') as file:
                markdown_content = file.read()
                content = markdown.markdown(markdown_content)
                soup = BeautifulSoup(content, 'html.parser')
                text_content = soup.get_text()

                lines = text_content.split('\n')
                lines = lines[:-1]
                new_text = '\n'.join(lines)
                print(text_content)
