#!/usr/bin/env python3
"""
Direct String Replacement Cleanup Script
- Direct string replacements for remaining references
- Simple and effective approach
"""

import os
from datetime import datetime

def direct_cleanup(content):
    """Direct string replacements for remaining references"""
    print("🔄 Performing direct string replacements...")
    
    # Direct replacements for file paths
    content = content.replace('header-footer-elementor.css', 'header-footer-builder.css')
    content = content.replace('elementor-icons.min.css', 'builder-icons.min.css')
    content = content.replace('elementor.js', 'builder.js')
    
    # Direct replacements for CSS classes
    content = content.replace('elementor-col-', 'builder-col-')
    content = content.replace('elementor-top-section', 'builder-top-section')
    content = content.replace('elementor-inner-section', 'builder-inner-section')
    content = content.replace('elementor-top-column', 'builder-top-column')
    content = content.replace('elementor-inner-column', 'builder-inner-column')
    content = content.replace('elementor-size-default', 'builder-size-default')
    content = content.replace('elementor-align-', 'builder-align-')
    content = content.replace('elementor-hidden-', 'builder-hidden-')
    content = content.replace('elementor-invisible', 'builder-invisible')
    content = content.replace('elementor-animation', 'builder-animation')
    content = content.replace('elementor-button', 'builder-button')
    content = content.replace('elementor-heading-title', 'builder-heading-title')
    content = content.replace('elementor-icon-list', 'builder-icon-list')
    content = content.replace('elementor-inline-items', 'builder-inline-items')
    content = content.replace('elementor-inline-item', 'builder-inline-item')
    content = content.replace('elementor-repeater-item', 'builder-repeater-item')
    content = content.replace('elementor-testimonial', 'builder-testimonial')
    content = content.replace('elementor-swiper-button', 'builder-swiper-button')
    content = content.replace('elementor-arrows-position', 'builder-arrows-position')
    content = content.replace('elementor-pagination-position', 'builder-pagination-position')
    content = content.replace('elementor-view-stacked', 'builder-view-stacked')
    content = content.replace('elementor-shape-circle', 'builder-shape-circle')
    content = content.replace('elementor-position-top', 'builder-position-top')
    content = content.replace('elementor-mobile-position-top', 'builder-mobile-position-top')
    content = content.replace('elementor-mobile-align-center', 'builder-mobile-align-center')
    content = content.replace('elementor-absolute', 'builder-absolute')
    content = content.replace('elementor-wrapper', 'builder-wrapper')
    content = content.replace('elementor-open-inline', 'builder-open-inline')
    
    # Direct replacements for data attributes
    content = content.replace('elementor_header_footer', 'custom_header_footer')
    content = content.replace('elementor_library', 'builder_library')
    
    # Direct replacements for script IDs
    content = content.replace('id="elementor-', 'id="builder-')
    content = content.replace('id="elementskit-', 'id="elements-')
    
    # Direct replacements for JavaScript
    content = content.replace('elementorFrontendConfig', 'builderFrontendConfig')
    content = content.replace('ElementorProFrontendConfig', 'ProBuilderFrontendConfig')
    content = content.replace('elementor/lazyload/observe', 'builder/lazyload/observe')
    
    # Direct replacements for WordPress admin
    content = content.replace('/wp-admin/admin-ajax.php', '/api/ajax.php')
    
    # Direct replacements for prefetch patterns
    content = content.replace('/wp-*.php', '/*.php')
    content = content.replace('/wp-admin/*', '/admin/*')
    content = content.replace('/wp-content/uploads/*', '/assets/media/*')
    content = content.replace('/wp-content/*', '/assets/*')
    content = content.replace('/wp-content/plugins/*', '/assets/modules/*')
    content = content.replace('/wp-content/themes/custom-theme-child/*', '/assets/templates/custom-theme-child/*')
    content = content.replace('/wp-content/themes/custom-theme/*', '/assets/templates/custom-theme/*')
    
    return content

def main():
    """Main function to process the HTML file"""
    print("🚀 Starting direct string replacement cleanup...")
    
    # Read the current index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create backup
    backup_filename = f'index_direct_cleanup_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
    with open(backup_filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Backup created: {backup_filename}")
    
    # Apply direct cleanup
    content = direct_cleanup(content)
    
    # Write the updated content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Direct string replacement cleanup complete!")
    print("🎯 All references should now be transformed!")

if __name__ == "__main__":
    main()
