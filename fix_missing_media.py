#!/usr/bin/env python3
"""
Script to fix missing media files by using available fallbacks
"""

import re
import os

def fix_missing_media():
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Define fallback mappings for missing files
    fallback_mappings = {
        # For missing sized versions, use the original or closest available size
        r'./wp-content/uploads/2024/10/dermatologicamente-\d+x\d+\.png': './wp-content/uploads/2024/10/dermatologicamente.png',
        r'./wp-content/uploads/2024/10/selo-aprovado-anvisa-p_optimized-\d+x\d+\.webp': './wp-content/uploads/2024/10/selo-aprovado-anvisa-p_optimized.webp',
        r'./wp-content/uploads/2024/10/peecock-08-\d+x\d+\.png': './wp-content/uploads/2024/10/peecock-08.png',
        
        # For missing original images, use available sized versions
        r'./wp-content/uploads/2024/10/fotos-peecock-20novonovo\.jpg': './wp-content/uploads/2024/10/fotos-peecock-20novonovo-683x1024.jpg',
        r'./wp-content/uploads/2024/10/fotos-peecock-21novonovo\.jpg': './wp-content/uploads/2024/10/fotos-peecock-21novonovo-682x1024.jpg',
        r'./wp-content/uploads/2024/10/fotos-peecock-34novonovo\.jpg': './wp-content/uploads/2024/10/fotos-peecock-34novonovo-683x1024.jpg',
        r'./wp-content/uploads/2024/10/fotos-peecock-37novonovo\.jpg': './wp-content/uploads/2024/10/fotos-peecock-37novonovo-683x1024.jpg',
        
        # For missing sized versions of photos, use available sizes
        r'./wp-content/uploads/2024/10/fotos-peecock-20novonovo-\d+x\d+\.jpg': './wp-content/uploads/2024/10/fotos-peecock-20novonovo-683x1024.jpg',
        r'./wp-content/uploads/2024/10/fotos-peecock-21novonovo-\d+x\d+\.jpg': './wp-content/uploads/2024/10/fotos-peecock-21novonovo-682x1024.jpg',
        r'./wp-content/uploads/2024/10/fotos-peecock-34novonovo-\d+x\d+\.jpg': './wp-content/uploads/2024/10/fotos-peecock-34novonovo-683x1024.jpg',
        r'./wp-content/uploads/2024/10/fotos-peecock-37novonovo-\d+x\d+\.jpg': './wp-content/uploads/2024/10/fotos-peecock-37novonovo-683x1024.jpg',
        
        # For missing image originals, use available sized versions
        r'./wp-content/uploads/2024/10/image-1\.png': './wp-content/uploads/2024/10/image-1-300x99.png',
        r'./wp-content/uploads/2024/10/image\.png': './wp-content/uploads/2024/10/image-300x133.png',
        
        # For missing 2025/08 sized versions, use originals
        r'./wp-content/uploads/2025/08/(\d+)-\d+x\d+\.png': r'./wp-content/uploads/2025/08/\1.png',
        
        # For missing videos, we'll disable them
        r'./wp-content/uploads/2025/05/[^"]*\.mp4': '#',
        
        # For missing efficacy images, we'll use a placeholder or disable
        r'./wp-content/uploads/2025/08/eficacia-[^"]*': '#',
        
        # For missing fotos-peecock-36, we'll use a similar available image
        r'./wp-content/uploads/2024/10/fotos-peecock-36[^"]*': './wp-content/uploads/2024/10/fotos-peecock-37novonovo-683x1024.jpg',
    }
    
    # Apply fallback mappings
    for pattern, replacement in fallback_mappings.items():
        content = re.sub(pattern, replacement, content)
    
    # Write the modified content back
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Missing media files fixed with fallbacks!")
    
    # Run the check again to see improvements
    print("\nRe-checking media files...")
    check_remaining_missing()

def check_remaining_missing():
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
    
    # Combine all URLs
    all_urls = img_matches + srcset_urls
    
    # Remove duplicates and filter for local files
    unique_urls = list(set(url for url in all_urls if url.startswith('./wp-content/uploads/') and url != '#'))
    
    missing_files = []
    for url in unique_urls:
        file_path = url[2:]  # Remove './' prefix
        if not os.path.exists(file_path):
            missing_files.append(url)
    
    print(f"Remaining missing files: {len(missing_files)}")
    if missing_files:
        for file in missing_files[:10]:  # Show first 10
            print(f"  - {file}")
        if len(missing_files) > 10:
            print(f"  ... and {len(missing_files) - 10} more")

if __name__ == "__main__":
    fix_missing_media()
