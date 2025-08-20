#!/usr/bin/env python3
"""
Script to fix font URLs in Google Fonts CSS files
"""

import os
import re

def fix_font_urls():
    font_css_dir = 'wp-content/uploads/elementor/google-fonts/css'
    
    if not os.path.exists(font_css_dir):
        print(f"Directory {font_css_dir} not found")
        return
    
    # Get all CSS files in the directory
    css_files = [f for f in os.listdir(font_css_dir) if f.endswith('.css')]
    
    for css_file in css_files:
        file_path = os.path.join(font_css_dir, css_file)
        
        # Read the CSS file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the incorrect domain with relative paths
        # Pattern: url(https://peecock.com.br/wp-content/uploads/elementor/google-fonts/fonts/...)
        content = re.sub(
            r'url\(https://peecock\.com\.br/wp-content/uploads/elementor/google-fonts/fonts/',
            'url(../../fonts/',
            content
        )
        
        # Also handle peacockcosmeticos.com.br if present
        content = re.sub(
            r'url\(https://peacockcosmeticos\.com\.br/wp-content/uploads/elementor/google-fonts/fonts/',
            'url(../../fonts/',
            content
        )
        
        # Write the modified content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Fixed font URLs in {css_file}")

if __name__ == "__main__":
    fix_font_urls()
