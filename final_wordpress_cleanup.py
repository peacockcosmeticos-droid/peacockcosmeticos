#!/usr/bin/env python3
"""
Final WordPress/WooCommerce Cleanup Script
- Clean remaining WooCommerce references in CSS and JS
- Update variable names and file references
- Maintain functionality while removing identifiers
"""

import re
import os
from datetime import datetime

def final_cleanup(content):
    """Final cleanup of remaining WordPress/WooCommerce references"""

    # Clean up CSS file references
    content = re.sub(r"id='woocommerce-([^']*)-css'", r"id='ecommerce-\1-css'", content)
    content = re.sub(r"woocommerce-layout\.css", "ecommerce-layout.css", content)
    content = re.sub(r"woocommerce-smallscreen\.css", "ecommerce-smallscreen.css", content)
    content = re.sub(r"woocommerce\.css", "ecommerce.css", content)

    # Clean up JavaScript file references
    content = re.sub(r"woocommerce\.min\.js", "ecommerce.min.js", content)
    content = re.sub(r"woocommerce/assets/js", "ecommerce/assets/js", content)

    # Update JavaScript variable names
    content = re.sub(r"var woocommerce_params", "var ecommerce_params", content)
    content = re.sub(r'"woocommerce":', '"ecommerce":', content)
    content = re.sub(r"woocommerce_notices_elements", "ecommerce_notices_elements", content)

    # Clean up CSS style blocks
    content = re.sub(r"id='woocommerce-inline-inline-css'", "id='ecommerce-inline-inline-css'", content)

    # Update remaining WooCommerce references in configuration
    content = re.sub(r'"wc-ajax=', '"ajax=', content)
    content = re.sub(r'wc-10\.1\.0', '1.0.0', content)

    # Clean up block references
    content = re.sub(r"ecommerce-blocks\.css\?ver=wc-10\.1\.0", "ecommerce-blocks.css?ver=1.0.0", content)

    return content

def main():
    """Main function to process the HTML file"""
    print("🔄 Starting final WordPress/WooCommerce cleanup...")

    # Read the current index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Create backup
    backup_filename = f'index_final_cleanup_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
    with open(backup_filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Backup created: {backup_filename}")

    # Apply final cleanup
    print("🔄 Applying final cleanup...")
    content = final_cleanup(content)

    # Write the updated content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Final WordPress/WooCommerce cleanup complete!")
    print("📊 Changes applied:")
    print("   - Cleaned CSS file references")
    print("   - Updated JavaScript variable names")
    print("   - Removed remaining WooCommerce identifiers")

if __name__ == "__main__":
    main()