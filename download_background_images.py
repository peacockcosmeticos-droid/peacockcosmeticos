#!/usr/bin/env python3
"""
Script to download missing background images for the Peacock website
"""

import requests
import os
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

def main():
    """Download all missing background images"""
    
    # Background images needed for slideshow and overlays
    images_to_download = [
        {
            "url": "https://testess-beta.vercel.app/assets/media/2024/10/banner01.jpg",
            "local_path": "assets/media/2024/10/banner01.jpg"
        },
        {
            "url": "https://testess-beta.vercel.app/assets/media/2024/10/banner03.jpg",
            "local_path": "assets/media/2024/10/banner03.jpg"
        },
        {
            "url": "https://testess-beta.vercel.app/assets/media/2024/10/peecock-03.png",
            "local_path": "assets/media/2024/10/peecock-03.png"
        },
        {
            "url": "https://testess-beta.vercel.app/assets/media/2024/10/bg01.jpg",
            "local_path": "assets/media/2024/10/bg01.jpg"
        }
    ]
    
    print("🖼️ Downloading background images for Peacock website...")
    
    success_count = 0
    total_count = len(images_to_download)
    
    for image in images_to_download:
        if download_image(image["url"], image["local_path"]):
            success_count += 1
    
    print(f"\n📊 Download Summary:")
    print(f"✅ Successfully downloaded: {success_count}/{total_count} images")
    
    if success_count == total_count:
        print("🎉 All background images downloaded successfully!")
    else:
        print(f"⚠️ {total_count - success_count} images failed to download")

if __name__ == "__main__":
    main()
