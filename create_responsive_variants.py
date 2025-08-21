#!/usr/bin/env python3
"""
Script to create missing responsive image variants for the Peacock website
"""

import os
from PIL import Image
import re
from pathlib import Path

def create_image_variant(source_path, target_path, target_width, target_height=None):
    """Create a resized variant of an image"""
    try:
        if os.path.exists(target_path):
            print(f"⏭️ Skipping (already exists): {target_path}")
            return True
            
        if not os.path.exists(source_path):
            print(f"❌ Source image not found: {source_path}")
            return False
            
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        # Open and resize image
        with Image.open(source_path) as img:
            # Convert to RGB if necessary (for JPEG output)
            if img.mode in ('RGBA', 'LA', 'P'):
                if target_path.lower().endswith(('.jpg', '.jpeg')):
                    # Create white background for JPEG
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                elif target_path.lower().endswith('.png'):
                    img = img.convert('RGBA')
            
            # Calculate dimensions maintaining aspect ratio
            original_width, original_height = img.size
            
            if target_height is None:
                # Calculate height based on width and aspect ratio
                aspect_ratio = original_height / original_width
                target_height = int(target_width * aspect_ratio)
            else:
                # Use provided dimensions
                pass
            
            # Resize image
            resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
            
            # Save with appropriate quality
            if target_path.lower().endswith(('.jpg', '.jpeg')):
                resized_img.save(target_path, 'JPEG', quality=85, optimize=True)
            elif target_path.lower().endswith('.png'):
                resized_img.save(target_path, 'PNG', optimize=True)
            elif target_path.lower().endswith('.webp'):
                resized_img.save(target_path, 'WEBP', quality=85, optimize=True)
            
            print(f"✅ Created: {target_path} ({target_width}x{target_height})")
            return True
            
    except Exception as e:
        print(f"❌ Error creating {target_path}: {e}")
        return False

