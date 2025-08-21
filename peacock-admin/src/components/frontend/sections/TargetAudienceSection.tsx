import React from 'react';
import { TargetAudienceType } from '../../../schemas/validation';

interface TargetAudienceSectionProps {
  heading?: string;
  targetAudience: TargetAudienceType[];
}

const TargetAudienceSection: React.FC<TargetAudienceSectionProps> = ({ heading, targetAudience }) => {
  return (
    <section className="elementor-section elementor-top-section elementor-element target-audience-section">
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

            <div className="target-audience-grid">
              {targetAudience.map((item, index) => (
                <div key={index} className="target-audience-item">
                  <h3 className="elementskit-info-box-title peacock-heading">
                    {item.title}
                  </h3>
                  <p className="peacock-text">{item.description}</p>
                </div>
              ))}
            </div>

          </div>
        </div>
      </div>
    </section>
  );
};

export default TargetAudienceSection;
