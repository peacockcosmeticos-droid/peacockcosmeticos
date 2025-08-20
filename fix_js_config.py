#!/usr/bin/env python3
"""
Script to fix JavaScript configuration URLs for offline use
"""

import re

def fix_js_config():
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix AJAX URLs in JavaScript configuration
    patterns = [
        # Fix admin-ajax.php URLs
        (r'"ajaxurl":"https:\\/\\/peacockcosmeticos\\.com\\.br\\/wp-admin\\/admin-ajax\\.php"', '"ajaxurl":"#"'),
        (r'"ajax_url":"\\/wp-admin\\/admin-ajax\\.php"', '"ajax_url":"#"'),
        
        # Fix asset URLs in Elementor config
        (r'"assets":"https:\\/\\/peacockcosmeticos\\.com\\.br\\/wp-content\\/plugins\\/elementor\\/assets\\/"', '"assets":"./wp-content/plugins/elementor/assets/"'),
        (r'"assets":"https:\\/\\/peacockcosmeticos\\.com\\.br\\/wp-content\\/plugins\\/pro-elements\\/assets\\/"', '"assets":"./wp-content/plugins/pro-elements/assets/"'),
        
        # Fix upload URLs
        (r'"uploadUrl":"https:\\/\\/peacockcosmeticos\\.com\\.br\\/wp-content\\/uploads"', '"uploadUrl":"./wp-content/uploads"'),
        
        # Fix REST API URLs
        (r'"rest":"https:\\/\\/peacockcosmeticos\\.com\\.br\\/wp-json\\/"', '"rest":"./wp-json/"'),
        
        # Fix WooCommerce cart URLs
        (r'"cart_page_url":"https:\\/\\/peacockcosmeticos\\.com\\.br\\/carrinho-2\\/"', '"cart_page_url":"#"'),
        (r'"checkout_page_url":"https:\\/\\/peacockcosmeticos\\.com\\.br\\/checkout\\/"', '"checkout_page_url":"#"'),
        
        # Fix Lottie animation URLs
        (r'"defaultAnimationUrl":"https:\\/\\/peacockcosmeticos\\.com\\.br\\/wp-content\\/plugins\\/pro-elements\\/modules\\/lottie\\/assets\\/animations\\/default\\.json"', '"defaultAnimationUrl":"./wp-content/plugins/pro-elements/modules/lottie/assets/animations/default.json"'),
        
        # Disable WooCommerce AJAX endpoints
        (r'"wc_ajax_url":"\\/\\?wc-ajax=%%endpoint%%"', '"wc_ajax_url":"#"'),
    ]
    
    # Apply all replacements
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    # Write the modified content back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("JavaScript configuration URLs fixed for offline use!")

if __name__ == "__main__":
    fix_js_config()
