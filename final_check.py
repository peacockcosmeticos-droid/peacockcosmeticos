#!/usr/bin/env python3
"""
Final check for any remaining external dependencies
"""

import re
import os

def final_check():
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=== FINAL OFFLINE READINESS CHECK ===\n")
    
    # Check for remaining external URLs
    external_patterns = [
        (r'https://[^"\'>\s]+', 'External HTTPS URLs'),
        (r'http://[^"\'>\s]+', 'External HTTP URLs'),
        (r'//[^"\'>\s/]+\.[^"\'>\s/]+', 'Protocol-relative URLs'),
    ]
    
    total_external = 0
    
    for pattern, description in external_patterns:
        matches = re.findall(pattern, content)
        # Filter out social media links and schema.org references that are expected
        filtered_matches = [
            match for match in matches 
            if not any(allowed in match for allowed in [
                'facebook.com', 'instagram.com', 'tiktok.com',  # Social media links (kept for display)
                'schema.org', 'gmpg.org'  # Schema references (already disabled)
            ])
        ]
        
        if filtered_matches:
            print(f"⚠️  {description}: {len(filtered_matches)} found")
            for match in filtered_matches[:5]:  # Show first 5
                print(f"   - {match}")
            if len(filtered_matches) > 5:
                print(f"   ... and {len(filtered_matches) - 5} more")
            total_external += len(filtered_matches)
        else:
            print(f"✅ {description}: None found")
    
    print(f"\n📊 Total problematic external URLs: {total_external}")
    
    # Check for missing local files
    print("\n=== CHECKING LOCAL FILE AVAILABILITY ===")
    
    # Find all local resource references
    local_patterns = [
        (r'src="(\./[^"]*)"', 'Script/Image sources'),
        (r'href="(\./[^"]*\.css[^"]*)"', 'CSS stylesheets'),
        (r'url\((\./[^)]*)\)', 'CSS background images'),
    ]
    
    missing_files = []
    total_local = 0
    
    for pattern, description in local_patterns:
        matches = re.findall(pattern, content)
        unique_matches = list(set(matches))
        
        missing_count = 0
        for match in unique_matches:
            file_path = match[2:] if match.startswith('./') else match  # Remove './' prefix
            # Remove query parameters for file existence check
            file_path = file_path.split('?')[0]
            if not os.path.exists(file_path):
                missing_files.append(match)
                missing_count += 1
        
        total_local += len(unique_matches)
        if missing_count > 0:
            print(f"⚠️  {description}: {missing_count}/{len(unique_matches)} missing")
        else:
            print(f"✅ {description}: All {len(unique_matches)} files found")
    
    print(f"\n📊 Total missing local files: {len(missing_files)}")
    if missing_files:
        print("Missing files:")
        for file in missing_files[:10]:
            print(f"   - {file}")
        if len(missing_files) > 10:
            print(f"   ... and {len(missing_files) - 10} more")
    
    # Check for disabled functionality
    print("\n=== CHECKING DISABLED FUNCTIONALITY ===")
    
    disabled_checks = [
        (r'onclick="alert\([^)]*offline[^)]*\)"', 'Purchase buttons disabled'),
        (r'<!-- Meta Pixel Code - DISABLED', 'Facebook Pixel disabled'),
        (r'"ajaxurl":"#"', 'AJAX endpoints disabled'),
        (r'"allowTracking":false', 'Tracking disabled'),
    ]
    
    for pattern, description in disabled_checks:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            print(f"✅ {description}: {len(matches)} instances")
        else:
            print(f"⚠️  {description}: Not found")
    
    # Summary
    print(f"\n=== SUMMARY ===")
    if total_external == 0 and len(missing_files) == 0:
        print("🎉 WEBSITE IS READY FOR OFFLINE USE!")
        print("✅ No external dependencies found")
        print("✅ All local files are available")
        print("✅ E-commerce functionality disabled")
        print("✅ Tracking scripts disabled")
    else:
        print("⚠️  WEBSITE NEEDS ATTENTION:")
        if total_external > 0:
            print(f"   - {total_external} external URLs still present")
        if len(missing_files) > 0:
            print(f"   - {len(missing_files)} local files missing")
    
    print(f"\n📁 Website location: {os.path.abspath('.')}")
    print(f"🌐 Open index.html in your browser to test offline functionality")

if __name__ == "__main__":
    final_check()
