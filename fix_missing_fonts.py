#!/usr/bin/env python3
"""
Script to replace missing Google Fonts with system font fallbacks
"""

import os
import re

def fix_missing_fonts():
    font_css_dir = 'wp-content/uploads/elementor/google-fonts/css'
    
    if not os.path.exists(font_css_dir):
        print(f"Directory {font_css_dir} not found")
        return
    
    # Font fallbacks mapping
    font_fallbacks = {
        'roboto': 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
        'robotoslab': '"Times New Roman", Times, serif',
        'raleway': 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
        'montserrat': 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
        'playfairdisplay': '"Times New Roman", Times, serif',
        'opensans': 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
        'lato': 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    }
    
    # Get all CSS files in the directory
    css_files = [f for f in os.listdir(font_css_dir) if f.endswith('.css')]
    
    for css_file in css_files:
        file_path = os.path.join(font_css_dir, css_file)
        font_name = css_file.replace('.css', '')
        
        if font_name in font_fallbacks:
            # Create a simple CSS file with system font fallback
            first_font = font_fallbacks[font_name].split(",")[0].strip()
            first_font = first_font.strip('"').strip("'")

            fallback_css = f"""/* System font fallback for {font_name.title()} */
/* This replaces the original Google Font with system fonts for offline use */

/* We'll use CSS custom properties to maintain compatibility */
:root {{
    --{font_name}-font-family: {font_fallbacks[font_name]};
}}

/* Override any existing font-face declarations */
@font-face {{
    font-family: '{font_name.title()}';
    src: local('{first_font}');
    font-display: swap;
}}
"""
            
            # Write the fallback CSS
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fallback_css)
            
            print(f"Created system font fallback for {font_name}")

if __name__ == "__main__":
    fix_missing_fonts()
