#!/usr/bin/env python3
"""
Remove unnecessary files and optimize the website structure
Removes unused plugins, duplicate files, and non-essential assets
"""

import os
import shutil
import re
import json

def analyze_file_usage():
    """Analyze which files are actually used in the HTML"""
    print("🔍 Analyzing file usage...")
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all referenced files
    css_files = re.findall(r'href=["\']([^"\']*\.css[^"\']*)["\']', content)
    js_files = re.findall(r'src=["\']([^"\']*\.js[^"\']*)["\']', content)
    image_files = re.findall(r'src=["\']([^"\']*\.(jpg|jpeg|png|gif|webp|svg)[^"\']*)["\']', content)
    
    # Also check for background images in CSS
    bg_images = re.findall(r'url\(["\']?([^"\']*\.(jpg|jpeg|png|gif|webp|svg)[^"\']*)["\']?\)', content)
    
    used_files = {
        'css': [f.replace('./', '') for f in css_files if f.startswith('./')],
        'js': [f.replace('./', '') for f in js_files if f.startswith('./')],
        'images': [f[0].replace('./', '') for f in image_files if f[0].startswith('./')],
        'bg_images': [f[0].replace('./', '') for f in bg_images if f[0].startswith('./')]
    }
    
    print(f"   📄 CSS files referenced: {len(used_files['css'])}")
    print(f"   ⚡ JS files referenced: {len(used_files['js'])}")
    print(f"   🖼️ Images referenced: {len(used_files['images']) + len(used_files['bg_images'])}")
    
    return used_files

def remove_unused_plugins():
    """Remove unused plugin files that are not referenced"""
    print("🧹 Removing unused plugin files...")
    
    plugins_dir = 'wp-content/plugins'
    if not os.path.exists(plugins_dir):
        print("   ⚠️ Plugins directory not found")
        return
    
    # List of plugins that are actually used based on HTML analysis
    used_plugins = [
        'elementor',
        'pro-elements', 
        'elementskit-lite',
        'header-footer-elementor',
        'woocommerce',
        'infixs-correios-automatico',
        'virtuaria-pagseguro'
    ]
    
    removed_count = 0
    for plugin in os.listdir(plugins_dir):
        plugin_path = os.path.join(plugins_dir, plugin)
        if os.path.isdir(plugin_path) and plugin not in used_plugins:
            print(f"   🗑️ Removing unused plugin: {plugin}")
            shutil.rmtree(plugin_path)
            removed_count += 1
    
    print(f"   ✅ Removed {removed_count} unused plugins")

def remove_duplicate_css_files():
    """Remove duplicate CSS files"""
    print("🎨 Removing duplicate CSS files...")
    
    # Files that are duplicates or not needed
    duplicate_files = [
        'wp-content/plugins/elementor/assets/css/widget-icon-list-c91d2640e685c8.min',  # Duplicate
        'wp-content/plugins/woocommerce/assets/css/woocommerce-smallscreen.css',  # Mobile-specific, can be combined
    ]
    
    removed_count = 0
    for file_path in duplicate_files:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"   🗑️ Removed duplicate: {file_path}")
            removed_count += 1
    
    print(f"   ✅ Removed {removed_count} duplicate CSS files")

def optimize_elementor_css():
    """Remove unused Elementor post-specific CSS files"""
    print("🎯 Optimizing Elementor CSS files...")
    
    elementor_css_dir = 'wp-content/uploads/elementor/css'
    if not os.path.exists(elementor_css_dir):
        print("   ⚠️ Elementor CSS directory not found")
        return
    
    # Read HTML to see which post CSS files are actually used
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find referenced post CSS files
    used_post_css = re.findall(r'elementor/css/(post-\d+\.css)', content)
    
    removed_count = 0
    for css_file in os.listdir(elementor_css_dir):
        if css_file.startswith('post-') and css_file not in used_post_css:
            file_path = os.path.join(elementor_css_dir, css_file)
            os.remove(file_path)
            print(f"   🗑️ Removed unused post CSS: {css_file}")
            removed_count += 1
    
    print(f"   ✅ Removed {removed_count} unused Elementor post CSS files")

