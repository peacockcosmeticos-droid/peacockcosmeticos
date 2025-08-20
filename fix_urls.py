#!/usr/bin/env python3
"""
Script to replace all remaining absolute URLs with relative paths in index.html
"""

import re

def fix_urls():
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace all remaining https://peacockcosmeticos.com.br/ URLs with relative paths
    # This pattern matches the domain in various contexts
    patterns = [
        # Standard href and src attributes
        (r'https://peacockcosmeticos\.com\.br/wp-content/', './wp-content/'),
        (r'https://peacockcosmeticos\.com\.br/wp-includes/', './wp-includes/'),
        
        # URLs in href attributes for internal links
        (r'href="https://peacockcosmeticos\.com\.br/"', 'href="./"'),
        (r'href="https://peacockcosmeticos\.com\.br/([^"]*)"', r'href="./\1"'),
        
        # URLs in src attributes
        (r'src="https://peacockcosmeticos\.com\.br/([^"]*)"', r'src="./\1"'),
        
        # URLs in srcset attributes
        (r'https://peacockcosmeticos\.com\.br/wp-content/', './wp-content/'),
        
        # URLs in JavaScript/JSON content
        (r'"https:\\/\\/peacockcosmeticos\\.com\\.br\\/"', '"./"'),
        (r'"https:\\/\\/peacockcosmeticos\\.com\\.br\\/([^"]*)"', r'"./\1"'),
        
        # URLs in content attributes and other places
        (r'content="https://peacockcosmeticos\.com\.br/([^"]*)"', r'content="./\1"'),
        (r'content="https://peacockcosmeticos\.com\.br/"', 'content="./"'),
        
        # URLs in schema.org JSON-LD
        (r'"https://peacockcosmeticos\.com\.br/"', '"./"'),
        (r'"https://peacockcosmeticos\.com\.br/([^"]*)"', r'"./\1"'),
        
        # Purchase/cart URLs - disable these for offline use
        (r'href="https://peacockcosmeticos\.com\.br/\?comprar_produto=[^"]*"', 'href="#" onclick="alert(\'Funcionalidade de compra desabilitada para visualização offline\'); return false;"'),
        
        # Privacy policy and other internal page links
        (r'href="https://peacockcosmeticos\.com\.br/privacy-policy/"', 'href="#"'),
        (r'href="https://peacockcosmeticos\.com\.br/carrinho-2/"', 'href="#"'),
        (r'href="https://peacockcosmeticos\.com\.br/checkout/"', 'href="#"'),
    ]
    
    # Apply all replacements
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    # Write the modified content back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("URL replacement completed!")

if __name__ == "__main__":
    fix_urls()
