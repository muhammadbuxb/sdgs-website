import shutil
import re

# 1. Copy blog_details.html to project_details.html
shutil.copyfile('blog_details.html', 'project_details.html')

# 2. Update project_details.html
with open('project_details.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change banner title
content = content.replace('<h2>Blog Details</h2>', '<h2>Project Details</h2>')

# Change featured image
content = content.replace(
    '<img class="img-fluid" src="assets/img/blog/single_blog_1.png" alt="">',
    '<img class="img-fluid" src="assets/img/gallery/project_medical.jpeg" alt="" style="width: 100%; height: auto; object-fit: cover;">'
)

# Change title
content = content.replace(
    'Second divided from form fish beast made every of seas\n                           all gathered us saying he our',
    'Project Details: Our Initiatives in Sindh'
)

# Change Category
content = content.replace(
    '<i class="fa fa-user"></i> Travel, Lifestyle',
    '<i class="fa fa-tag"></i> Social Welfare'
)

# Replace "MCSE boot camps..." text with generic text
generic_text = "We are passionately committed to reaching every corner of Sindh with essential services. Through the support of our volunteers and generous donors, this project has significantly impacted local communities by directly addressing immediate needs while laying the foundation for long-term sustainability. We invite you to join our movement and help us expand this critical work."
content = re.sub(r'MCSE boot camps have its supporters.*?fraction of the camp price\. However, who has the willpower', generic_text, content, flags=re.DOTALL)
content = re.sub(r'MCSE boot camps have its supporters.*?self-imposed MCSE training\. who has the willpower to actually', generic_text, content, flags=re.DOTALL)
content = re.sub(r'MCSE boot camps have its supporters.*?self-imposed MCSE training\.', generic_text, content, flags=re.DOTALL)

with open('project_details.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 3. Update index.html and projects.html to link to project_details.html
for file in ['index.html', 'projects.html']:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Change href="projects.html" inside Our Projects section to href="project_details.html"
    # The links look like: <h3><a href="projects.html">Patients Treated in Free Medical Camps</a></h3>
    html = html.replace('href="projects.html">Patients Treated', 'href="project_details.html">Patients Treated')
    html = html.replace('href="projects.html">Families Reached', 'href="project_details.html">Families Reached')
    html = html.replace('href="projects.html">Students Supported', 'href="project_details.html">Students Supported')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Project Details created and links updated.")
