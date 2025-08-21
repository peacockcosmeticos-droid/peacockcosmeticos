import React from 'react';
import { BuyButtonType } from '../../../schemas/validation';

interface BeforeAfterResultsProps {
  images: string[];
  buyButton?: BuyButtonType;
}

const BeforeAfterResults: React.FC<BeforeAfterResultsProps> = ({ images, buyButton }) => {
  const handleBuyClick = (e: React.MouseEvent) => {
    e.preventDefault();
    if (buyButton?.url && buyButton.url !== '#') {
      window.open(buyButton.url, '_blank');
    } else {
      alert('Funcionalidade de compra será configurada em breve!');
    }
  };

  return (
    <section className="elementor-section elementor-top-section elementor-element before-after-section">
      <div className="elementor-container elementor-column-gap-default">
        <div className="elementor-column elementor-col-100 elementor-top-column">
          <div className="elementor-widget-wrap elementor-element-populated">
            
            <div className="before-after-grid">
              {images.map((image, index) => (
                <div key={index} className="elementor-element elementor-widget elementor-widget-image">
                  <div className="elementor-widget-container">
                    <img 
                      loading="lazy" 
                      decoding="async" 
                      src={image} 
                      alt={`Resultado antes e depois do uso do sérum Peecock ${index + 1}`}
                      className="attachment-large size-large"
                    />
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

export default BeforeAfterResults;
