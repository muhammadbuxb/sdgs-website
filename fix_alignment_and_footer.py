import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix alignment of projects (the extra </div> issue)
    # The erroneous block is:
    # </div>
    #                 </div>
    #                 <div class="col-lg-4 col-md-6 col-sm-6">
    #                     <div class="single-cases mb-40">
    #                         <div class="cases-img">
    #                             <img src="assets/img/gallery/project_flood_medical.jpeg"
    
    # We can just replace the specific occurrence of double closing div before the new projects
    bad_structure = """                </div>
                </div>
                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-cases mb-40">
                        <div class="cases-img">
                            <img src="assets/img/gallery/project_flood_medical.jpeg\""""
                            
    good_structure = """                </div>
                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-cases mb-40">
                        <div class="cases-img">
                            <img src="assets/img/gallery/project_flood_medical.jpeg\""""
                            
    if bad_structure in content:
        content = content.replace(bad_structure, good_structure)
        
    # 2. Fix copyright
    # Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="fa fa-heart" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
    # We will regex replace it because the spacing might vary
    
    pattern = r'Copyright.*?All rights reserved \| This template is made with.*?Colorlib</a>'
    new_copyright = r'Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | SDGS Welfare Organization'
    
    content = re.sub(pattern, new_copyright, content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Alignment and copyright fixed.")
