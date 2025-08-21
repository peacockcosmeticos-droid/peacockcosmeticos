import React from 'react';
import { HowToUseType, BuyButtonType } from '../../../schemas/validation';

interface HowToUseSectionProps {
  heading?: string;
  steps: HowToUseType[];
  buyButton?: BuyButtonType;
}

const HowToUseSection: React.FC<HowToUseSectionProps> = ({ heading, steps, buyButton }) => {
  const handleBuyClick = (e: React.MouseEvent) => {
    e.preventDefault();
    if (buyButton?.url && buyButton.url !== '#') {
      window.open(buyButton.url, '_blank');
    } else {
      alert('Funcionalidade de compra será configurada em breve!');
    }
  };

  return (
    <section className="elementor-section elementor-top-section elementor-element how-to-use-section">
      <div className="elementor-container elementor-column-gap-default">
        <div className="elementor-column elementor-col-100 elementor-top-column">
          <div className="elementor-widget-wrap elementor-element-populated">
            
            {heading && (
              <div className="elementor-element elementor-widget elementor-widget-elementskit-heading">
                <div className="elementor-widget-container">
                  <h2 
                    className="ekit-heading--title elementskit-section-title peacock-heading"
                    dangerouslySetInnerHTML={{ __html: heading }}
                  />
                </div>
              </div>
            )}

            <div className="how-to-use-steps">
              {steps.map((step, index) => (
                <div key={index} className="how-to-use-step">
                  <h3 className="elementskit-info-box-title peacock-heading">
                    {step.step}
                  </h3>
                  <p className="peacock-text">{step.instruction}</p>
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

export default HowToUseSection;
