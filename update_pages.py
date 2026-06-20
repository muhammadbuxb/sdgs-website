import re

# Update projects.html
with open('projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_projects = """    <!-- Our Projects Start -->
    <div class="our-cases-area section-padding30">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-xl-6 col-lg-7 col-md-10 col-sm-10">
                    <!-- Section Tittle -->
                    <div class="section-tittle text-center mb-80">
                        <span>Our Projects</span>
                        <h2>Explore our latest projects</h2>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-cases mb-40">
                        <div class="cases-img">
                            <img src="assets/img/gallery/project_medical.jpeg" alt="">
                        </div>
                        <div class="cases-caption" style="padding: 30px;">
                            <h3><a href="projects.html">Patients Treated in Free Medical Camps</a></h3>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-cases mb-40">
                        <div class="cases-img">
                            <img src="assets/img/gallery/project_relief.jpeg" alt="">
                        </div>
                        <div class="cases-caption" style="padding: 30px;">
                            <h3><a href="projects.html">Families Reached via Emergency Relief & Rations</a></h3>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6 col-sm-6">
                    <div class="single-cases mb-40">
                        <div class="cases-img">
                            <img src="assets/img/gallery/project_education.jpeg" alt="">
                        </div>
                        <div class="cases-caption" style="padding: 30px;">
                            <h3><a href="projects.html">Students Supported in Local Education Initiatives</a></h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Our Projects End -->"""

content = re.sub(r'<!-- Our Cases Start -->.*?<!-- Our Cases End -->', new_projects, content, flags=re.DOTALL)
content = content.replace('<h2>latest causes </h2>', '<h2>Projects</h2>')

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update our-workings.html
with open('our-workings.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_workings = """    <!-- Our Workings Start -->
    <section class="featured-job-area section-padding30 section-bg2" data-background="assets/img/gallery/section_bg03.png">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-xl-7 col-lg-9 col-md-10 col-sm-12">
                    <!-- Section Tittle -->
                    <div class="section-tittle text-center mb-80">
                        <span>What we are doing</span>
                        <h2>Our Workings</h2>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-lg-9 col-md-12">
                    <!-- single-job-content -->
                    <div class="single-job-items mb-30">
                        <div class="job-items align-items-center">
                            <div class="company-img">
                                <a href="our-workings.html"><img src="assets/img/gallery/working_education.jpeg" alt="" style="width: 150px; border-radius: 5px;"></a>
                            </div>
                            <div class="job-tittle">
                                <a href="our-workings.html"><h4>Education for the Future</h4></a>
                                <ul>
                                    <li style="white-space: normal;"><strong>Nurturing Minds and the Environment</strong><br>We firmly believe that education is the absolute foundation of any sustainable, thriving community. We are committed to breaking the cycle of poverty by empowering the next generation. Makeshift & Local Schools: We actively fund and support local learning centers, providing vital resources, books, and safe outdoor school settings for children who lack access to formal infrastructure. Environmental Stewardship: Education goes beyond the classroom. We foster a strong spirit of environmental responsibility in our youth by organizing interactive tree-planting campaigns and climate awareness drives. The Goal: To cultivate educated, environmentally conscious citizens who will lead Sindh into a sustainable future.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-9 col-md-12">
                    <!-- single-job-content -->
                    <div class="single-job-items mb-30">
                        <div class="job-items align-items-center">
                            <div class="company-img">
                                <a href="our-workings.html"><img src="assets/img/gallery/working_relief.jpeg" alt="" style="width: 150px; border-radius: 5px;"></a>
                            </div>
                            <div class="job-tittle">
                                <a href="our-workings.html"><h4>Disaster Response & Social Welfare</h4></a>
                                <ul>
                                    <li style="white-space: normal;"><strong>Standing Resilient Against Climate Adversity</strong><br>Sindh is increasingly vulnerable to extreme weather and climate adversity. When disaster strikes, the SDGS Welfare Organization is immediately on the ground, serving as a vital lifeline for affected families. Crisis Intervention: We specialize in rapid response, from distributing emergency food rations and survival supplies to families facing sudden displacement or extreme poverty. Heat Wave Relief: During life-threatening summer temperatures, we proactively set up heat wave relief camps, providing critical hydration, shade, and medical support to prevent heatstroke and save lives. The Goal: To ensure that no individual is left behind during a crisis, providing the immediate relief necessary to help communities get back on their feet.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-9 col-md-12">
                    <!-- single-job-content -->
                    <div class="single-job-items mb-30">
                        <div class="job-items align-items-center">
                            <div class="company-img">
                                <a href="our-workings.html"><img src="assets/img/gallery/working_medical.jpeg" alt="" style="width: 150px; border-radius: 5px;"></a>
                            </div>
                            <div class="job-tittle">
                                <a href="our-workings.html"><h4>Emergency Medical Relief</h4></a>
                                <ul>
                                    <li style="white-space: normal;"><strong>Bridging the Gap in Healthcare Access</strong><br>In many remote and disaster-affected areas of Sindh, basic medical care is completely out of reach. We organize heavily equipped, free medical camps to bring healthcare directly to the vulnerable. Our Approach: Using our red mobile medical vans, our dedicated teams of volunteer doctors and nurses travel to underserved communities. Services Provided: We offer comprehensive health check-ups, essential diagnostics, and free medicine distribution to families who otherwise could not afford treatment. The Goal: To prevent minor illnesses from becoming life-threatening and to ensure maternal and pediatric health remains a priority, no matter the location.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Our Workings End -->"""

content = re.sub(r'<!-- Featured_job_start -->.*?<!-- Featured_job_end -->', new_workings, content, flags=re.DOTALL)
content = content.replace('<h2>social events </h2>', '<h2>Our Workings</h2>')

with open('our-workings.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated projects.html and our-workings.html")
