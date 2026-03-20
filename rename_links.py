import os

dir_path = r"c:\Github\4. demo\Edu_space"

for file in os.listdir(dir_path):
    if not file.endswith('.html'):
        continue
    filepath = os.path.join(dir_path, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Thay the the long link
    content = content.replace("eduplay_landing_page_illustrated_style.html", "index.html")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
print("Updated links")
