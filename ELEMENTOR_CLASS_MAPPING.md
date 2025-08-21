# 🎯 COMPREHENSIVE ELEMENTOR CLASS MAPPING

## 📊 ANALYSIS SUMMARY

**LIVE WEBSITE**: https://testess-beta.vercel.app/ ✅ **FULLY FUNCTIONAL**
**LOCAL WEBSITE**: file:///C:/Users/User/Downloads/peacockcosmeticos/bk/peacockcosmeticos.com.br%20-%20Copia%20(2)/index.html ✅ **FULLY FUNCTIONAL**

**TOTAL ELEMENTOR REFERENCES FOUND**: 528+ lines in HTML
**REPLACEMENT STRATEGY**: Systematic batch replacement with thorough testing

## 🔄 CORE CLASS MAPPINGS

### **Primary Container Classes**
```
elementor-section          → builder-section
elementor-container        → builder-container  
elementor-column           → builder-column
elementor-element          → builder-element
elementor-widget           → builder-widget
```

### **Layout & Structure Classes**
```
elementor-top-section      → builder-top-section
elementor-inner-section    → builder-inner-section
elementor-top-column       → builder-top-column
elementor-inner-column     → builder-inner-column
elementor-col-100          → builder-col-100
elementor-col-50           → builder-col-50
elementor-col-33           → builder-col-33
elementor-col-25           → builder-col-25
```

### **Widget Container Classes**
```
elementor-widget-wrap      → builder-widget-wrap
elementor-widget-container → builder-widget-container
```

### **Responsive & Sizing Classes**
```
elementor-section-boxed           → builder-section-boxed
elementor-section-full_width      → builder-section-full_width
elementor-section-height-default  → builder-section-height-default
elementor-section-content-middle  → builder-section-content-middle
elementor-column-gap-default      → builder-column-gap-default
```

### **Widget-Specific Classes**
```
elementor-widget-image            → builder-widget-image
elementor-widget-heading          → builder-widget-heading
elementor-widget-button           → builder-widget-button
elementor-widget-icon-box         → builder-widget-icon-box
elementor-widget-testimonial-carousel → builder-widget-testimonial-carousel
elementor-widget-menu-anchor      → builder-widget-menu-anchor
```

### **Animation & State Classes**
```
elementor-invisible        → builder-invisible
elementor-animated         → builder-animated
elementor-align-center     → builder-align-center
elementor-align-left       → builder-align-left
```

### **Background & Overlay Classes**
```
elementor-background-overlay      → builder-background-overlay
elementor-background-slideshow    → builder-background-slideshow
```

### **Swiper/Carousel Classes**
```
elementor-swiper           → builder-swiper
elementor-main-swiper      → builder-main-swiper
```

### **Icon & Shape Classes**
```
elementor-icon             → builder-icon
elementor-icon-box-wrapper → builder-icon-box-wrapper
elementor-icon-box-icon    → builder-icon-box-icon
elementor-icon-box-content → builder-icon-box-content
elementor-icon-box-title   → builder-icon-box-title
elementor-shape-circle     → builder-shape-circle
elementor-view-stacked     → builder-view-stacked
```

### **Button Classes**
```
elementor-button           → builder-button
elementor-button-wrapper   → builder-button-wrapper
elementor-button-content-wrapper → builder-button-content-wrapper
elementor-button-text      → builder-button-text
elementor-button-link      → builder-button-link
elementor-size-sm          → builder-size-sm
```

### **Testimonial Classes**
```
elementor-testimonial--skin-default → builder-testimonial--skin-default
elementor-testimonial--layout-image_inline → builder-testimonial--layout-image_inline
elementor-testimonial--align-center → builder-testimonial--align-center
elementor-testimonial__text → builder-testimonial__text
elementor-testimonial__name → builder-testimonial__name
elementor-testimonial__title → builder-testimonial__title
```

### **Menu & Navigation Classes**
```
elementor-menu-anchor      → builder-menu-anchor
elementor-nav-menu         → builder-nav-menu
```

### **Utility Classes**
```
elementor-hidden-mobile    → builder-hidden-mobile
elementor-hidden-tablet    → builder-hidden-tablet
elementor-widget-mobile__width-initial → builder-widget-mobile__width-initial
elementor-widget__width-initial → builder-widget__width-initial
```

