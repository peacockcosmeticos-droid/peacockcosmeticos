#!/usr/bin/env python3
"""
Asset optimization script for Peacock Cosméticos website
Optimizes images, implements lazy loading, and improves asset delivery
"""

import re
import os
import json
from PIL import Image
import shutil

def implement_lazy_loading():
    """Add lazy loading to images for better performance"""
    print("🖼️ Implementing lazy loading for images...")
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add lazy loading to images (except the first few critical ones)
    # Pattern to find img tags
    img_pattern = r'<img([^>]*?)src="([^"]*)"([^>]*?)>'
    
    def replace_img(match):
        before_src = match.group(1)
        src = match.group(2)
        after_src = match.group(3)
        
        # Skip if already has loading attribute or is a critical image
        if 'loading=' in before_src + after_src:
            return match.group(0)
        
        # Skip critical images (first banner images, logos)
        critical_images = ['banner01.jpg', 'banner03.jpg', 'peecock-08.png', 'selo-aprovado-anvisa']
        if any(critical in src for critical in critical_images):
            return match.group(0)
        
        # Add lazy loading
        return f'<img{before_src}src="{src}" loading="lazy"{after_src}>'
    
    content = re.sub(img_pattern, replace_img, content)
    
    # Write back the content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("   ✅ Lazy loading implemented for non-critical images")

