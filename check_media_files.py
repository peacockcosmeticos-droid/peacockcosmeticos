#!/usr/bin/env python3
"""
Script to check if all media files referenced in HTML exist locally
"""

import re
import os

def check_media_files():
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all image sources
    img_pattern = r'src="(\./wp-content/uploads/[^"]*)"'
    img_matches = re.findall(img_pattern, content)
    
    # Find all srcset references
    srcset_pattern = r'srcset="([^"]*)"'
    srcset_matches = re.findall(srcset_pattern, content)
    
    # Extract individual URLs from srcset
    srcset_urls = []
    for srcset in srcset_matches:
        # Split by comma and extract URLs
        urls = re.findall(r'(\./wp-content/uploads/[^\s,]*)', srcset)
        srcset_urls.extend(urls)
    
    # Find all background images in style attributes
    bg_pattern = r'background-image:\s*url\(([^)]*)\)'
    bg_matches = re.findall(bg_pattern, content)
    
    # Combine all URLs
    all_urls = img_matches + srcset_urls + bg_matches
    
    # Remove duplicates and filter for local files
    unique_urls = list(set(url for url in all_urls if url.startswith('./wp-content/uploads/')))
    
    print(f"Found {len(unique_urls)} unique media file references:")
    
    missing_files = []
    existing_files = []
    
    for url in sorted(unique_urls):
        # Convert URL to file path
        file_path = url[2:]  # Remove './' prefix
        
        if os.path.exists(file_path):
            existing_files.append(url)
            print(f"✓ {url}")
        else:
            missing_files.append(url)
            print(f"✗ {url} - FILE NOT FOUND")
    
    print(f"\nSummary:")
    print(f"Existing files: {len(existing_files)}")
    print(f"Missing files: {len(missing_files)}")
    
    if missing_files:
        print(f"\nMissing files:")
        for file in missing_files:
            print(f"  - {file}")
    
    return missing_files

if __name__ == "__main__":
    check_media_files()
