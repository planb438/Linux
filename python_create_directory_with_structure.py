import os

def create_directory_structure(root_dir):
    # Create root directory
    os.makedirs(root_dir, exist_ok=True)

    # Create README.md
    with open(os.path.join(root_dir, 'README.md'), 'w') as readme_file:
        readme_file.write("# Overview of the repository and instructions\n")

    # Create website directory and its contents
    website_dir = os.path.join(root_dir, 'website')
    os.makedirs(website_dir)
    website_files = ['index.html', 'about.html', 'resume.html', 'projects.html',
                     'certifications.html', 'skills.html', 'contact.html']
    for file in website_files:
        with open(os.path.join(website_dir, file), 'w') as html_file:
            html_file.write(f"<html><body><h1>{os.path.splitext(file)[0]}</h1></body></html>")

    # Create css, js, and img directories inside website
    os.makedirs(os.path.join(website_dir, 'css'))
    os.makedirs(os.path.join(website_dir, 'js'))
    os.makedirs(os.path.join(website_dir, 'img'))

    # Create projects directory
    os.makedirs(os.path.join(root_dir, 'projects'))

    # Create certifications directory
    os.makedirs(os.path.join(root_dir, 'certifications'))

    # Create blog directory
    os.makedirs(os.path.join(root_dir, 'blog'))
    blog_files = ['post1.md', 'post2.md']
    for file in blog_files:
        with open(os.path.join(root_dir, 'blog', file), 'w') as blog_file:
            blog_file.write(f"# Blog post title\n\nContent of {file}")

    # Create scripts directory and its subdirectories
    scripts_dir = os.path.join(root_dir, 'scripts')
    os.makedirs(scripts_dir)
    script_categories = ['aws_scripts', 'linux_scripts', 'nmap_scripts', 'other_scripts']
    for category in script_categories:
        os.makedirs(os.path.join(scripts_dir, category))

    # Create README.md inside scripts directory
    with open(os.path.join(scripts_dir, 'README.md'), 'w') as scripts_readme:
        scripts_readme.write("# Overview of the scripts and instructions\n")

if __name__ == "__main__":
    root_directory = '/path/to/your/directory'
    create_directory_structure(root_directory)
