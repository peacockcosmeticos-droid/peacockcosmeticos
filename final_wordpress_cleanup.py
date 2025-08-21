#!/usr/bin/env python3
"""
Comprehensive WordPress/WooCommerce/Elementor Disguise Script
- Remove all WooCommerce folder references and update to ecommerce
- Remove all Elementor references and update to generic names
- Clean WordPress-specific JavaScript configurations
- Remove unnecessary WooCommerce functionality for external checkout
- Ensure native custom-built appearance
"""

import re
import os
from datetime import datetime

def clean_woocommerce_references(content):
    """Clean WooCommerce folder references and update to ecommerce"""
    print("🔄 Cleaning WooCommerce folder references...")

    # Update folder paths from woocommerce to ecommerce
    content = re.sub(r'./assets/modules/woocommerce/', './assets/modules/ecommerce/', content)

    # Update CSS file references
    content = re.sub(r"id='woocommerce-([^']*)-css'", r"id='ecommerce-\1-css'", content)
    content = re.sub(r"woocommerce-layout\.css", "ecommerce-layout.css", content)
    content = re.sub(r"woocommerce-smallscreen\.css", "ecommerce-smallscreen.css", content)
    content = re.sub(r"woocommerce\.css", "ecommerce.css", content)

    # Update JavaScript file references
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

def clean_elementor_references(content):
    """Clean Elementor references and update to generic names"""
    print("🔄 Cleaning Elementor references...")

    # Update folder paths from elementor to generic names
    content = re.sub(r'./assets/modules/elementor/', './assets/modules/page-builder/', content)
    content = re.sub(r'./assets/modules/elementor-pro/', './assets/modules/pro-builder/', content)
    content = re.sub(r'./assets/modules/header-footer-elementor/', './assets/modules/header-footer/', content)
    content = re.sub(r'./assets/modules/pro-elements/', './assets/modules/pro-elements/', content)
    content = re.sub(r'./assets/media/elementor/', './assets/media/builder/', content)

    # Update CSS IDs and references
    content = re.sub(r"id='elementor-([^']*)-css'", r"id='builder-\1-css'", content)
    content = re.sub(r"id='hfe-([^']*)-css'", r"id='header-footer-\1-css'", content)

    # Update theme references
    content = re.sub(r'hello-elementor', 'custom-theme', content)

    return content

def clean_css_classes(content):
    """Clean WordPress/Elementor-specific CSS classes"""
    print("🔄 Cleaning CSS classes...")

    # Update body classes
    content = re.sub(r'theme-hello-elementor', 'theme-custom', content)
    content = re.sub(r'child-theme-hello-elementor-child', 'child-theme-custom', content)
    content = re.sub(r'hello-elementor-default', 'custom-theme-default', content)
    content = re.sub(r'elementor-default', 'builder-default', content)
    content = re.sub(r'elementor-template-full-width', 'builder-template-full-width', content)
    content = re.sub(r'elementor-kit-8', 'builder-kit-8', content)
    content = re.sub(r'elementor-page', 'builder-page', content)
    content = re.sub(r'ehf-template-hello-elementor', 'ehf-template-custom', content)
    content = re.sub(r'ehf-stylesheet-hello-elementor-child', 'ehf-stylesheet-custom', content)

    # Update data attributes
    content = re.sub(r'data-elementor-type', 'data-builder-type', content)
    content = re.sub(r'data-elementor-id', 'data-builder-id', content)
    content = re.sub(r'data-elementor-post-type', 'data-builder-post-type', content)
    content = re.sub(r'data-element_type', 'data-element-type', content)

    # Update CSS classes in HTML
    content = re.sub(r'class="elementor', 'class="builder', content)
    content = re.sub(r'elementor-section', 'builder-section', content)
    content = re.sub(r'elementor-container', 'builder-container', content)
    content = re.sub(r'elementor-column', 'builder-column', content)
    content = re.sub(r'elementor-widget', 'builder-widget', content)
    content = re.sub(r'elementor-element', 'builder-element', content)

    return content

