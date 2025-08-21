# File Structure Mapping for WordPress Disguise Transformation

## Critical Issue Identified
The HTML file paths were changed but the physical files were not moved, causing 404 errors and broken CSS loading.

## Required File/Folder Moves

### 1. WooCommerce → Ecommerce
**Current Location**: `./assets/modules/woocommerce/`
**New Location**: `./assets/modules/ecommerce/`
**Files Affected**: 
- CSS: ecommerce-layout.css, ecommerce-smallscreen.css, ecommerce.css, brands.css, ecommerce-blocks.css
- JS: jquery.blockUI.min.js, add-to-cart.min.js, js.cookie.min.js, ecommerce.min.js, sourcebuster.min.js, order-attribution.min.js

### 2. Elementor → Page-Builder
**Current Location**: `./assets/modules/elementor/`
**New Location**: `./assets/modules/page-builder/`
**Files Affected**:
- CSS: frontend.min.css, widget-*.min.css, animations, swiper, eicons, font-awesome
- JS: webpack.runtime.min.js, frontend-modules.min.js, frontend.min.js, swiper.min.js
- Lib: animations, swiper, eicons, font-awesome

### 3. Header-Footer-Elementor → Header-Footer-Builder
**Current Location**: `./assets/modules/header-footer-elementor/`
**New Location**: `./assets/modules/header-footer-builder/`
**Files Affected**:
- CSS: header-footer-elementor.css, frontend.css
- Inc: widgets-css/frontend.css

### 4. Elementor Media Files
**Current Location**: `./assets/media/elementor/`
**New Location**: `./assets/media/page-builder/`
**Files Affected**:
- CSS: post-*.css files
- Google Fonts: css files
- All subdirectories

### 5. Hello-Elementor Theme (if referenced)
**Current Location**: `./assets/templates/hello-elementor/`
**New Location**: `./assets/templates/hello-builder/` (if needed)

## HTML References That Need Physical Files
Based on HTML analysis, these paths are referenced and need actual files:

### CSS Files (47 references):
- ./assets/modules/ecommerce/assets/css/ecommerce-layout.css
- ./assets/modules/ecommerce/assets/css/ecommerce-smallscreen.css
- ./assets/modules/ecommerce/assets/css/ecommerce.css
- ./assets/modules/ecommerce/assets/css/brands.css
- ./assets/modules/ecommerce/assets/client/blocks/ecommerce-blocks.css
- ./assets/modules/header-footer-builder/inc/widgets-css/frontend.css
- ./assets/modules/header-footer-builder/assets/css/header-footer-elementor.css
- ./assets/modules/page-builder/assets/css/frontend.min.css
- ./assets/modules/page-builder/assets/css/widget-*.min.css
- ./assets/modules/page-builder/assets/lib/animations/styles/*.min.css
- ./assets/modules/page-builder/assets/lib/swiper/v8/css/swiper.min.css
- ./assets/modules/page-builder/assets/lib/eicons/css/elementor-icons.min.css
- ./assets/modules/page-builder/assets/lib/font-awesome/css/*.css
- ./assets/media/page-builder/css/post-*.css
- ./assets/media/page-builder/google-fonts/css/*.css

### JavaScript Files (10 references):
- ./assets/modules/ecommerce/assets/js/jquery-blockui/jquery.blockUI.min.js
- ./assets/modules/ecommerce/assets/js/frontend/add-to-cart.min.js
- ./assets/modules/ecommerce/assets/js/js-cookie/js.cookie.min.js
- ./assets/modules/ecommerce/assets/js/frontend/ecommerce.min.js
- ./assets/modules/ecommerce/assets/js/sourcebuster/sourcebuster.min.js
- ./assets/modules/ecommerce/assets/js/frontend/order-attribution.min.js
- ./assets/modules/page-builder/assets/js/webpack.runtime.min.js
- ./assets/modules/page-builder/assets/js/frontend-modules.min.js
- ./assets/modules/page-builder/assets/js/frontend.min.js
- ./assets/modules/page-builder/assets/lib/swiper/v8/swiper.min.js

## Action Plan
1. Move woocommerce → ecommerce
2. Move elementor → page-builder  
3. Move header-footer-elementor → header-footer-builder
4. Move assets/media/elementor → assets/media/page-builder
5. Test CSS/JS loading
6. Verify visual fidelity
7. Deploy and test live site
