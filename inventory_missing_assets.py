#!/usr/bin/env python3
"""
Comprehensive inventory of all missing media assets that need to be downloaded
"""

import re
import os
import json

def inventory_missing_assets():
    # Read the HTML file
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=== COMPREHENSIVE MISSING ASSETS INVENTORY ===\n")
    
    missing_assets = {
        "videos": [],
        "images": [],
        "icons": [],
        "fonts": [],
        "css": [],
        "other": []
    }
    
    # 1. Find all video references
    print("🎬 CHECKING VIDEO FILES...")
    video_patterns = [
        r'src="(\./wp-content/uploads/[^"]*\.mp4)"',
        r'src="(\./wp-content/uploads/[^"]*\.webm)"',
        r'src="(\./wp-content/uploads/[^"]*\.avi)"'
    ]
    
    for pattern in video_patterns:
        matches = re.findall(pattern, content)
        for match in matches:
            file_path = match[2:]  # Remove './' prefix
            if not os.path.exists(file_path):
                missing_assets["videos"].append({
                    "local_path": file_path,
                    "url_path": match,
                    "original_url": f"https://peacockcosmeticos.com.br/{file_path}"
                })
                print(f"❌ Missing: {match}")
    
    # 2. Find all image references
    print(f"\n🖼️  CHECKING IMAGE FILES...")
    image_patterns = [
        r'src="(\./wp-content/uploads/[^"]*\.(jpg|jpeg|png|gif|webp|svg))"',
        r'srcset="([^"]*)"',  # Will need special handling
        r'content="(\./wp-content/uploads/[^"]*\.(jpg|jpeg|png|gif|webp|svg))"',
        r'url\((\./wp-content/uploads/[^)]*\.(jpg|jpeg|png|gif|webp|svg))\)'
    ]
    
    # Handle regular src and content attributes
    for pattern in [image_patterns[0], image_patterns[2], image_patterns[3]]:
        matches = re.findall(pattern, content)
        for match in matches:
            if isinstance(match, tuple):
                file_url = match[0]
            else:
                file_url = match
            
            file_path = file_url[2:] if file_url.startswith('./') else file_url
            if not os.path.exists(file_path):
                missing_assets["images"].append({
                    "local_path": file_path,
                    "url_path": file_url,
                    "original_url": f"https://peacockcosmeticos.com.br/{file_path}"
                })
                print(f"❌ Missing: {file_url}")
    
    # Handle srcset attributes (multiple URLs)
    srcset_matches = re.findall(image_patterns[1], content)
    for srcset in srcset_matches:
        # Extract individual URLs from srcset
        urls = re.findall(r'(\./wp-content/uploads/[^\s,]*\.(jpg|jpeg|png|gif|webp|svg))', srcset)
        for url_match in urls:
            file_url = url_match[0]
            file_path = file_url[2:]
            if not os.path.exists(file_path):
                missing_assets["images"].append({
                    "local_path": file_path,
                    "url_path": file_url,
                    "original_url": f"https://peacockcosmeticos.com.br/{file_path}"
                })
                print(f"❌ Missing (srcset): {file_url}")
    
    # 3. Check for favicon and icon files
    print(f"\n🔗 CHECKING FAVICON AND ICON FILES...")
    favicon_patterns = [
        r'href="(\./wp-content/uploads/[^"]*icon[^"]*\.(png|ico|svg))"',
        r'content="(\./wp-content/uploads/[^"]*icon[^"]*\.(png|ico|svg))"'
    ]
    
    # Also check for the specific favicon files we know are missing
    known_missing_favicons = [
        "wp-content/uploads/2024/10/cropped-peecock-icon-32x32.png",
        "wp-content/uploads/2024/10/cropped-peecock-icon-192x192.png",
        "wp-content/uploads/2024/10/cropped-peecock-icon-180x180.png",
        "wp-content/uploads/2024/10/cropped-peecock-icon-270x270.png"
    ]
    
    for favicon_file in known_missing_favicons:
        if not os.path.exists(favicon_file):
            missing_assets["icons"].append({
                "local_path": favicon_file,
                "url_path": f"./{favicon_file}",
                "original_url": f"https://peacockcosmeticos.com.br/{favicon_file}"
            })
            print(f"❌ Missing favicon: {favicon_file}")
    
    # 4. Check for missing efficacy images (that we replaced with fallbacks)
    print(f"\n📊 CHECKING EFFICACY/RESULTS IMAGES...")
    known_missing_efficacy = [
        "wp-content/uploads/2025/08/eficacia-1.jpeg",
        "wp-content/uploads/2025/08/eficacia-1-819x1024.jpeg",
        "wp-content/uploads/2025/08/eficacia-1-240x300.jpeg",
        "wp-content/uploads/2025/08/eficacia-1-768x960.jpeg",
        "wp-content/uploads/2025/08/eficacia-1-600x750.jpeg",
        "wp-content/uploads/2025/08/eficacia-2.jpeg",
        "wp-content/uploads/2025/08/eficacia-2-819x1024.jpeg",
        "wp-content/uploads/2025/08/eficacia-2-240x300.jpeg",
        "wp-content/uploads/2025/08/eficacia-2-768x960.jpeg",
        "wp-content/uploads/2025/08/eficacia-2-600x750.jpeg"
    ]
    
    for efficacy_file in known_missing_efficacy:
        if not os.path.exists(efficacy_file):
            missing_assets["images"].append({
                "local_path": efficacy_file,
                "url_path": f"./{efficacy_file}",
                "original_url": f"https://peacockcosmeticos.com.br/{efficacy_file}"
            })
            print(f"❌ Missing efficacy: {efficacy_file}")
    
    # Remove duplicates
    for category in missing_assets:
        seen = set()
        unique_assets = []
        for asset in missing_assets[category]:
            if asset["local_path"] not in seen:
                seen.add(asset["local_path"])
                unique_assets.append(asset)
        missing_assets[category] = unique_assets
    
    # Summary
    print(f"\n📊 SUMMARY:")
    print(f"Videos: {len(missing_assets['videos'])} missing")
    print(f"Images: {len(missing_assets['images'])} missing")
    print(f"Icons: {len(missing_assets['icons'])} missing")
    print(f"Fonts: {len(missing_assets['fonts'])} missing")
    print(f"CSS: {len(missing_assets['css'])} missing")
    print(f"Other: {len(missing_assets['other'])} missing")
    
    total_missing = sum(len(assets) for assets in missing_assets.values())
    print(f"TOTAL: {total_missing} missing assets")
    
    # Save to JSON for later use
    with open('missing_assets_inventory.json', 'w', encoding='utf-8') as f:
        json.dump(missing_assets, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Inventory saved to: missing_assets_inventory.json")
    
    return missing_assets

if __name__ == "__main__":
    inventory_missing_assets()
