import React, { useEffect, useState } from 'react';
import { useContent } from '../../contexts/ContentContext';
import Header from './sections/Header';
import HeroSection from './sections/HeroSection';
import TestimonialsCarousel from './sections/TestimonialsCarousel';
import WhyChooseSection from './sections/WhyChooseSection';
import EfficacyProof from './sections/EfficacyProof';
import ProductVideo from './sections/ProductVideo';
import TargetAudienceSection from './sections/TargetAudienceSection';
import BeforeAfterResults from './sections/BeforeAfterResults';
import HowToUseSection from './sections/HowToUseSection';
import DetailedTestimonials from './sections/DetailedTestimonials';
import FAQSection from './sections/FAQSection';
import Footer from './sections/Footer';
import LoadingSpinner from '../ui/LoadingSpinner';
import ErrorMessage from '../ui/ErrorMessage';

const Homepage: React.FC = () => {
  const { content, isLoading, error, loadContent } = useContent();
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    // Load content if not already loaded
    if (!content && !isLoading) {
      loadContent();
    }
  }, [content, isLoading, loadContent]);

  useEffect(() => {
    // Add fade-in animation
    const timer = setTimeout(() => setIsVisible(true), 100);
    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    // Set page title and meta description
    if (content?.metadata) {
      document.title = content.metadata.title;
      
      // Update meta description
      const metaDescription = document.querySelector('meta[name="description"]');
      if (metaDescription) {
        metaDescription.setAttribute('content', content.metadata.description);
      }

      // Update meta keywords
      const metaKeywords = document.querySelector('meta[name="keywords"]');
      if (metaKeywords) {
        metaKeywords.setAttribute('content', content.metadata.keywords);
      }

      // Update Open Graph tags
      const ogTitle = document.querySelector('meta[property="og:title"]');
      if (ogTitle) {
        ogTitle.setAttribute('content', content.metadata.ogTitle);
      }

      const ogDescription = document.querySelector('meta[property="og:description"]');
      if (ogDescription) {
        ogDescription.setAttribute('content', content.metadata.ogDescription);
      }
    }
  }, [content]);

  if (isLoading) {
    return <LoadingSpinner message="Carregando página..." />;
  }

  if (error) {
    return (
      <ErrorMessage 
        message={error} 
        onRetry={loadContent}
        title="Erro ao carregar a página"
      />
    );
  }

  if (!content) {
    return (
      <ErrorMessage 
        message="Conteúdo não encontrado" 
        onRetry={loadContent}
        title="Conteúdo indisponível"
      />
    );
  }

  return (
    <div 
      className={`homepage transition-opacity duration-1000 ${
        isVisible ? 'opacity-100' : 'opacity-0'
      }`}
      data-rsssl="1"
    >
      {/* Page Structure matching original HTML */}
      <div id="page" className="hfeed site">
        
        {/* Header */}
        <Header 
          logo={content.images?.logo}
          buyButton={content.buyButtons?.find(btn => btn.location === 'header')}
          company={content.company}
        />

        {/* Main Content */}
        <main id="content" className="site-content">
          
          {/* Hero Section */}
          <HeroSection 
            heading={content.mainHeadings?.hero}
            anvisaSeal={content.images?.anvisaSeal}
            buyButton={content.buyButtons?.find(btn => btn.location === 'hero-section')}
          />

          {/* Testimonials Carousel */}
          <TestimonialsCarousel 
            testimonials={content.testimonials || []}
          />

          {/* Why Choose Section */}
          <WhyChooseSection 
            heading={content.mainHeadings?.whyChoose}
            features={content.productFeatures || []}
          />

          {/* Efficacy Proof */}
          <EfficacyProof 
            images={content.images?.efficacyProof || []}
          />

          {/* Product Video */}
          <ProductVideo 
            videoUrl={content.images?.productVideo}
          />

          {/* Target Audience Section */}
          <TargetAudienceSection 
            heading={content.mainHeadings?.targetAudience}
            targetAudience={content.targetAudience || []}
          />

          {/* Before/After Results */}
          <BeforeAfterResults 
            images={content.images?.beforeAfter || []}
            buyButton={content.buyButtons?.find(btn => btn.location === 'results-section')}
          />

          {/* How To Use Section */}
          <HowToUseSection 
            heading={content.mainHeadings?.howToUse}
            steps={content.howToUse || []}
            buyButton={content.buyButtons?.find(btn => btn.location === 'benefits-section')}
          />

          {/* Detailed Testimonials */}
          <DetailedTestimonials 
            testimonials={content.detailedTestimonials || []}
            buyButton={content.buyButtons?.find(btn => btn.location === 'shipping-section')}
          />

          {/* FAQ Section */}
          <FAQSection 
            faq={content.faq || []}
          />

        </main>

        {/* Footer */}
        <Footer 
          logo={content.images?.logo}
          socialMedia={content.socialMedia}
          company={content.company}
          trustBadges={content.images?.trustBadges || []}
        />

      </div>

      {/* Preserve original JavaScript functionality */}
      <script
        dangerouslySetInnerHTML={{
          __html: `
            // Preserve original elementorFrontendConfig for compatibility
            window.elementorFrontendConfig = {
              environmentMode: {edit: false, preview: false, isScriptDebug: false},
              breakpoints: {xs: 0, sm: 480, md: 768, lg: 1025, xl: 1440, xxl: 1600},
              responsive: {
                breakpoints: {
                  mobile: {value: 767, direction: "max", is_enabled: true},
                  tablet: {value: 1024, direction: "max", is_enabled: true}
                }
              },
              swiperClass: "swiper",
              kit: {
                active_breakpoints: ["viewport_mobile", "viewport_tablet"],
                global_image_lightbox: "yes"
              }
            };

            // Initialize animations on scroll
            const observeElements = () => {
              const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                  if (entry.isIntersecting) {
                    entry.target.classList.add('fadeIn');
                    entry.target.classList.remove('elementor-invisible');
                  }
                });
              }, { threshold: 0.1 });

              document.querySelectorAll('.elementor-invisible').forEach(el => {
                observer.observe(el);
              });
            };

            // Initialize when DOM is ready
            if (document.readyState === 'loading') {
              document.addEventListener('DOMContentLoaded', observeElements);
            } else {
              observeElements();
            }
          `,
        }}
      />
    </div>
  );
};

export default Homepage;