def clean_javascript_config(content):
    """Clean WordPress-specific JavaScript configurations"""
    print("🔄 Cleaning JavaScript configurations...")

    # Update WordPress admin URLs
    content = re.sub(r'\/wp-admin\/admin-ajax\.php', '/api/ajax.php', content)
    content = re.sub(r'"ajaxurl":"[^"]*wp-admin[^"]*"', '"ajaxurl":"/api/ajax.php"', content)

    # Update prefetch configuration to remove WordPress patterns
    prefetch_pattern = r'"prefetch":\[{"source":"document","where":{"and":\[{"href_matches":"\\\/\*"},{"not":{"href_matches":\["\\\/wp-\*\.php","\\\/wp-admin\\\\\*","\\\/wp-content\\\/uploads\\\\\*","\\\/wp-content\\\\\*","\\\/wp-content\\\/plugins\\\\\*","\\\/wp-content\\\/themes\\\/hello-elementor-child\\\\\*","\\\/wp-content\\\/themes\\\/hello-elementor\\\\\*","\\\\\*\\\\\?\(\.\+\)"\]}},{"not":{"selector_matches":"a\[rel~=\\"nofollow\\"\]"}},{"not":{"selector_matches":"\.no-prefetch, \.no-prefetch a"}}]},"eagerness":"conservative"}]'
    prefetch_replacement = r'"prefetch":[{"source":"document","where":{"and":[{"href_matches":"\\/*"},{"not":{"href_matches":["\\/*\\?(.+)"]}},{"not":{"selector_matches":"a[rel~=\\"nofollow\\"]"}},{"not":{"selector_matches":".no-prefetch, .no-prefetch a"}}]},"eagerness":"conservative"}]'
    content = re.sub(prefetch_pattern, prefetch_replacement, content)

    # Update Elementor configuration object names
    content = re.sub(r'var elementorFrontendConfig', 'var builderFrontendConfig', content)
    content = re.sub(r'var ElementorProFrontendConfig', 'var ProBuilderFrontendConfig', content)

    # Update asset URLs in JavaScript
    content = re.sub(r'"assets":"\.\/assets\/modules\/elementor\/assets\/"', '"assets":"./assets/modules/page-builder/assets/"', content)
    content = re.sub(r'"assets":"\.\/assets\/modules\/pro-elements\/assets\/"', '"assets":"./assets/modules/pro-builder/assets/"', content)

    # Update upload URLs
    content = re.sub(r'"uploadUrl":"\.\/assets\/media"', '"uploadUrl":"./assets/media"', content)

    return content

def remove_unnecessary_woocommerce_functionality(content):
    """Remove unnecessary WooCommerce functionality for external checkout"""
    print("🔄 Removing unnecessary WooCommerce functionality...")

    # Remove WooCommerce cart-related JavaScript variables
    content = re.sub(r'var wc_add_to_cart_params = {[^}]+};', '', content)

    # Remove WooCommerce-specific menu cart configuration
    content = re.sub(r'"menu_cart":{"cart_page_url":"[^"]*","checkout_page_url":"[^"]*","fragments_nonce":"[^"]*"}', '"menu_cart":{"enabled":false}', content)

    # Update ecommerce configuration to be more generic
    content = re.sub(r'"ecommerce":', '"shop":', content)
    content = re.sub(r'ecommerce_notices_elements', 'shop_notices_elements', content)

    return content

def ensure_native_appearance(content):
    """Ensure all remaining references look like custom-built website"""
    print("🔄 Ensuring native custom-built appearance...")

    # Update generator meta tag
    content = re.sub(r'content="Elementor [^"]*"', 'content="Custom Page Builder 1.0.0"', content)

    # Update any remaining WordPress-specific comments
    content = re.sub(r'<!-- WordPress[^>]*-->', '<!-- Custom CMS -->', content)
    content = re.sub(r'<!-- Elementor[^>]*-->', '<!-- Page Builder -->', content)

    # Update script IDs to be more generic
    content = re.sub(r'id="elementor-([^"]*)-js"', r'id="builder-\1-js"', content)
    content = re.sub(r'id="elementskit-([^"]*)-js"', r'id="elements-\1-js"', content)

    # Update any remaining theme references
    content = re.sub(r'hello-theme-', 'custom-theme-', content)

    # Clean up any remaining WordPress-specific nonces or tokens
    content = re.sub(r'"nonce":"[a-f0-9]{10}"', '"nonce":"custom_token"', content)

    return content

