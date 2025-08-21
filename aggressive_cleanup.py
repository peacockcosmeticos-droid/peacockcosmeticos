#!/usr/bin/env python3
"""
Aggressive WordPress/WooCommerce/Elementor Cleanup Script
- Complete removal of all remaining references
- Comprehensive transformation to native appearance
"""

import re
import os
from datetime import datetime

def aggressive_cleanup(content):
    """Aggressive cleanup of all remaining WordPress/WooCommerce/Elementor references"""
    print("🔄 Performing aggressive cleanup...")
    
    # Replace ALL elementor references in CSS classes and attributes
    content = re.sub(r'\belementor-([a-zA-Z0-9_-]+)', r'builder-\1', content)
    content = re.sub(r'\belementor\b', 'builder', content)
    
    # Replace ALL woocommerce references
    content = re.sub(r'\bwoocommerce\b', 'ecommerce', content)
    
    # Replace ALL wp-admin references
    content = re.sub(r'\/wp-admin\/[^"\']*', '/api/ajax.php', content)
    content = re.sub(r'wp-admin', 'admin', content)
    
    # Replace ALL wp-content references in prefetch and other configurations
    content = re.sub(r'\/wp-content\/', '/assets/', content)
    content = re.sub(r'wp-content', 'assets', content)
    
    # Replace theme references
    content = re.sub(r'page-template-elementor_header_footer', 'page-template-custom_header_footer', content)
    content = re.sub(r'elementor_header_footer', 'custom_header_footer', content)
    content = re.sub(r'elementor_library', 'builder_library', content)
    
    # Replace script IDs
    content = re.sub(r'id="elementor-([^"]*)"', r'id="builder-\1"', content)
    content = re.sub(r'id="elementskit-([^"]*)"', r'id="elements-\1"', content)
    
    # Replace file paths in href and src attributes
    content = re.sub(r'header-footer-elementor\.css', 'header-footer-builder.css', content)
    content = re.sub(r'elementor-icons\.min\.css', 'builder-icons.min.css', content)
    content = re.sub(r'elementor\.js', 'builder.js', content)
    
    # Replace data attributes
    content = re.sub(r'data-builder-post-type="elementor_library"', 'data-builder-post-type="builder_library"', content)
    
    # Replace JavaScript configuration objects
    content = re.sub(r'elementorFrontendConfig', 'builderFrontendConfig', content)
    content = re.sub(r'ElementorProFrontendConfig', 'ProBuilderFrontendConfig', content)
    
    # Clean up prefetch configuration completely
    prefetch_old = r'"prefetch":\[{"source":"document","where":{"and":\[{"href_matches":"\\\/\*"},{"not":{"href_matches":\["\\\/wp-\*\.php","\\\/wp-admin\\\\\*","\\\/wp-content\\\/uploads\\\\\*","\\\/wp-content\\\\\*","\\\/wp-content\\\/plugins\\\\\*","\\\/wp-content\\\/themes\\\/custom-theme-child\\\\\*","\\\/wp-content\\\/themes\\\/custom-theme\\\\\*","\\\\\*\\\\\?\(\.\+\)"\]}},{"not":{"selector_matches":"a\[rel~=\\"nofollow\\"\]"}},{"not":{"selector_matches":"\.no-prefetch, \.no-prefetch a"}}]},"eagerness":"conservative"}]'
    prefetch_new = r'"prefetch":[{"source":"document","where":{"and":[{"href_matches":"\\/*"},{"not":{"href_matches":["\\/*\\?(.+)"]}},{"not":{"selector_matches":"a[rel~=\\"nofollow\\"]"}},{"not":{"selector_matches":".no-prefetch, .no-prefetch a"}}]},"eagerness":"conservative"}]'
    content = re.sub(prefetch_old, prefetch_new, content)
    
    # Clean up any remaining WordPress-specific patterns
    content = re.sub(r'elementor/lazyload/observe', 'builder/lazyload/observe', content)
    
    return content

def main():
    """Main function to process the HTML file"""
    print("🚀 Starting aggressive WordPress/WooCommerce/Elementor cleanup...")
    
    # Read the current index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create backup
    backup_filename = f'index_aggressive_cleanup_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
    with open(backup_filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Backup created: {backup_filename}")
    
    # Apply aggressive cleanup
    content = aggressive_cleanup(content)
    
    # Write the updated content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Aggressive WordPress/WooCommerce/Elementor cleanup complete!")
    print("🎯 All references should now be transformed to native appearance!")

if __name__ == "__main__":
    main()
