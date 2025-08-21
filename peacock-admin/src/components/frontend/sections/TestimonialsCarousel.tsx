import React, { useEffect, useRef } from 'react';
import { TestimonialType } from '../../../schemas/validation';

interface TestimonialsCarouselProps {
  testimonials: TestimonialType[];
}

const TestimonialsCarousel: React.FC<TestimonialsCarouselProps> = ({ testimonials }) => {
  const carouselRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Initialize Swiper carousel functionality
    const initializeCarousel = () => {
      if (typeof window !== 'undefined' && carouselRef.current) {
        // Simple carousel implementation without external dependencies
        const carousel = carouselRef.current;
        const slides = carousel.querySelectorAll('.testimonial-slide');
        let currentSlide = 0;

        const showSlide = (index: number) => {
          slides.forEach((slide, i) => {
            const slideElement = slide as HTMLElement;
            slideElement.style.display = i === index ? 'block' : 'none';
          });
        };

        const nextSlide = () => {
          currentSlide = (currentSlide + 1) % slides.length;
          showSlide(currentSlide);
        };

        // Show first slide
        showSlide(0);

        // Auto-advance slides every 5 seconds
        const interval = setInterval(nextSlide, 5000);

        // Cleanup
        return () => clearInterval(interval);
      }
    };

    const cleanup = initializeCarousel();
    return cleanup;
  }, [testimonials]);

  if (!testimonials || testimonials.length === 0) {
    return null;
  }

  return (
    <section 
      className="elementor-section elementor-top-section elementor-element elementor-element-testimonials elementor-section-full_width elementor-section-height-default" 
      data-id="testimonials" 
      data-element_type="section"
    >
      <div className="elementor-container elementor-column-gap-default">
        <div 
          className="elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-testimonials-col" 
          data-id="testimonials-col" 
          data-element_type="column"
        >
          <div className="elementor-widget-wrap elementor-element-populated">
            
            {/* Testimonials Carousel */}
            <div 
              className="elementor-element elementor-element-testimonials-carousel elementor-widget elementor-widget-testimonial-carousel" 
              data-id="testimonials-carousel" 
              data-element_type="widget" 
              data-widget_type="testimonial-carousel.default"
            >
              <div className="elementor-widget-container">
                <div 
                  ref={carouselRef}
                  className="testimonials-carousel swiper-container"
                >
                  <div className="swiper-wrapper">
                    {testimonials.map((testimonial, index) => (
                      <div 
                        key={testimonial.id || index}
                        className="testimonial-slide swiper-slide"
                        style={{ display: index === 0 ? 'block' : 'none' }}
                      >
                        <div className="testimonial-content">
                          
                          {/* Customer Image */}
                          {testimonial.image && (
                            <div className="testimonial-image">
                              <div 
                                className="elementor-element elementor-element-image elementor-widget elementor-widget-image" 
                                data-element_type="widget" 
                                data-widget_type="image.default"
                              >
                                <div className="elementor-widget-container">
                                  <img 
                                    loading="lazy" 
                                    decoding="async" 
                                    width="600" 
                                    height="650" 
                                    src={testimonial.image} 
                                    className="attachment-large size-large testimonial-customer-image" 
                                    alt={`Depoimento de ${testimonial.name}`}
                                  />
                                </div>
                              </div>
                            </div>
                          )}

                          {/* Testimonial Quote */}
                          <div 
                            className="elementor-element elementor-element-quote elementor-widget elementor-widget-text-editor" 
                            data-element_type="widget" 
                            data-widget_type="text-editor.default"
                          >
                            <div className="elementor-widget-container">
                              <p className="testimonial-quote peacock-text">
                                "{testimonial.quote}"
                              </p>
                            </div>
                          </div>

                          {/* Customer Name */}
                          <div 
                            className="elementor-element elementor-element-name elementor-widget elementor-widget-heading" 
                            data-element_type="widget" 
                            data-widget_type="heading.default"
                          >
                            <div className="elementor-widget-container">
                              <h2 className="elementor-heading-title elementor-size-default peacock-heading">
                                {testimonial.name}
                              </h2>
                            </div>
                          </div>

                        </div>
                      </div>
                    ))}
                  </div>

                  {/* Navigation Dots */}
                  <div className="swiper-pagination">
                    {testimonials.map((_, index) => (
                      <span 
                        key={index}
                        className={`swiper-pagination-bullet ${index === 0 ? 'swiper-pagination-bullet-active' : ''}`}
                        onClick={() => {
                          // Handle dot click
                          const slides = carouselRef.current?.querySelectorAll('.testimonial-slide');
                          if (slides) {
                            slides.forEach((slide, i) => {
                              const slideElement = slide as HTMLElement;
                              slideElement.style.display = i === index ? 'block' : 'none';
                            });
                            
                            // Update active dot
                            const dots = carouselRef.current?.querySelectorAll('.swiper-pagination-bullet');
                            if (dots) {
                              dots.forEach((dot, i) => {
                                dot.classList.toggle('swiper-pagination-bullet-active', i === index);
                              });
                            }
                          }
                        }}
                      />
                    ))}
                  </div>

                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>
  );
};

export default TestimonialsCarousel;