def optimize_image_sizes():
    """Check and report on image optimization opportunities"""
    print("📐 Analyzing image optimization opportunities...")
    
    uploads_dir = 'wp-content/uploads'
    if not os.path.exists(uploads_dir):
        print("   ⚠️ Uploads directory not found")
        return
    
    large_images = []
    total_size = 0
    image_count = 0
    
    # Walk through all image files
    for root, dirs, files in os.walk(uploads_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                total_size += file_size
                image_count += 1
                
                # Flag large images (>500KB)
                if file_size > 500 * 1024:
                    large_images.append({
                        'path': file_path,
                        'size_kb': round(file_size / 1024, 1)
                    })
    
    print(f"   📊 Total images: {image_count}")
    print(f"   📏 Total size: {round(total_size / (1024*1024), 1)} MB")
    print(f"   ⚠️ Large images (>500KB): {len(large_images)}")
    
    if large_images:
        print("   🔍 Large images found:")
        for img in large_images[:5]:  # Show first 5
            print(f"      • {img['path']}: {img['size_kb']} KB")
    
    return {
        'total_images': image_count,
        'total_size_mb': round(total_size / (1024*1024), 1),
        'large_images': len(large_images)
    }

def add_resource_hints():
    """Add resource hints for better performance"""
    print("🚀 Adding resource hints...")
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Resource hints to add
    resource_hints = '''
	<!-- Resource Hints for Performance -->
	<link rel="preload" href="./wp-content/uploads/2024/10/banner01.jpg" as="image">
	<link rel="preload" href="./wp-content/uploads/2024/10/peecock-08.png" as="image">
	<link rel="preload" href="./wp-content/plugins/elementor/assets/css/frontend.min.css" as="style">
	<link rel="prefetch" href="./wp-content/uploads/2024/10/banner03.jpg">
	'''
    
    # Insert after the existing performance meta tags
    content = re.sub(
        r'(<!-- Performance Optimization Meta Tags -->.*?<link rel="preconnect"[^>]*>)',
        r'\1' + resource_hints,
        content,
        flags=re.DOTALL
    )
    
    # Write back the content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("   ✅ Resource hints added for critical assets")

def optimize_css_delivery():
    """Optimize CSS delivery for better performance"""
    print("🎨 Optimizing CSS delivery...")
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Critical CSS files that should load immediately
    critical_css = [
        'elementor/assets/css/frontend.min.css',
        'themes/hello-elementor/style.css',
        'uploads/elementor/css/post-16.css'
    ]
    
    # Non-critical CSS that can be loaded asynchronously
    non_critical_patterns = [
        r'(<link[^>]*woocommerce[^>]*\.css[^>]*>)',
        r'(<link[^>]*font-awesome[^>]*\.css[^>]*>)',
        r'(<link[^>]*widget-[^>]*\.css[^>]*>)',
    ]
    
    # Convert non-critical CSS to async loading
    for pattern in non_critical_patterns:
        def make_async(match):
            link_tag = match.group(1)
            if 'media=' not in link_tag:
                # Add media="print" and onload to make it async
                link_tag = link_tag.replace('>', ' media="print" onload="this.media=\'all\'">')
            return link_tag
        
        content = re.sub(pattern, make_async, content)
    
    # Write back the content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("   ✅ CSS delivery optimized with async loading")

def minify_inline_styles():
    """Minify inline styles and scripts"""
    print("🗜️ Minifying inline styles...")
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Minify inline CSS (remove extra whitespace)
    def minify_css(match):
        css_content = match.group(1)
        # Remove extra whitespace and newlines
        css_content = re.sub(r'\s+', ' ', css_content)
        css_content = re.sub(r';\s*}', '}', css_content)
        css_content = re.sub(r'{\s*', '{', css_content)
        css_content = re.sub(r';\s*', ';', css_content)
        return f'<style>{css_content.strip()}</style>'
    
    content = re.sub(r'<style[^>]*>(.*?)</style>', minify_css, content, flags=re.DOTALL)
    
    # Write back the content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("   ✅ Inline styles minified")

def add_compression_meta():
    """Add meta tags for better compression"""
    print("📦 Adding compression meta tags...")
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Compression and caching hints
    compression_meta = '''
	<!-- Compression and Caching Hints -->
	<meta http-equiv="Cache-Control" content="public, max-age=31536000">
	<meta name="format-detection" content="telephone=no">
	'''
    
    # Insert after viewport meta tag
    content = re.sub(
        r'(<meta name="viewport"[^>]*>)',
        r'\1' + compression_meta,
        content
    )
    
    # Write back the content
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("   ✅ Compression meta tags added")

def create_optimization_summary():
    """Create a summary of all optimizations"""
    print("📊 Creating optimization summary...")
    
    # Analyze final state
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count optimizations
    lazy_images = len(re.findall(r'loading="lazy"', content))
    preload_hints = len(re.findall(r'rel="preload"', content))
    async_css = len(re.findall(r'media="print"', content))
    
    # Get file sizes
    html_size = os.path.getsize('index.html')
    
    summary = {
        "asset_optimizations": {
            "lazy_loading_images": lazy_images,
            "preload_hints": preload_hints,
            "async_css_files": async_css,
            "html_size_kb": round(html_size / 1024, 1)
        },
        "performance_improvements": [
            "Implemented lazy loading for non-critical images",
            "Added resource hints for critical assets",
            "Optimized CSS delivery with async loading",
            "Minified inline styles",
            "Added compression meta tags"
        ],
        "next_steps": [
            "Consider implementing WebP format for images",
            "Set up proper caching headers on server",
            "Consider using a CDN for static assets",
            "Implement service worker for offline functionality"
        ]
    }
    
    with open('asset_optimization_report.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print("   ✅ Optimization summary created")
    return summary

def main():
    """Run all asset optimization steps"""
    print("🎯 Starting asset optimization...\n")
    
    # Run optimizations
    implement_lazy_loading()
    image_stats = optimize_image_sizes()
    add_resource_hints()
    optimize_css_delivery()
    minify_inline_styles()
    add_compression_meta()
    summary = create_optimization_summary()
    
    print("\n🎉 Asset optimization completed!")
    print("📈 Results:")
    print(f"   🖼️ Images with lazy loading: {summary['asset_optimizations']['lazy_loading_images']}")
    print(f"   🚀 Preload hints added: {summary['asset_optimizations']['preload_hints']}")
    print(f"   🎨 Async CSS files: {summary['asset_optimizations']['async_css_files']}")
    print(f"   📄 Final HTML size: {summary['asset_optimizations']['html_size_kb']} KB")
    
    if image_stats:
        print(f"   📊 Total images: {image_stats['total_images']} ({image_stats['total_size_mb']} MB)")

if __name__ == "__main__":
    main()