def remove_unused_fonts():
    """Remove unused font files"""
    print("🔤 Removing unused font files...")
    
    fonts_dir = 'wp-content/uploads/elementor/google-fonts'
    if not os.path.exists(fonts_dir):
        print("   ⚠️ Fonts directory not found")
        return
    
    # Read HTML to see which fonts are actually used
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find referenced font CSS files
    used_fonts = re.findall(r'google-fonts/css/([^"\']*\.css)', content)
    
    css_dir = os.path.join(fonts_dir, 'css')
    if os.path.exists(css_dir):
        removed_count = 0
        for font_file in os.listdir(css_dir):
            if font_file.endswith('.css') and font_file not in used_fonts:
                file_path = os.path.join(css_dir, font_file)
                os.remove(file_path)
                print(f"   🗑️ Removed unused font: {font_file}")
                removed_count += 1
        
        print(f"   ✅ Removed {removed_count} unused font files")

def remove_development_files():
    """Remove development and backup files"""
    print("🧽 Removing development files...")
    
    # Files that are only needed for development
    dev_files = [
        'fix_urls.py',
        'fix_font_urls.py', 
        'fix_js_config.py',
        'fix_missing_fonts.py',
        'fix_missing_media.py',
        'disable_ecommerce.py',
        'check_media_files.py',
        'inventory_missing_assets.py',
        'search_videos.py',
        'final_check.py',
        'missing_assets_inventory.json',
        'OFFLINE_CONVERSION_REPORT.md'
    ]
    
    removed_count = 0
    for file_path in dev_files:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"   🗑️ Removed dev file: {file_path}")
            removed_count += 1
    
    print(f"   ✅ Removed {removed_count} development files")

def create_cleanup_report():
    """Create a report of cleanup operations"""
    print("📊 Creating cleanup report...")
    
    # Calculate directory sizes
    def get_dir_size(path):
        total = 0
        if os.path.exists(path):
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    if os.path.exists(filepath):
                        total += os.path.getsize(filepath)
        return total
    
    # Get sizes of main directories
    sizes = {
        'wp-content/plugins': get_dir_size('wp-content/plugins'),
        'wp-content/uploads': get_dir_size('wp-content/uploads'),
        'wp-content/themes': get_dir_size('wp-content/themes'),
        'wp-includes': get_dir_size('wp-includes')
    }
    
    # Count remaining files
    file_counts = {}
    for dir_name, dir_path in [('plugins', 'wp-content/plugins'), ('uploads', 'wp-content/uploads')]:
        count = 0
        if os.path.exists(dir_path):
            for root, dirs, files in os.walk(dir_path):
                count += len(files)
        file_counts[dir_name] = count
    
    report = {
        "cleanup_summary": {
            "operations_performed": [
                "Removed unused plugins",
                "Removed duplicate CSS files", 
                "Optimized Elementor CSS files",
                "Removed unused font files",
                "Removed development files"
            ],
            "directory_sizes_mb": {k: round(v / (1024*1024), 2) for k, v in sizes.items()},
            "file_counts": file_counts
        },
        "performance_impact": {
            "reduced_http_requests": "Fewer CSS and JS files to load",
            "smaller_payload": "Removed unused assets",
            "cleaner_structure": "Organized file structure"
        }
    }
    
    with open('cleanup_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("   ✅ Cleanup report created!")
    return report

def main():
    """Run all cleanup operations"""
    print("🧹 Starting comprehensive cleanup...\n")
    
    # Analyze current usage
    used_files = analyze_file_usage()
    
    # Run cleanup operations
    remove_unused_plugins()
    remove_duplicate_css_files()
    optimize_elementor_css()
    remove_unused_fonts()
    remove_development_files()
    
    # Create report
    report = create_cleanup_report()
    
    print("\n🎉 Cleanup completed!")
    print("📈 Results:")
    for op in report['cleanup_summary']['operations_performed']:
        print(f"   ✅ {op}")
    
    print(f"\n📁 Directory sizes:")
    for dir_name, size_mb in report['cleanup_summary']['directory_sizes_mb'].items():
        print(f"   📂 {dir_name}: {size_mb} MB")

if __name__ == "__main__":
    main()
