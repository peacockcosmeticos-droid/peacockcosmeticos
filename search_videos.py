#!/usr/bin/env python3
"""
Search for video references in the scraped HTML content
"""

import re

# The scraped HTML content from Firecrawl
html_content = """<!DOCTYPE html><html lang="pt-BR"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style rel="stylesheet" type="text/css">@charset "utf-8";

img:is([sizes="auto" i], [sizes^="auto," i]) { contain-intrinsic-size: 3000px 1500px; }
</style><style rel="stylesheet" type="text/css">@charset "utf-8";

img.wp-smiley, img.emoji { display: inline !important; border: none !important; box-shadow: none !important; height: 1em !important; width: 1em !important; margin: 0px 0.07em !important; vertical-align: -0.1em !important; background: none !important; padding: 0px !important; }
</style>"""

def search_for_videos():
    print("=== SEARCHING FOR VIDEO REFERENCES ===\n")
    
    # Search for video elements
    video_patterns = [
        r'<video[^>]*src="([^"]*\.mp4)"[^>]*>',
        r'src="([^"]*\.mp4)"',
        r'href="([^"]*\.mp4)"',
        r'url\(([^)]*\.mp4)\)',
        r'([^"\s]*\.mp4)',
    ]
    
    found_videos = set()
    
    for pattern in video_patterns:
        matches = re.findall(pattern, html_content, re.IGNORECASE)
        for match in matches:
            if isinstance(match, tuple):
                video_url = match[0]
            else:
                video_url = match
            
            if video_url and '.mp4' in video_url.lower():
                found_videos.add(video_url)
                print(f"Found video: {video_url}")
    
    if not found_videos:
        print("❌ No video files found in the scraped content")
        print("\nLet me search for any video-related content...")
        
        # Search for video-related keywords
        video_keywords = ['video', 'mp4', 'CLARISSA', 'UNBOXING', 'Peecock']
        for keyword in video_keywords:
            if keyword.lower() in html_content.lower():
                print(f"✅ Found keyword '{keyword}' in content")
                # Find context around the keyword
                pattern = rf'.{{0,100}}{re.escape(keyword)}.{{0,100}}'
                matches = re.findall(pattern, html_content, re.IGNORECASE)
                for match in matches[:3]:  # Show first 3 matches
                    print(f"   Context: ...{match}...")
            else:
                print(f"❌ Keyword '{keyword}' not found")
    
    return list(found_videos)

if __name__ == "__main__":
    videos = search_for_videos()
    print(f"\n📊 Total videos found: {len(videos)}")
