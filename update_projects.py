import os
import shutil
import re

# 1. Copy images
src_dir = 'our-work'
dest_dir = 'assets/img/gallery'

img_map = {
    'WhatsApp Image 2026-06-17 at 11.47.38.jpeg': 'project_flood_medical.jpeg',
    'WhatsApp Image 2026-06-17 at 11.47.03.jpeg': 'project_ramzan_rashan.jpeg',
    'WhatsApp Image 2026-06-17 at 11.46.45.jpeg': 'project_tree_plantation.jpeg'
}

for src_name, dest_name in img_map.items():
    src_path = os.path.join(src_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dest_path)

# 2. Add projects to index.html and projects.html
new_projects_html = """
                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-cases mb-40">
                        <div class="cases-img">
                            <img src="assets/img/gallery/project_flood_medical.jpeg" alt="" style="width: 100%; height: 250px; object-fit: cover;">
                        </div>
                        <div class="cases-caption" style="padding: 30px;">
                            <h3><a href="project_details.html">Medical Camp for Flood Effected areas of sindh 2022 ( District Naushero Feroze)</a></h3>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-cases mb-40">
                        <div class="cases-img">
                            <img src="assets/img/gallery/project_ramzan_rashan.jpeg" alt="" style="width: 100%; height: 250px; object-fit: cover;">
                        </div>
                        <div class="cases-caption" style="padding: 30px;">
                            <h3><a href="project_details.html">Rashan Distribution in the Month of Ramzan</a></h3>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-cases mb-40">
                        <div class="cases-img">
                            <img src="assets/img/gallery/project_tree_plantation.jpeg" alt="" style="width: 100%; height: 250px; object-fit: cover;">
                        </div>
                        <div class="cases-caption" style="padding: 30px;">
                            <h3><a href="project_details.html">Tree Plantations for Green Enviroment</a></h3>
                        </div>
                    </div>
                </div>
            </div>"""

for file in ['index.html', 'projects.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to insert the new projects right before the closing </div> of the <div class="row"> inside the Our Projects section
    # The last project before the closing div is "Students Supported in Local Education Initiatives".
    # Let's find that block and append to it.
    target_block = """<h3><a href="project_details.html">Students Supported in Local Education Initiatives</a></h3>
                        </div>
                    </div>
                </div>
            </div>"""
    
    # Replace the target block with target block + new projects
    if target_block in content:
        # Note: target_block includes the closing `</div>` for the row, so we append the new items 
        # and then close the row again, or just replace the `</div>` with our new projects which end with `</div>`.
        replacement = target_block.replace('</div>\n            </div>', '</div>\n                </div>' + new_projects_html)
        content = content.replace(target_block, replacement)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Clean up project_details.html
with open('project_details.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Hide likes and comments counts: <p class="like-info">...</p>
content = re.sub(r'<p class="like-info">.*?</p>', '<!-- hidden likes -->', content, flags=re.DOTALL)
content = re.sub(r'<p class="comment-count">.*?</p>', '<!-- hidden comment count -->', content, flags=re.DOTALL)
content = re.sub(r'<li><a href="#"><i class="fa fa-comments"></i>.*?</a></li>', '<!-- hidden comments -->', content, flags=re.DOTALL)

# Hide Comments Section: <div class="comments-area">...</div>
# Note: This regex might be tricky if there are nested divs. 
# Alternatively, we can just replace 'class="comments-area"' with 'class="comments-area d-none"'
content = content.replace('class="comments-area"', 'class="comments-area d-none"')

# Hide Leave a Reply form: <div class="comment-form">...</div>
content = content.replace('class="comment-form"', 'class="comment-form d-none"')

# Hide Right Sidebar and make main content full width
# The main content is in <div class="col-lg-8 posts-list">
content = content.replace('<div class="col-lg-8 posts-list">', '<div class="col-lg-12 posts-list">')
# The right sidebar is in <div class="col-lg-4"> inside the same row
content = content.replace('<div class="col-lg-4">', '<div class="col-lg-4 d-none">')

with open('project_details.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added new projects and cleaned up project details.")
