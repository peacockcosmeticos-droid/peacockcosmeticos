import React from 'react';
import { BuyButtonType } from '../../../schemas/validation';

interface HeroSectionProps {
  heading?: string;
  anvisaSeal?: string;
  buyButton?: BuyButtonType;
}

const HeroSection: React.FC<HeroSectionProps> = ({ heading, anvisaSeal, buyButton }) => {
  const handleBuyClick = (e: React.MouseEvent) => {
    e.preventDefault();
    if (buyButton?.url && buyButton.url !== '#') {
      window.open(buyButton.url, '_blank');
    } else {
      alert('Funcionalidade de compra será configurada em breve!');
    }
  };

  return (
    <section 
      className="elementor-section elementor-top-section elementor-element elementor-element-6de4cf9 elementor-section-full_width elementor-section-height-default elementor-section-height-default" 
      data-id="6de4cf9" 
      data-element_type="section"
    >
      <div className="elementor-container elementor-column-gap-default">
        <div 
          className="elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-0e86620" 
          data-id="0e86620" 
          data-element_type="column"
        >
          <div className="elementor-widget-wrap elementor-element-populated">
            
            {/* ANVISA Seal */}
            {anvisaSeal && (
              <div 
                className="elementor-element elementor-element-0e86620 elementor-widget-mobile__width-initial elementor-widget elementor-widget-image" 
                data-id="0e86620" 
                data-element_type="widget" 
                data-widget_type="image.default"
              >
                <div className="elementor-widget-container">
                  <img 
                    decoding="async" 
                    width="300" 
                    height="300" 
                    src={anvisaSeal} 
                    className="attachment-large size-large image-480" 
                    alt="Selo de aprovação ANVISA - Produto seguro e regulamentado"
                    loading="lazy"
                  />
                </div>
              </div>
            )}

            {/* Hero Heading */}
            {heading && (
              <div 
                className="elementor-element elementor-element-6de4cf9 animated-slow elementor-invisible elementor-widget elementor-widget-elementskit-heading" 
                data-id="6de4cf9" 
                data-element_type="widget" 
                data-settings='{"_animation":"fadeIn","_animation_delay":200}' 
                data-widget_type="elementskit-heading.default"
              >
                <div className="elementor-widget-container">
                  <div className="ekit-wid-con">
                    <div className="ekit-heading elementskit-section-title-wraper text_left ekit_heading_tablet- ekit_heading_mobile-">
                      <h1 
                        className="ekit-heading--title elementskit-section-title peacock-heading"
                        dangerouslySetInnerHTML={{ __html: heading }}
                      />
                    </div>
                  </div>
                </div>
              </div>
            )}

            {/* CTA Button */}
            {buyButton && (
              <div className="elementor-element elementor-element-1f29174 e-con-full e-flex e-con e-child" data-id="1f29174" data-element_type="container">
                <div className="elementor-element elementor-element-635e08f e-con-full e-flex e-con e-child" data-id="635e08f" data-element_type="container">
                  <div 
                    className="elementor-element elementor-element-aa11618 elementor-align-left animated-slow elementor-invisible elementor-widget elementor-widget-button" 
                    data-id="aa11618" 
                    data-element_type="widget" 
                    data-settings='{"_animation":"fadeIn","_animation_delay":400}' 
                    data-widget_type="button.default"
                  >
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
                </div>
              </div>
            )}

          </div>
        </div>

        {/* Right Column - Could be used for additional content */}
        <div 
          className="elementor-column elementor-col-50 elementor-top-column elementor-element elementor-element-right-col" 
          data-id="right-col" 
          data-element_type="column"
        >
          <div className="elementor-widget-wrap elementor-element-populated">
            {/* Additional hero content can be added here */}
          </div>
        </div>

      </div>
    </section>
  );
};

export default HeroSection;
