#!/usr/bin/env python3
"""
Enhanced WordPress Cleanup Script
- Remove remaining WordPress/WooCommerce identifiers
- Clean up CSS custom properties
- Update JavaScript variables
- Remove WordPress-specific classes and IDs
"""

import re
import os
from datetime import datetime

def enhanced_wordpress_cleanup(content):
    """Enhanced cleanup of WordPress identifiers"""

    # Remove WordPress-specific comments
    content = re.sub(r'// Disable WordPress emoji support for offline use', '// Disable emoji support for offline use', content)

    # Clean up CSS custom properties (remove wp-- prefixes)
    wp_css_replacements = [
        (r'--wp--preset--', '--preset--'),
        (r'--wp--style--', '--style--'),
        (r'\.wp-site-blocks', '.site-blocks'),
        (r'\.wp-element-button', '.element-button'),
        (r'\.wp-block-button__link', '.block-button__link'),
        (r'\.wp-block-pullquote', '.block-pullquote'),
    ]

    for pattern, replacement in wp_css_replacements:
        content = re.sub(pattern, replacement, content)

    # Update remaining CSS classes
    css_class_replacements = {
        'wp-image-': 'image-',
        'wp-post': 'post',
        'wp-page': 'page',
        'data-wp-strategy': 'data-strategy',
        'wp-util': 'util',
        'wp-dom-ready': 'dom-ready',
        'wp-hooks': 'hooks',
        'wp-i18n': 'i18n',
    }

    for wp_class, new_class in css_class_replacements.items():
        content = content.replace(wp_class, new_class)

    # Update JavaScript variables and functions
    js_replacements = [
        (r'wp\.i18n\.setLocaleData', 'app.i18n.setLocaleData'),
        (r'"wpPreview"', '"preview"'),
        (r'"ajaxurl":"\/wp-admin\/admin-ajax\.php"', '"ajaxurl":"/admin/ajax.php"'),
        (r'"uploadUrl":"\.\/assets\/uploads"', '"uploadUrl":"./assets/media"'),
        (r'"rest":"\.\/api\/"', '"rest":"./api/"'),
        (r'https:\/\/peacockcosmeticos\.com\.br\/wp-admin\/admin-ajax\.php', 'https://peacockcosmeticos.com.br/admin/ajax.php'),
    ]

    for pattern, replacement in js_replacements:
        content = re.sub(pattern, replacement, content)

    # Clean up WooCommerce references
    woocommerce_replacements = [
        (r'woocommerce-js', 'ecommerce-js'),
        (r'\.woocommerce', '.ecommerce'),
        (r'wc-blocks', 'ecommerce-blocks'),
        (r'wc-add-to-cart', 'add-to-cart'),
        (r'wc-order-attribution', 'order-attribution'),
        (r'wc-ajax', 'ajax'),
    ]

    for pattern, replacement in woocommerce_replacements:
        content = re.sub(pattern, replacement, content)

    # Remove WordPress-specific speculation rules
    content = re.sub(
        r'"href_matches":\["\/wp-\*\.php","\/wp-admin\/\*","\/wp-content\/uploads\/\*","\/wp-content\/\*","\/wp-content\/plugins\/\*","\/wp-content\/themes\/hello-elementor-child\/\*","\/wp-content\/themes\/hello-elementor\/\*","\/*\\?\(.+\)"\]',
        '"href_matches":["/*.php","/admin/*","/assets/media/*","/assets/*","/assets/modules/*","/assets/templates/hello-elementor-child/*","/assets/templates/hello-elementor/*","/*\\\\?(.+)"]',
        content
    )

    # Clean up remaining WordPress references in data attributes
    content = re.sub(r'data-elementor-type="wp-post"', 'data-elementor-type="post"', content)
    content = re.sub(r'data-elementor-type="wp-page"', 'data-elementor-type="page"', content)
    content = re.sub(r'data-elementor-post-type="elementor-hf"', 'data-elementor-post-type="header-footer"', content)

    return content

def clean_remaining_references(content):
    """Clean up any remaining WordPress references"""

    # Remove WordPress version references
    content = re.sub(r'\?ver=6\.8\.2', '?ver=1.0.0', content)
    content = re.sub(r'\?ver=10\.1\.0', '?ver=1.0.0', content)
    content = re.sub(r'\?ver=3\.31\.2', '?ver=1.0.0', content)

    # Clean up file paths that might still reference WordPress structure
    content = re.sub(r'wp-content\\uploads', 'assets/media', content)
    content = re.sub(r'wp-content\\plugins', 'assets/modules', content)
    content = re.sub(r'wp-content\\themes', 'assets/templates', content)

    # Remove WordPress-specific noscript styles
    content = re.sub(r'<noscript><style>\.woocommerce-product-gallery\{ opacity: 1 !important; \}</style></noscript>', '', content)

    return content

def main():
    """Main function to process the HTML file"""
    print("🔄 Starting enhanced WordPress cleanup...")

    # Read the current index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Create backup
    backup_filename = f'index_enhanced_cleanup_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
    with open(backup_filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Backup created: {backup_filename}")

    # Apply enhanced cleanup
    print("🔄 Applying enhanced WordPress cleanup...")
    content = enhanced_wordpress_cleanup(content)

    print("🔄 Cleaning remaining references...")
    content = clean_remaining_references(content)

    # Write the updated content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Enhanced WordPress cleanup complete!")
    print("📊 Additional changes applied:")
    print("   - Cleaned CSS custom properties")
    print("   - Updated JavaScript variables")
    print("   - Removed WooCommerce references")
    print("   - Cleaned data attributes")
    print("   - Updated file paths")

if __name__ == "__main__":
    main()