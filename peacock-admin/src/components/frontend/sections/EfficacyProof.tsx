import React from 'react';

interface EfficacyProofProps {
  images: string[];
}

const EfficacyProof: React.FC<EfficacyProofProps> = ({ images }) => {
  return (
    <section className="elementor-section elementor-top-section elementor-element efficacy-proof-section">
      <div className="elementor-container elementor-column-gap-default">
        <div className="elementor-column elementor-col-100 elementor-top-column">
          <div className="elementor-widget-wrap elementor-element-populated">
            {images.map((image, index) => (
              <div key={index} className="elementor-element elementor-widget elementor-widget-image">
                <div className="elementor-widget-container">
                  <img 
                    loading="lazy" 
                    decoding="async" 
                    src={image} 
                    alt={`Comprovação de eficácia do sérum Peecock ${index + 1}`}
                    className="attachment-large size-large"
                  />
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default EfficacyProof;
