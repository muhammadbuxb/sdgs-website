import re

# 1. Update image sizes in index.html and projects.html
for file in ['index.html', 'projects.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'<img src="(assets/img/gallery/project_[a-z]+\.jpeg)" alt="">',
        r'<img src="\1" alt="" style="width: 100%; height: 250px; object-fit: cover;">',
        content
    )
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update Pillars of Action in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We only want to target the Pillars of Action section. 
# It starts around "<!--? Services Area Start -->" and ends at "<!-- Services Area End -->"
services_match = re.search(r'<!--\? Services Area Start -->(.*?)<!-- Services Area End -->', content, flags=re.DOTALL)
if services_match:
    services_html = services_match.group(1)
    
    # Add flex to columns
    services_html = services_html.replace(
        '<div class="col-lg-4 col-md-6 col-sm-6">',
        '<div class="col-lg-4 col-md-6 col-sm-6 mb-50" style="display: flex;">'
    )
    # Update single-cat to take full height and center content
    services_html = services_html.replace(
        '<div class="single-cat text-center mb-50">',
        '<div class="single-cat text-center" style="width: 100%; display: flex; flex-direction: column; justify-content: center;">'
    )
    services_html = services_html.replace(
        '<div class="single-cat active text-center mb-50">',
        '<div class="single-cat active text-center" style="width: 100%; display: flex; flex-direction: column; justify-content: center;">'
    )
    
    content = content[:services_match.start(1)] + services_html + content[services_match.end(1):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Design fixes applied.")
