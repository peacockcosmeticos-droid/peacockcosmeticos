import React from 'react';
import { ProductFeatureType } from '../../../schemas/validation';

interface WhyChooseSectionProps {
  heading?: string;
  features: ProductFeatureType[];
}

const WhyChooseSection: React.FC<WhyChooseSectionProps> = ({ heading, features }) => {
  return (
    <section className="elementor-section elementor-top-section elementor-element why-choose-section">
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

            <div className="features-grid">
              {features.map((feature, index) => (
                <div key={index} className="feature-item">
                  <h4 className="elementor-icon-box-title peacock-heading">
                    <span dangerouslySetInnerHTML={{ __html: feature.title }} />
                  </h4>
                  {feature.description && (
                    <p className="peacock-text">{feature.description}</p>
                  )}
                </div>
              ))}
            </div>

          </div>
        </div>
      </div>
    </section>
  );
};

export default WhyChooseSection;
