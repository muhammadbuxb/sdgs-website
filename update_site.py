import os
import glob
import re

html_files = glob.glob('*.html')

# Menu updates
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update menu links
    content = content.replace('href="program.html">latest causes</a>', 'href="projects.html">Projects</a>')
    content = content.replace('href="events.html">social events </a>', 'href="our-workings.html">Our Workings</a>')
    content = content.replace('href="events.html">social events</a>', 'href="our-workings.html">Our Workings</a>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Menu links updated in all html files")
