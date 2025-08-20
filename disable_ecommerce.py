#!/usr/bin/env python3
"""
Script to disable e-commerce functionality while preserving visual appearance
"""

import re

def disable_ecommerce():
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Disable purchase buttons by replacing href with onclick alert
    purchase_patterns = [
        # Replace purchase links with disabled functionality
        (r'href="\./\?comprar_produto=[^"]*"', 'href="#" onclick="alert(\'Funcionalidade de compra desabilitada para visualização offline\'); return false;"'),
        
        # Disable cart redirect
        (r'"cart_redirect_after_add":"no"', '"cart_redirect_after_add":"no"'),
        
        # Disable WooCommerce AJAX
        (r'"wc_ajax_url":"\\/\\?wc-ajax=%%endpoint%%"', '"wc_ajax_url":"#"'),
    ]
    
    # Apply all replacements
    for pattern, replacement in purchase_patterns:
        content = re.sub(pattern, replacement, content)
    
    # Write the modified content back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("E-commerce functionality disabled!")

if __name__ == "__main__":
    disable_ecommerce()
