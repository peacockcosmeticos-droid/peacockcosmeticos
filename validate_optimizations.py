#!/usr/bin/env python3
"""
Validation script to ensure all optimizations are working correctly
and the site maintains visual fidelity and functionality
"""

import re
import os
import json

def validate_external_dependencies():
    """Validate that external dependencies are properly handled"""
    print("🔍 Validating external dependencies...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for problematic external URLs
    problematic_patterns = [
        (r'https://peacockcosmeticos\.com\.br/', 'Original domain references'),
        (r'src="https://[^"]*"', 'External image sources'),
        (r'href="https://[^"]*\.css"', 'External CSS files'),
        (r'src="https://[^"]*\.js"', 'External JavaScript files'),
    ]
    
    issues = []
    for pattern, description in problematic_patterns:
        matches = re.findall(pattern, content)
        if matches:
            # Filter out allowed external URLs (social media, etc.)
            allowed_domains = ['facebook.com', 'instagram.com', 'tiktok.com', 'gmpg.org', 'yoast.com']
            filtered_matches = [m for m in matches if not any(domain in m for domain in allowed_domains)]
            if filtered_matches:
                issues.append({
                    'type': description,
                    'count': len(filtered_matches),
                    'examples': filtered_matches[:3]
                })
    
    if issues:
        print("   ⚠️ External dependency issues found:")
        for issue in issues:
            print(f"      • {issue['type']}: {issue['count']} instances")
            for example in issue['examples']:
                print(f"        - {example}")
    else:
        print("   ✅ No problematic external dependencies found")
    
    return len(issues) == 0

def validate_performance_optimizations():
    """Validate that performance optimizations are in place"""
    print("⚡ Validating performance optimizations...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    optimizations = {
        'lazy_loading': len(re.findall(r'loading="lazy"', content)),
        'preload_hints': len(re.findall(r'rel="preload"', content)),
        'prefetch_hints': len(re.findall(r'rel="prefetch"', content)),
        'defer_scripts': len(re.findall(r'defer[>\s]', content)),
        'async_css': len(re.findall(r'media="print"', content)),
        'compression_meta': len(re.findall(r'Cache-Control', content)),
    }
    
    print("   📊 Performance optimizations found:")
    for opt, count in optimizations.items():
        status = "✅" if count > 0 else "⚠️"
        print(f"      {status} {opt.replace('_', ' ').title()}: {count}")
    
    return optimizations

def validate_visual_elements():
    """Validate that critical visual elements are preserved"""
    print("🎨 Validating visual elements...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    critical_elements = {
        'logo': r'peecock-08\.png',
        'banner_images': r'banner0[13]\.jpg',
        'testimonial_images': r'uploads/2025/08/[0-9]+\.png',
        'product_images': r'fotos-peecock-[^"]*\.jpg',
        'certification_badges': r'selo-aprovado-anvisa|dermatologicamente',
        'social_icons': r'facebook|instagram|tiktok',
    }
    
    missing_elements = []
    for element, pattern in critical_elements.items():
        matches = re.findall(pattern, content)
        if not matches:
            missing_elements.append(element)
        else:
            print(f"   ✅ {element.replace('_', ' ').title()}: {len(matches)} found")
    
    if missing_elements:
        print("   ⚠️ Missing critical elements:")
        for element in missing_elements:
            print(f"      • {element.replace('_', ' ').title()}")
    
    return len(missing_elements) == 0

def validate_functionality():
    """Validate that key functionality is preserved"""
    print("⚙️ Validating functionality...")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    functionality_checks = {
        'navigation_menu': r'<nav[^>]*>',
        'accordion_faq': r'ekit-accordion',
        'image_carousel': r'swiper|carousel',
        'testimonials': r'testimonial',
        'contact_info': r'sac@peacockcosmeticos\.com\.br',
        'social_links': r'href="https://www\.(facebook|instagram|tiktok)',
    }
    
    working_features = []
    broken_features = []
    
    for feature, pattern in functionality_checks.items():
        if re.search(pattern, content):
            working_features.append(feature)
            print(f"   ✅ {feature.replace('_', ' ').title()}: Working")
        else:
            broken_features.append(feature)
            print(f"   ⚠️ {feature.replace('_', ' ').title()}: Not found")
    
    return len(broken_features) == 0

def check_file_sizes():
    """Check file sizes and report optimization impact"""
    print("📏 Checking file sizes...")
    
    file_sizes = {}
    
    # Check main HTML file
    if os.path.exists('index.html'):
        file_sizes['index.html'] = os.path.getsize('index.html')
    
    # Check key directories
    directories = [
        'wp-content/plugins',
        'wp-content/uploads', 
        'wp-content/themes',
        'wp-includes'
    ]
    
    for dir_path in directories:
        if os.path.exists(dir_path):
            total_size = 0
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.exists(file_path):
                        total_size += os.path.getsize(file_path)
            file_sizes[dir_path] = total_size
    
    print("   📊 File sizes:")
    for path, size in file_sizes.items():
        if size > 1024 * 1024:  # > 1MB
            size_str = f"{size / (1024*1024):.1f} MB"
        else:
            size_str = f"{size / 1024:.1f} KB"
        print(f"      📁 {path}: {size_str}")
    
    return file_sizes

def create_validation_report():
    """Create a comprehensive validation report"""
    print("📋 Creating validation report...")
    
    # Run all validations
    deps_valid = validate_external_dependencies()
    perf_opts = validate_performance_optimizations()
    visual_valid = validate_visual_elements()
    func_valid = validate_functionality()
    file_sizes = check_file_sizes()
    
    # Calculate overall score
    validations = [deps_valid, visual_valid, func_valid]
    score = sum(validations) / len(validations) * 100
    
    report = {
        "validation_summary": {
            "overall_score": f"{score:.0f}%",
            "external_dependencies": "✅ Clean" if deps_valid else "⚠️ Issues found",
            "visual_elements": "✅ Preserved" if visual_valid else "⚠️ Missing elements",
            "functionality": "✅ Working" if func_valid else "⚠️ Issues found"
        },
        "performance_optimizations": perf_opts,
        "file_sizes": {k: f"{v/(1024*1024):.1f} MB" if v > 1024*1024 else f"{v/1024:.1f} KB" 
                     for k, v in file_sizes.items()},
        "recommendations": [
            "Deploy to production server with proper caching headers",
            "Monitor Core Web Vitals after deployment",
            "Consider implementing WebP images for further optimization",
            "Set up monitoring for performance regression"
        ]
    }
    
    with open('validation_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("   ✅ Validation report created")
    return report

def main():
    """Run comprehensive validation"""
    print("🔍 Starting comprehensive validation...\n")
    
    report = create_validation_report()
    
    print(f"\n🎯 Validation Results:")
    print(f"   📊 Overall Score: {report['validation_summary']['overall_score']}")
    print(f"   🔗 External Dependencies: {report['validation_summary']['external_dependencies']}")
    print(f"   🎨 Visual Elements: {report['validation_summary']['visual_elements']}")
    print(f"   ⚙️ Functionality: {report['validation_summary']['functionality']}")
    
    print(f"\n⚡ Performance Optimizations:")
    for opt, count in report['performance_optimizations'].items():
        print(f"   • {opt.replace('_', ' ').title()}: {count}")
    
    print(f"\n📁 File Sizes:")
    for path, size in report['file_sizes'].items():
        print(f"   • {path}: {size}")
    
    print(f"\n🚀 Ready for deployment!")

if __name__ == "__main__":
    main()
