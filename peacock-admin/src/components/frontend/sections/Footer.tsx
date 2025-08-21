import React from 'react';
import { SocialMediaType, CompanyType } from '../../../schemas/validation';

interface FooterProps {
  logo?: string;
  socialMedia?: SocialMediaType;
  company?: CompanyType;
  trustBadges: string[];
}

const Footer: React.FC<FooterProps> = ({ logo, socialMedia, company, trustBadges }) => {
  return (
    <footer id="colophon" itemScope itemType="#">
      <div 
        data-elementor-type="post" 
        data-elementor-id="343" 
        className="elementor elementor-343" 
        data-elementor-post-type="header-footer"
      >
        <section 
          className="elementor-section elementor-top-section elementor-element elementor-element-footer elementor-section-full_width elementor-section-height-default" 
          data-id="footer" 
          data-element_type="section"
        >
          <div className="elementor-container elementor-column-gap-default">
            
            {/* Logo Column */}
            <div 
              className="elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-logo-col" 
              data-id="logo-col" 
              data-element_type="column"
            >
              <div className="elementor-widget-wrap elementor-element-populated">
                {logo && (
                  <div className="elementor-element elementor-widget elementor-widget-image">
                    <div className="elementor-widget-container">
                      <img 
                        loading="lazy" 
                        decoding="async" 
                        width="300" 
                        height="73" 
                        src={logo} 
                        className="attachment-medium size-medium footer-logo" 
                        alt={`Logo ${company?.name}`}
                      />
                    </div>
                  </div>
                )}
              </div>
            </div>

            {/* Social Media Column */}
            <div 
              className="elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-social-col" 
              data-id="social-col" 
              data-element_type="column"
            >
              <div className="elementor-widget-wrap elementor-element-populated">
                {socialMedia && (
                  <div className="elementor-element elementor-widget elementor-widget-social-icons">
                    <div className="elementor-widget-container">
                      <div className="elementor-social-icons-wrapper elementor-grid">
                        
                        {socialMedia.facebook && (
                          <span className="elementor-grid-item">
                            <a 
                              className="elementor-icon elementor-social-icon elementor-social-icon-facebook elementor-repeater-item-facebook" 
                              href={socialMedia.facebook} 
                              target="_blank" 
                              rel="noopener noreferrer"
                            >
                              <span className="elementor-screen-only">Facebook</span>
                              <i className="fab fa-facebook"></i>
                            </a>
                          </span>
                        )}

                        {socialMedia.instagram && (
                          <span className="elementor-grid-item">
                            <a 
                              className="elementor-icon elementor-social-icon elementor-social-icon-instagram elementor-repeater-item-instagram" 
                              href={socialMedia.instagram} 
                              target="_blank" 
                              rel="noopener noreferrer"
                            >
                              <span className="elementor-screen-only">Instagram</span>
                              <i className="fab fa-instagram"></i>
                            </a>
                          </span>
                        )}

                        {socialMedia.tiktok && (
                          <span className="elementor-grid-item">
                            <a 
                              className="elementor-icon elementor-social-icon elementor-social-icon-tiktok elementor-repeater-item-tiktok" 
                              href={socialMedia.tiktok} 
                              target="_blank" 
                              rel="noopener noreferrer"
                            >
                              <span className="elementor-screen-only">TikTok</span>
                              <i className="fab fa-tiktok"></i>
                            </a>
                          </span>
                        )}

                      </div>
                    </div>
                  </div>
                )}
              </div>
            </div>

            {/* Trust Badges Column */}
            <div 
              className="elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-trust-col" 
              data-id="trust-col" 
              data-element_type="column"
            >
              <div className="elementor-widget-wrap elementor-element-populated">
                <div className="trust-badges-grid">
                  {trustBadges.map((badge, index) => (
                    <div key={index} className="elementor-element elementor-widget elementor-widget-image">
                      <div className="elementor-widget-container">
                        <img 
                          loading="lazy" 
                          decoding="async" 
                          src={badge} 
                          className="attachment-medium size-medium trust-badge" 
                          alt={`Selo de confiança ${index + 1}`}
                        />
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>

          </div>
        </section>

        {/* Copyright Section */}
        <section 
          className="elementor-section elementor-top-section elementor-element elementor-element-copyright elementor-section-full_width elementor-section-height-default" 
          data-id="copyright" 
          data-element_type="section"
        >
          <div className="elementor-container elementor-column-gap-default">
            <div 
              className="elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-copyright-col" 
              data-id="copyright-col" 
              data-element_type="column"
            >
              <div className="elementor-widget-wrap elementor-element-populated">
                <div className="elementor-element elementor-widget elementor-widget-text-editor">
                  <div className="elementor-widget-container">
                    <p className="copyright-text peacock-text">
                      ©2025 - {company?.name} - CNPJ: {company?.cnpj}<br />
                      {company?.address}<br />
                      SAC: {company?.email}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

      </div>
    </footer>
  );
};

export default Footer;
