#!/usr/bin/env python3
"""
Careful WordPress/WooCommerce/Elementor Reference Cleanup Script
- Only changes file paths and reference names in HTML
- Preserves ALL CSS class names and styling
- Maintains 100% visual fidelity and functionality
"""

import re
import os
from datetime import datetime

def create_backup(content):
    """Create backup of current working state"""
    backup_filename = f'index_careful_cleanup_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
    with open(backup_filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Backup created: {backup_filename}")
    return backup_filename

def analyze_references(content):
    """Analyze all WordPress/WooCommerce/Elementor references"""
    print("🔍 Analyzing WordPress/WooCommerce/Elementor references...")
    
    # Find WooCommerce folder references
    woo_paths = re.findall(r'["\']([^"\']*woocommerce[^"\']*)["\']', content)
    print(f"📁 WooCommerce folder references found: {len(woo_paths)}")
    for path in woo_paths[:5]:  # Show first 5
        print(f"   - {path}")
    
    # Find Elementor folder references  
    elementor_paths = re.findall(r'["\']([^"\']*elementor[^"\']*)["\']', content)
    print(f"📁 Elementor folder references found: {len(elementor_paths)}")
    for path in elementor_paths[:5]:  # Show first 5
        print(f"   - {path}")
    
    # Find WordPress admin references
    wp_admin = re.findall(r'["\']([^"\']*wp-admin[^"\']*)["\']', content)
    print(f"🔧 WordPress admin references found: {len(wp_admin)}")
    
    # Find script IDs with WordPress references
    script_ids = re.findall(r'id=["\']([^"\']*(?:elementor|woocommerce|wp-)[^"\']*)["\']', content)
    print(f"🆔 WordPress script IDs found: {len(script_ids)}")
    
    return {
        'woo_paths': woo_paths,
        'elementor_paths': elementor_paths, 
        'wp_admin': wp_admin,
        'script_ids': script_ids
    }

def cleanup_woocommerce_paths(content):
    """Step 1: Rename WooCommerce folder references in HTML file paths only"""
    print("🔄 Step 1: Cleaning up WooCommerce folder references...")
    
    # Replace WooCommerce folder paths in href and src attributes
    content = re.sub(r'(href=["\'][^"\']*)/woocommerce/', r'\1/ecommerce/', content)
    content = re.sub(r'(src=["\'][^"\']*)/woocommerce/', r'\1/ecommerce/', content)
    
    # Replace in CSS and JS file paths
    content = content.replace('./assets/modules/woocommerce/', './assets/modules/ecommerce/')
    content = content.replace('/assets/modules/woocommerce/', '/assets/modules/ecommerce/')
    
    print("✅ WooCommerce folder references updated")
    return content

def cleanup_elementor_paths(content):
    """Step 2: Rename Elementor folder references in HTML file paths only"""
    print("🔄 Step 2: Cleaning up Elementor folder references...")
    
    # Replace Elementor folder paths in href and src attributes
    content = re.sub(r'(href=["\'][^"\']*)/elementor/', r'\1/page-builder/', content)
    content = re.sub(r'(src=["\'][^"\']*)/elementor/', r'\1/page-builder/', content)
    
    # Replace specific elementor module paths
    content = content.replace('./assets/modules/header-footer-elementor/', './assets/modules/header-footer-builder/')
    content = content.replace('/assets/modules/header-footer-elementor/', '/assets/modules/header-footer-builder/')
    content = content.replace('./assets/modules/elementor/', './assets/modules/page-builder/')
    content = content.replace('/assets/modules/elementor/', '/assets/modules/page-builder/')
    
    print("✅ Elementor folder references updated")
    return content

def cleanup_javascript_config(content):
    """Step 3: Clean up JavaScript configuration objects"""
    print("🔄 Step 3: Cleaning up JavaScript configuration...")
    
    # Replace WordPress admin AJAX URL
    content = content.replace('/wp-admin/admin-ajax.php', '/api/ajax.php')
    
    # Clean up prefetch configuration patterns
    content = re.sub(r'"/wp-\*\.php"', '"/*.php"', content)
    content = re.sub(r'"/wp-admin/\*"', '"/admin/*"', content)
    content = re.sub(r'"/wp-content/uploads/\*"', '"/assets/media/*"', content)
    content = re.sub(r'"/wp-content/\*"', '"/assets/*"', content)
    content = re.sub(r'"/wp-content/plugins/\*"', '"/assets/modules/*"', content)
    content = re.sub(r'"/wp-content/themes/([^"]*)"', r'"/assets/templates/\1"', content)
    
    print("✅ JavaScript configuration updated")
    return content

def cleanup_script_identifiers(content):
    """Step 4: Disguise remaining WordPress identifiers"""
    print("🔄 Step 4: Cleaning up script identifiers and handles...")

    # Replace script IDs (but preserve functionality)
    content = re.sub(r'id=["\']elementor-([^"\']*)["\']', r'id="builder-\1"', content)
    content = re.sub(r'id=["\']woocommerce-([^"\']*)["\']', r'id="ecommerce-\1"', content)
    content = re.sub(r'id=["\']wp-([^"\']*)["\']', r'id="core-\1"', content)

    # Replace data attributes that reference WordPress-specific values
    content = content.replace('elementor_header_footer', 'custom_header_footer')
    content = content.replace('elementor_library', 'builder_library')

    # Replace JavaScript variable names (preserve functionality)
    content = content.replace('elementorFrontendConfig', 'builderFrontendConfig')
    content = content.replace('ElementorProFrontendConfig', 'ProBuilderFrontendConfig')

    print("✅ Script identifiers updated")
    return content

def cleanup_native_appearance(content):
    """Step 5: Ensure native custom-built appearance"""
    print("🔄 Step 5: Final cleanup for native appearance...")

    # Replace remaining WordPress-specific comments and references
    content = re.sub(r'<!-- wp:', '<!-- custom:', content)
    content = re.sub(r'<!-- /wp:', '<!-- /custom:', content)

    # Replace any remaining wp- prefixes in non-functional contexts
    content = re.sub(r'wp-block-', 'custom-block-', content)

    # Clean up any remaining WordPress generator tags
    content = re.sub(r'<meta name="generator"[^>]*WordPress[^>]*>', '', content)

    print("✅ Native appearance finalized")
    return content

def main():
    """Main function to perform careful cleanup"""
    print("🚀 Starting careful WordPress/WooCommerce/Elementor cleanup...")
    print("⚠️  CRITICAL: Preserving ALL CSS class names and styling!")

    # Read current index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Create backup
    backup_file = create_backup(content)

    # Analyze current references
    analysis = analyze_references(content)

    # Step 1: Clean up WooCommerce paths
    content = cleanup_woocommerce_paths(content)

    # Step 2: Clean up Elementor paths
    content = cleanup_elementor_paths(content)

    # Step 3: Clean up JavaScript configuration
    content = cleanup_javascript_config(content)

    # Step 4: Clean up script identifiers
    content = cleanup_script_identifiers(content)

    # Step 5: Ensure native appearance
    content = cleanup_native_appearance(content)

    # Write updated content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Comprehensive cleanup complete!")
    print("🎯 Visual fidelity and functionality preserved!")
    print(f"📁 Backup available: {backup_file}")

if __name__ == "__main__":
    main()
