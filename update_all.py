import os
import re

dir_path = r'c:\Github\4. demo\Edu_space'

for file in os.listdir(dir_path):
    if not file.endswith('.html'):
        continue
    filepath = os.path.join(dir_path, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace Logo divs
    content = re.sub(
        r'<div class="([^"]*?text-xl font-bold[^"]*?)">EduSlide Pro</div>',
        r'<a href="eduplay_landing_page_illustrated_style.html" class="\1 hover:opacity-80 transition-opacity">EduSlide Pro</a>',
        content
    )
    # Replace Logo spans
    content = re.sub(
        r'<span class="([^"]*?text-xl font-bold[^"]*?)">EduSlide Pro</span>',
        r'<a href="eduplay_landing_page_illustrated_style.html" class="\1 hover:opacity-80 transition-opacity">EduSlide Pro</a>',
        content
    )

    if file == 'eduplay_landing_page_illustrated_style.html':
        content = content.replace('<html lang="vi">', '<html lang="vi" class="scroll-smooth">')
        
        if 'aos.css' not in content:
            content = content.replace(
                '<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>',
                '<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>\n<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet"/>',
                1
            )
            
        if 'aos.js' not in content:
            content = content.replace(
                '</body></html>',
                '<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n<script>\n  AOS.init({\n    duration: 800,\n    easing: "ease-out-cubic",\n    once: true,\n    offset: 50\n  });\n</script>\n</body></html>'
            )
            
        # Add simple AOS to major sections
        content = content.replace('<section class="py-24', '<section data-aos="fade-up" class="py-24')
        content = content.replace('<section class="py-16', '<section data-aos="fade-up" class="py-16')
        content = content.replace('<div class="md:w-[55%] lg:w-1/2', '<div data-aos="fade-right" class="md:w-[55%] lg:w-1/2')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Update successfully finished")