def create_responsive_variants():
    """Create all missing responsive image variants"""
    
    variants_to_create = [
        # Logo variants
        {
            "source": "assets/media/2024/10/peecock-08.png",
            "variants": [
                ("assets/media/2024/10/peecock-08-300x74.png", 300, 74)
            ]
        },
        
        # Seal variants
        {
            "source": "assets/media/2024/10/selo-aprovado-anvisa-p_optimized.webp",
            "variants": [
                ("assets/media/2024/10/selo-aprovado-anvisa-p_optimized-100x100.webp", 100, 100),
                ("assets/media/2024/10/selo-aprovado-anvisa-p_optimized-150x150.webp", 150, 150)
            ]
        },
        
        # Dermatologically tested variants
        {
            "source": "assets/media/2024/10/dermatologicamente.png",
            "variants": [
                ("assets/media/2024/10/dermatologicamente-100x100.png", 100, 100),
                ("assets/media/2024/10/dermatologicamente-150x150.png", 150, 150)
            ]
        },
        
        # Testimonial image variants (2025/08 series)
        {
            "source": "assets/media/2025/08/1.png",
            "variants": [
                ("assets/media/2025/08/1-277x300.png", 277, 300)
            ]
        },
        {
            "source": "assets/media/2025/08/2.png",
            "variants": [
                ("assets/media/2025/08/2-277x300.png", 277, 300)
            ]
        },
        {
            "source": "assets/media/2025/08/3.png",
            "variants": [
                ("assets/media/2025/08/3-277x300.png", 277, 300)
            ]
        },
        {
            "source": "assets/media/2025/08/4.png",
            "variants": [
                ("assets/media/2025/08/4-277x300.png", 277, 300)
            ]
        },
        {
            "source": "assets/media/2025/08/5.png",
            "variants": [
                ("assets/media/2025/08/5-277x300.png", 277, 300)
            ]
        },
        {
            "source": "assets/media/2025/08/6.png",
            "variants": [
                ("assets/media/2025/08/6-277x300.png", 277, 300)
            ]
        },
        {
            "source": "assets/media/2025/08/7.png",
            "variants": [
                ("assets/media/2025/08/7-277x300.png", 277, 300)
            ]
        },
        {
            "source": "assets/media/2025/08/8.png",
            "variants": [
                ("assets/media/2025/08/8-277x300.png", 277, 300)
            ]
        },
        {
            "source": "assets/media/2025/08/9.png",
            "variants": [
                ("assets/media/2025/08/9-277x300.png", 277, 300)
            ]
        },
        {
            "source": "assets/media/2025/08/10.png",
            "variants": [
                ("assets/media/2025/08/10-277x300.png", 277, 300)
            ]
        },
        
        # Before/after image variants (critical for mobile)
        {
            "source": "assets/media/2024/10/fotos-peecock-20novonovo-683x1024.jpg",
            "variants": [
                ("assets/media/2024/10/fotos-peecock-20novonovo-200x300.jpg", 200, 300),
                ("assets/media/2024/10/fotos-peecock-20novonovo-768x1152.jpg", 768, 1152),
                ("assets/media/2024/10/fotos-peecock-20novonovo.jpg", 683, 1024)  # Original size
            ]
        },
        {
            "source": "assets/media/2024/10/fotos-peecock-21novonovo-682x1024.jpg",
            "variants": [
                ("assets/media/2024/10/fotos-peecock-21novonovo-200x300.jpg", 200, 300),
                ("assets/media/2024/10/fotos-peecock-21novonovo.jpg", 682, 1024)  # Original size
            ]
        },
        {
            "source": "assets/media/2024/10/fotos-peecock-34novonovo-683x1024.jpg",
            "variants": [
                ("assets/media/2024/10/fotos-peecock-34novonovo-200x300.jpg", 200, 300),
                ("assets/media/2024/10/fotos-peecock-34novonovo-768x1152.jpg", 768, 1152),
                ("assets/media/2024/10/fotos-peecock-34novonovo.jpg", 683, 1024)  # Original size
            ]
        },
        {
            "source": "assets/media/2024/10/fotos-peecock-37novonovo-683x1024.jpg",
            "variants": [
                ("assets/media/2024/10/fotos-peecock-37novonovo-200x300.jpg", 200, 300),
                ("assets/media/2024/10/fotos-peecock-37novonovo-768x1152.jpg", 768, 1152),
                ("assets/media/2024/10/fotos-peecock-37novonovo.jpg", 683, 1024)  # Original size
            ]
        },
        
        # Efficacy proof variants
        {
            "source": "assets/media/2025/08/eficacia-1-819x1024.jpeg",
            "variants": [
                ("assets/media/2025/08/eficacia-1-240x300.jpeg", 240, 300),
                ("assets/media/2025/08/eficacia-1-768x960.jpeg", 768, 960)
            ]
        },
        {
            "source": "assets/media/2025/08/eficacia-2-819x1024.jpeg",
            "variants": [
                ("assets/media/2025/08/eficacia-2-240x300.jpeg", 240, 300),
                ("assets/media/2025/08/eficacia-2-768x960.jpeg", 768, 960)
            ]
        },
        
        # Footer image variants
        {
            "source": "assets/media/2024/10/image-300x133.png",
            "variants": [
                ("assets/media/2024/10/image.png", 400, 177)  # Original size based on aspect ratio
            ]
        },
        {
            "source": "assets/media/2024/10/image-1-300x99.png",
            "variants": [
                ("assets/media/2024/10/image-1.png", 391, 129)  # Original size based on aspect ratio
            ]
        }
    ]
    
    print("🖼️ Creating missing responsive image variants...")
    
    total_variants = sum(len(item["variants"]) for item in variants_to_create)
    success_count = 0
    
    for item in variants_to_create:
        source_path = item["source"]
        
        if not os.path.exists(source_path):
            print(f"⚠️ Source image not found: {source_path}")
            continue
            
        for variant_path, width, height in item["variants"]:
            if create_image_variant(source_path, variant_path, width, height):
                success_count += 1
    
    print(f"\n📊 Creation Summary:")
    print(f"✅ Successfully created: {success_count}/{total_variants} variants")
    
    if success_count == total_variants:
        print("🎉 All responsive image variants are now available!")
    else:
        print(f"⚠️ {total_variants - success_count} variants failed to create")

if __name__ == "__main__":
    create_responsive_variants()