def final_pass_cleanup(content):
    """Final pass to catch remaining references"""
    print("🔄 Final pass cleanup for remaining references...")

    # Clean remaining elementor CSS classes that weren't caught
    content = re.sub(r'elementor-col-(\d+)', r'builder-col-\1', content)
    content = re.sub(r'elementor-top-column', 'builder-top-column', content)
    content = re.sub(r'elementor-inner-column', 'builder-inner-column', content)
    content = re.sub(r'elementor-size-default', 'builder-size-default', content)
    content = re.sub(r'elementor-align-', 'builder-align-', content)
    content = re.sub(r'elementor-hidden-', 'builder-hidden-', content)
    content = re.sub(r'elementor-invisible', 'builder-invisible', content)
    content = re.sub(r'elementor-animation', 'builder-animation', content)
    content = re.sub(r'elementor-button', 'builder-button', content)
    content = re.sub(r'elementor-heading-title', 'builder-heading-title', content)
    content = re.sub(r'elementor-icon-list', 'builder-icon-list', content)
    content = re.sub(r'elementor-inline-items', 'builder-inline-items', content)
    content = re.sub(r'elementor-inline-item', 'builder-inline-item', content)
    content = re.sub(r'elementor-repeater-item', 'builder-repeater-item', content)
    content = re.sub(r'elementor-testimonial', 'builder-testimonial', content)
    content = re.sub(r'elementor-swiper-button', 'builder-swiper-button', content)
    content = re.sub(r'elementor-arrows-position', 'builder-arrows-position', content)
    content = re.sub(r'elementor-pagination-position', 'builder-pagination-position', content)
    content = re.sub(r'elementor-view-stacked', 'builder-view-stacked', content)
    content = re.sub(r'elementor-shape-circle', 'builder-shape-circle', content)
    content = re.sub(r'elementor-position-top', 'builder-position-top', content)
    content = re.sub(r'elementor-mobile-position-top', 'builder-mobile-position-top', content)
    content = re.sub(r'elementor-mobile-align-center', 'builder-mobile-align-center', content)
    content = re.sub(r'elementor-absolute', 'builder-absolute', content)
    content = re.sub(r'elementor-wrapper', 'builder-wrapper', content)
    content = re.sub(r'elementor-open-inline', 'builder-open-inline', content)

    # Clean remaining WordPress admin references
    content = re.sub(r'\/wp-admin\/admin-ajax\.php', '/api/ajax.php', content)
    content = re.sub(r'"url":"[^"]*wp-admin[^"]*"', '"url":"/api/ajax.php"', content)

    # Clean remaining script references
    content = re.sub(r'elementor/lazyload/observe', 'builder/lazyload/observe', content)

    # Clean remaining data attributes
    content = re.sub(r'data-builder-post-type="elementor_library"', 'data-builder-post-type="builder_library"', content)

    # Clean remaining CSS file names in file paths
    content = re.sub(r'header-footer-elementor\.css', 'header-footer-builder.css', content)
    content = re.sub(r'elementor-icons\.min\.css', 'builder-icons.min.css', content)

    # Clean remaining JavaScript file references
    content = re.sub(r'elementor\.js', 'builder.js', content)

    return content

def main():
    """Main function to process the HTML file"""
    print("🚀 Starting comprehensive WordPress/WooCommerce/Elementor disguise...")

    # Read the current index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Create backup
    backup_filename = f'index_comprehensive_cleanup_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
    with open(backup_filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Backup created: {backup_filename}")

    # Apply comprehensive cleanup
    content = clean_woocommerce_references(content)
    content = clean_elementor_references(content)
    content = clean_css_classes(content)
    content = clean_javascript_config(content)
    content = remove_unnecessary_woocommerce_functionality(content)
    content = ensure_native_appearance(content)
    content = final_pass_cleanup(content)

    # Write the updated content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Comprehensive WordPress/WooCommerce/Elementor disguise complete!")
    print("📊 Transformations applied:")
    print("   ✅ WooCommerce → ecommerce folder structure")
    print("   ✅ Elementor → page-builder generic naming")
    print("   ✅ WordPress-specific CSS classes cleaned")
    print("   ✅ JavaScript configurations updated")
    print("   ✅ Unnecessary WooCommerce functionality removed")
    print("   ✅ Native custom-built appearance ensured")
    print("   ✅ Final pass cleanup completed")
    print("🎯 Website now appears as professionally custom-built!")

if __name__ == "__main__":
    main()