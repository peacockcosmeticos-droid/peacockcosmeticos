#!/usr/bin/env python3
"""
Script to update all WordPress folder path references to new structure
wp-content/ → assets/
wp-content/plugins/ → assets/modules/
wp-content/themes/ → assets/templates/
wp-content/uploads/ → assets/media/
wp-includes/ → core/
"""

import re
import os
from pathlib import Path

def update_file_paths(file_path):
    """Update WordPress paths in a single file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Update path references
        replacements = [
            # Main folder changes
            (r'\.\/wp-content\/uploads\/', './assets/media/'),
            (r'\.\/wp-content\/plugins\/', './assets/modules/'),
            (r'\.\/wp-content\/themes\/', './assets/templates/'),
            (r'\.\/wp-content\/', './assets/'),
            (r'\.\/wp-includes\/', './core/'),

            # Without leading ./
            (r'"wp-content\/uploads\/', '"assets/media/'),
            (r'"wp-content\/plugins\/', '"assets/modules/'),
            (r'"wp-content\/themes\/', '"assets/templates/'),
            (r'"wp-content\/', '"assets/'),
            (r'"wp-includes\/', '"core/'),

            # In URLs and hrefs
            (r'href=["\']\.\/wp-content\/uploads\/', 'href="./assets/media/'),
            (r'href=["\']\.\/wp-content\/plugins\/', 'href="./assets/modules/'),
            (r'href=["\']\.\/wp-content\/themes\/', 'href="./assets/templates/'),
            (r'href=["\']\.\/wp-content\/', 'href="./assets/'),
            (r'href=["\']\.\/wp-includes\/', 'href="./core/'),

            # In src attributes
            (r'src=["\']\.\/wp-content\/uploads\/', 'src="./assets/media/'),
            (r'src=["\']\.\/wp-content\/plugins\/', 'src="./assets/modules/'),
            (r'src=["\']\.\/wp-content\/themes\/', 'src="./assets/templates/'),
            (r'src=["\']\.\/wp-content\/', 'src="./assets/'),
            (r'src=["\']\.\/wp-includes\/', 'src="./core/'),
        ]

        changes_made = 0
        for pattern, replacement in replacements:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                changes_made += len(re.findall(pattern, content))
                content = new_content

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated {changes_made} path references in {file_path}")
            return changes_made
        else:
            print(f"ℹ️  No changes needed in {file_path}")
            return 0

    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")
        return 0

def main():
    """Main function to update all relevant files"""
    print("🔄 Starting WordPress path reference updates...")

    # Files to update
    files_to_update = [
        'index.html'
    ]

    # Also update CSS files in the new assets/media/elementor/css/ directory
    css_dir = Path('assets/media/elementor/css')
    if css_dir.exists():
        css_files = list(css_dir.glob('*.css'))
        files_to_update.extend([str(f) for f in css_files])

    total_changes = 0

    for file_path in files_to_update:
        if os.path.exists(file_path):
            changes = update_file_paths(file_path)
            total_changes += changes
        else:
            print(f"⚠️  File not found: {file_path}")

    print(f"\n✅ Path update complete! Total changes made: {total_changes}")

if __name__ == "__main__":
    main()