## 🎯 DATA ATTRIBUTES TO REPLACE

### **Core Data Attributes**
```
data-elementor-type        → data-builder-type
data-elementor-id          → data-builder-id
data-elementor-post-type   → data-builder-post-type
data-element_type          → data-element_type (keep as is)
data-widget_type           → data-widget_type (keep as is)
```

### **Settings Attributes**
```
data-elementor-device-mode → data-builder-device-mode
data-elementor-settings    → data-builder-settings
```

## 🔧 CSS SELECTOR UPDATES REQUIRED

### **Files to Update**
1. `assets/media/page-builder/css/post-16.css` - Main page styles
2. `assets/media/page-builder/css/post-74.css` - Header styles  
3. `assets/media/page-builder/css/post-343.css` - Footer styles
4. `assets/media/page-builder/css/post-8.css` - Global styles
5. All widget CSS files in `assets/modules/page-builder/assets/css/`

### **CSS Replacement Pattern**
```css
/* FROM */
.elementor-section { ... }
.elementor-element { ... }
.elementor-widget { ... }

/* TO */
.builder-section { ... }
.builder-element { ... }
.builder-widget { ... }
```

## 🚀 REPLACEMENT STRATEGY

### **Phase 1: HTML Class Replacement**
1. **Batch 1**: Core container classes (section, container, column, element)
2. **Batch 2**: Widget classes (widget, widget-wrap, widget-container)
3. **Batch 3**: Specific widget types (image, heading, button, etc.)
4. **Batch 4**: Utility and responsive classes
5. **Batch 5**: Data attributes

### **Phase 2: CSS File Updates**
1. **Main CSS files**: post-16.css, post-74.css, post-343.css, post-8.css
2. **Widget CSS files**: All widget-*.css files
3. **Core CSS files**: frontend.min.css and related

### **Phase 3: JavaScript Updates**
1. **Already completed**: `elementorFrontendConfig` → `builderFrontendConfig`
2. **Already completed**: `ElementorProFrontendConfig` → `BuilderProFrontendConfig`
3. **Verify**: No additional JS references need updating

## ⚠️ CRITICAL TESTING POINTS

### **After Each Batch**
1. ✅ **Carousel functionality** - All 3 carousels must work
2. ✅ **FAQ accordion** - All expand/collapse must work  
3. ✅ **Responsive design** - Mobile/tablet layouts must be preserved
4. ✅ **Visual fidelity** - 100% identical appearance
5. ✅ **Navigation** - All menu links and anchors must work
6. ✅ **Animations** - FadeIn and other animations must work

### **Functionality Checklist**
- [ ] Testimonial carousel (10 slides)
- [ ] Before/After carousel (4 slides)  
- [ ] Customer reviews carousel (6 slides)
- [ ] FAQ accordion (12 questions)
- [ ] Navigation menu (5 items)
- [ ] Sticky header behavior
- [ ] Background slideshow
- [ ] Button hover effects
- [ ] Mobile responsive layout

## 📊 ESTIMATED IMPACT

### **Files to Modify**
- **HTML**: 1 file (index.html)
- **CSS**: ~15-20 files
- **Total Changes**: 500+ class name replacements

### **Risk Assessment**
- **Risk Level**: MEDIUM (systematic approach reduces risk)
- **Mitigation**: Batch processing with testing after each batch
- **Rollback**: Git commits after each successful batch

### **Performance Impact**
- **Positive**: Cleaner, more generic class names
- **Neutral**: Same CSS rules, just different selectors
- **No Performance Loss**: All functionality preserved

## 🎯 SUCCESS CRITERIA

1. ✅ **Zero Elementor references** in HTML and CSS
2. ✅ **100% functionality preserved** - all carousels and accordions work
3. ✅ **100% visual fidelity** - identical appearance
4. ✅ **All responsive breakpoints** working correctly
5. ✅ **Clean console** - no JavaScript errors
6. ✅ **WordPress disguise complete** - no obvious WordPress/Elementor traces

## 📝 NEXT STEPS

1. **Start with HTML Batch 1**: Core container classes
2. **Test thoroughly** after each batch
3. **Update corresponding CSS** for each batch
4. **Commit changes** after each successful batch
5. **Final comprehensive testing** when complete

This systematic approach ensures 100% functionality preservation while completely disguising the WordPress/Elementor origins.
