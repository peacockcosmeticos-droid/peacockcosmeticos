import React from 'react';
import { DetailedTestimonialType, BuyButtonType } from '../../../schemas/validation';

interface DetailedTestimonialsProps {
  testimonials: DetailedTestimonialType[];
  buyButton?: BuyButtonType;
}

const DetailedTestimonials: React.FC<DetailedTestimonialsProps> = ({ testimonials, buyButton }) => {
  const handleBuyClick = (e: React.MouseEvent) => {
    e.preventDefault();
    if (buyButton?.url && buyButton.url !== '#') {
      window.open(buyButton.url, '_blank');
    } else {
      alert('Funcionalidade de compra será configurada em breve!');
    }
  };

  return (
    <section className="elementor-section elementor-top-section elementor-element detailed-testimonials-section">
      <div className="elementor-container elementor-column-gap-default">
        <div className="elementor-column elementor-col-100 elementor-top-column">
          <div className="elementor-widget-wrap elementor-element-populated">
            
            <div className="detailed-testimonials-grid">
              {testimonials.map((testimonial, index) => (
                <div key={index} className="detailed-testimonial-item">
                  <div className="elementor-element elementor-widget elementor-widget-text-editor">
                    <div className="elementor-widget-container">
                      <p className="testimonial-quote peacock-text">
                        "{testimonial.quote}"
                      </p>
                      <h4 className="testimonial-author peacock-heading">
                        - {testimonial.name}
                      </h4>
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {buyButton && (
              <div className="elementor-element elementor-widget elementor-widget-button">
                <div className="elementor-widget-container">
                  <div className="elementor-button-wrapper">
                    <button 
                      className="elementor-button elementor-button-link elementor-size-sm peacock-button"
                      onClick={handleBuyClick}
                      type="button"
                    >
                      <span className="elementor-button-content-wrapper">
                        <span 
                          className="elementor-button-text"
                          dangerouslySetInnerHTML={{ __html: buyButton.text }}
                        />
                      </span>
                    </button>
                  </div>
                </div>
              </div>
            )}

          </div>
        </div>
      </div>
    </section>
  );
};

export default DetailedTestimonials;
