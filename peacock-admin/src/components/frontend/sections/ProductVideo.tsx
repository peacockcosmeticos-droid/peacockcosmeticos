import React from 'react';

interface ProductVideoProps {
  videoUrl?: string;
}

const ProductVideo: React.FC<ProductVideoProps> = ({ videoUrl }) => {
  if (!videoUrl) return null;

  return (
    <section className="elementor-section elementor-top-section elementor-element product-video-section">
      <div className="elementor-container elementor-column-gap-default">
        <div className="elementor-column elementor-col-100 elementor-top-column">
          <div className="elementor-widget-wrap elementor-element-populated">
            <div className="elementor-element elementor-widget elementor-widget-video">
              <div className="elementor-widget-container">
                <div className="e-hosted-video elementor-wrapper elementor-open-inline">
                  <video 
                    className="elementor-video" 
                    src={videoUrl} 
                    controls 
                    preload="metadata" 
                    controlsList="nodownload"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProductVideo;
