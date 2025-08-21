#!/usr/bin/env python3
"""
Script to download all missing responsive image variants for the Peacock website
"""

import requests
import os
import re
from pathlib import Path

def download_image(url, local_path):
    """Download an image from URL to local path"""
    try:
        print(f"Downloading {url}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        # Save the image
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✅ Downloaded: {local_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error downloading {url}: {e}")
        return False

def extract_srcset_images():
    """Extract all image URLs from srcset attributes in index.html"""
    
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all srcset attributes
    srcset_pattern = r'srcset="([^"]*)"'
    srcset_matches = re.findall(srcset_pattern, content)
    
    image_urls = set()
    
    for srcset in srcset_matches:
        # Split by comma and extract URLs
        urls = re.findall(r'(\./[^\s,]*)', srcset)
        for url in urls:
            # Convert to full URL
            full_url = url.replace('./', 'https://testess-beta.vercel.app/')
            local_path = url.replace('./', '')
            image_urls.add((full_url, local_path))
    
    return list(image_urls)

def main():
    """Download all missing responsive image variants"""
    
    print("🖼️ Analyzing responsive images in Peacock website...")
    
    # Extract all image URLs from srcset attributes
    image_urls = extract_srcset_images()
    
    print(f"Found {len(image_urls)} responsive image variants to check...")
    
    # Additional specific images that are critical for responsive design
    additional_images = [
        # Logo variants
        ("https://testess-beta.vercel.app/assets/media/2024/10/peecock-08-300x74.png", "assets/media/2024/10/peecock-08-300x74.png"),
        
        # Seal variants
        ("https://testess-beta.vercel.app/assets/media/2024/10/selo-aprovado-anvisa-p_optimized-100x100.webp", "assets/media/2024/10/selo-aprovado-anvisa-p_optimized-100x100.webp"),
        ("https://testess-beta.vercel.app/assets/media/2024/10/selo-aprovado-anvisa-p_optimized-150x150.webp", "assets/media/2024/10/selo-aprovado-anvisa-p_optimized-150x150.webp"),
        
        # Dermatologically tested variants
        ("https://testess-beta.vercel.app/assets/media/2024/10/dermatologicamente-100x100.png", "assets/media/2024/10/dermatologicamente-100x100.png"),
        ("https://testess-beta.vercel.app/assets/media/2024/10/dermatologicamente-150x150.png", "assets/media/2024/10/dermatologicamente-150x150.png"),
        
        # Testimonial image variants (2025/08 series)
        ("https://testess-beta.vercel.app/assets/media/2025/08/1-277x300.png", "assets/media/2025/08/1-277x300.png"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/2-277x300.png", "assets/media/2025/08/2-277x300.png"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/3-277x300.png", "assets/media/2025/08/3-277x300.png"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/4-277x300.png", "assets/media/2025/08/4-277x300.png"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/5-277x300.png", "assets/media/2025/08/5-277x300.png"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/6-277x300.png", "assets/media/2025/08/6-277x300.png"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/7-277x300.png", "assets/media/2025/08/7-277x300.png"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/8-277x300.png", "assets/media/2025/08/8-277x300.png"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/9-277x300.png", "assets/media/2025/08/9-277x300.png"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/10-277x300.png", "assets/media/2025/08/10-277x300.png"),
        
        # Efficacy proof variants
        ("https://testess-beta.vercel.app/assets/media/2025/08/eficacia-1-240x300.jpeg", "assets/media/2025/08/eficacia-1-240x300.jpeg"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/eficacia-1-768x960.jpeg", "assets/media/2025/08/eficacia-1-768x960.jpeg"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/eficacia-1-600x750.jpeg", "assets/media/2025/08/eficacia-1-600x750.jpeg"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/eficacia-1.jpeg", "assets/media/2025/08/eficacia-1.jpeg"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/eficacia-2-240x300.jpeg", "assets/media/2025/08/eficacia-2-240x300.jpeg"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/eficacia-2-768x960.jpeg", "assets/media/2025/08/eficacia-2-768x960.jpeg"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/eficacia-2-600x750.jpeg", "assets/media/2025/08/eficacia-2-600x750.jpeg"),
        ("https://testess-beta.vercel.app/assets/media/2025/08/eficacia-2.jpeg", "assets/media/2025/08/eficacia-2.jpeg"),
    ]
    
    # Combine all images
    all_images = image_urls + additional_images
    
    # Remove duplicates
    unique_images = list(set(all_images))
    
    print(f"Total unique images to download: {len(unique_images)}")
    
    success_count = 0
    total_count = len(unique_images)
    
    for url, local_path in unique_images:
        # Check if file already exists
        if os.path.exists(local_path):
            print(f"⏭️ Skipping (already exists): {local_path}")
            success_count += 1
            continue
            
        if download_image(url, local_path):
            success_count += 1
    
    print(f"\n📊 Download Summary:")
    print(f"✅ Successfully processed: {success_count}/{total_count} images")
    
    if success_count == total_count:
        print("🎉 All responsive images are now available!")
    else:
        print(f"⚠️ {total_count - success_count} images failed to download")

if __name__ == "__main__":
    main()
