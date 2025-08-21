#!/usr/bin/env python3
"""
Comprehensive performance optimization script for Peacock Cosméticos website
Fixes external dependencies and optimizes loading performance
"""

import re
import os
import json

def fix_external_dependencies():
    """Fix remaining external dependencies in index.html"""
    print("🔧 Fixing external dependencies...")
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix remaining external URLs
    fixes = [
        # Fix ElementsKit AJAX URL
        (r'"ajaxurl":"https:\\/\\/peacockcosmeticos\\.com\\.br\\/wp-admin\\/admin-ajax\\.php"', '"ajaxurl":"#"'),
        
        # Fix oEmbed URLs (already commented but clean them up)
        (r'https%3A%2F%2Fpeacockcosmeticos\.com\.br%2F', './'),
        
        # Disable Facebook Pixel completely
        (r"'https://connect\.facebook\.net/en_US/fbevents\.js'", "'#'"),
        (r'src="https://www\.facebook\.com/tr\?[^"]*"', 'src="#"'),
        
        # Keep social media links but add rel="noopener" for security
        (r'href="(https://www\.facebook\.com/[^"]*)"([^>]*>)', r'href="\1" rel="noopener noreferrer" target="_blank"\2'),
        (r'href="(https://www\.instagram\.com/[^"]*)"([^>]*>)', r'href="\1" rel="noopener noreferrer" target="_blank"\2'),
        (r'href="(https://www\.tiktok\.com/[^"]*)"([^>]*>)', r'href="\1" rel="noopener noreferrer" target="_blank"\2'),
    ]
    
    for pattern, replacement in fixes:
        content = re.sub(pattern, replacement, content)
    
    # Write back the fixed content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ External dependencies fixed!")

def optimize_css_loading():
    """Optimize CSS loading by combining and minifying where possible"""
    print("🎨 Optimizing CSS loading...")
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all CSS files that can be combined
    css_patterns = [
        # Remove duplicate CSS files
        (r'<link[^>]*widget-icon-list-c91d2640e685c8\.min[^>]*>\s*', ''),  # Remove duplicate icon list CSS
        
        # Add preload hints for critical CSS
        (r'(<link[^>]*elementor/assets/css/frontend\.min\.css[^>]*>)', 
         r'<link rel="preload" href="./wp-content/plugins/elementor/assets/css/frontend.min.css" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\1'),
    ]
    
    for pattern, replacement in css_patterns:
        content = re.sub(pattern, replacement, content)
    
    # Write back the optimized content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ CSS loading optimized!")

def optimize_javascript_loading():
    """Optimize JavaScript loading and remove unnecessary scripts"""
    print("⚡ Optimizing JavaScript loading...")
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # JavaScript optimizations
    js_optimizations = [
        # Add defer to non-critical scripts
        (r'(<script[^>]*wp-includes/js/underscore\.min\.js[^>]*)>', r'\1 defer>'),
        (r'(<script[^>]*wp-includes/js/wp-util\.min\.js[^>]*)>', r'\1 defer>'),
        
        # Remove or disable analytics scripts
        (r'<script[^>]*starter-templates-zip-preview[^>]*></script>\s*', ''),
        
        # Optimize Elementor scripts loading
        (r'(<script[^>]*elementor/assets/js/webpack\.runtime[^>]*)>', r'\1 defer>'),
    ]
    
    for pattern, replacement in js_optimizations:
        content = re.sub(pattern, replacement, content)
    
    # Write back the optimized content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ JavaScript loading optimized!")

def add_performance_meta_tags():
    """Add performance-related meta tags"""
    print("🚀 Adding performance meta tags...")
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Performance meta tags to add
    performance_tags = '''
	<!-- Performance Optimization Meta Tags -->
	<meta name="resource-hints" content="preload">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<link rel="dns-prefetch" href="//fonts.googleapis.com">
	<link rel="preconnect" href="//fonts.gstatic.com" crossorigin>
	'''
    
    # Insert after the viewport meta tag
    content = re.sub(
        r'(<meta name="viewport"[^>]*>)',
        r'\1' + performance_tags,
        content
    )
    
    # Write back the content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Performance meta tags added!")

def create_optimization_report():
    """Create a report of optimizations performed"""
    print("📊 Creating optimization report...")
    
    # Read the HTML file to analyze
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count resources
    css_count = len(re.findall(r'<link[^>]*\.css[^>]*>', content))
    js_count = len(re.findall(r'<script[^>]*\.js[^>]*>', content))
    img_count = len(re.findall(r'<img[^>]*>', content))
    external_urls = len(re.findall(r'https://[^"\'>\s]+', content))
    
    report = {
        "optimization_summary": {
            "css_files": css_count,
            "javascript_files": js_count,
            "images": img_count,
            "external_urls_remaining": external_urls,
            "optimizations_applied": [
                "Fixed external domain dependencies",
                "Optimized CSS loading with preload hints",
                "Added defer attributes to non-critical JavaScript",
                "Disabled Facebook Pixel for offline use",
                "Added performance meta tags",
                "Secured external social media links"
            ]
        },
        "performance_improvements": {
            "external_dependencies_removed": "peacockcosmeticos.com.br AJAX calls disabled",
            "css_optimization": "Preload hints added for critical CSS",
            "javascript_optimization": "Defer attributes added to non-critical scripts",
            "security_improvements": "Added rel='noopener noreferrer' to external links"
        },
        "recommendations": [
            "Consider combining multiple CSS files into one",
            "Implement image lazy loading for better performance",
            "Consider using WebP format for images",
            "Minify remaining CSS and JavaScript files"
        ]
    }
    
    # Save the report
    with open('performance_optimization_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("✅ Optimization report created!")
    return report

def main():
    """Run all optimization steps"""
    print("🎯 Starting comprehensive performance optimization...\n")
    
    # Run all optimization steps
    fix_external_dependencies()
    optimize_css_loading()
    optimize_javascript_loading()
    add_performance_meta_tags()
    report = create_optimization_report()
    
    print("\n🎉 Performance optimization completed!")
    print(f"📈 Results:")
    print(f"   - CSS files: {report['optimization_summary']['css_files']}")
    print(f"   - JavaScript files: {report['optimization_summary']['javascript_files']}")
    print(f"   - External URLs remaining: {report['optimization_summary']['external_urls_remaining']}")
    print(f"   - Optimizations applied: {len(report['optimization_summary']['optimizations_applied'])}")
    
    print("\n📋 Next steps:")
    for rec in report['recommendations']:
        print(f"   • {rec}")

if __name__ == "__main__":
    main()
