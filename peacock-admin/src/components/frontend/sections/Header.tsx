import React from 'react';
import { BuyButtonType, CompanyType } from '../../../schemas/validation';

interface HeaderProps {
  logo?: string;
  buyButton?: BuyButtonType;
  company?: CompanyType;
}

const Header: React.FC<HeaderProps> = ({ logo, buyButton, company }) => {
  const handleBuyClick = (e: React.MouseEvent) => {
    e.preventDefault();
    if (buyButton?.url && buyButton.url !== '#') {
      window.open(buyButton.url, '_blank');
    } else {
      alert('Funcionalidade de compra será configurada em breve!');
    }
  };

  return (
    <header id="masthead" itemScope itemType="#">
      <p className="main-title bhf-hidden" itemProp="headline">
        <a href="./" title={company?.name} rel="home">
          {company?.name}
        </a>
      </p>
      
      <div 
        data-elementor-type="post" 
        data-elementor-id="74" 
        className="elementor elementor-74" 
        data-elementor-post-type="header-footer"
      >
        <section 
          className="elementor-section elementor-top-section elementor-element elementor-element-10fc2bfe elementor-section-full_width elementor-section-height-default elementor-section-height-default" 
          data-id="10fc2bfe" 
          data-element_type="section"
        >
          <div className="elementor-container elementor-column-gap-default">
            <div 
              className="elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-7b5c1b8c" 
              data-id="7b5c1b8c" 
              data-element_type="column"
            >
              <div className="elementor-widget-wrap elementor-element-populated">
                <div 
                  className="elementor-element elementor-element-4973a0c3 elementor-widget elementor-widget-image" 
                  data-id="4973a0c3" 
                  data-element_type="widget" 
                  data-widget_type="image.default"
                >
                  <div className="elementor-widget-container">
                    {logo && (
                      <img 
                        fetchPriority="high" 
                        width="600" 
                        height="147" 
                        src={logo} 
                        className="attachment-full size-full image-205" 
                        alt={`Logo ${company?.name}`}
                        loading="eager"
                      />
                    )}
                  </div>
                </div>
              </div>
            </div>
            
            <div 
              className="elementor-column elementor-col-33 elementor-top-column elementor-element elementor-element-2b5c8e6" 
              data-id="2b5c8e6" 
              data-element_type="column"
            >
              <div className="elementor-widget-wrap elementor-element-populated">
                <div 
                  className="elementor-element elementor-element-5b8c1a4 elementor-nav-menu__align-center elementor-nav-menu--dropdown-tablet elementor-nav-menu__text-align-aside elementor-nav-menu--toggle elementor-nav-menu--burger elementor-widget elementor-widget-nav-menu" 
                  data-id="5b8c1a4" 
                  data-element_type="widget" 
                  data-widget_type="nav-menu.default"
                >
                  <div className="elementor-widget-container">
                    <nav className="elementor-nav-menu--main elementor-nav-menu__container elementor-nav-menu--layout-horizontal e--pointer-underline e--animation-fade">
                      <ul id="menu-1-5b8c1a4" className="elementor-nav-menu">
                        <li className="menu-item menu-item-type-post_type menu-item-object-page menu-item-home current-menu-item page_item page-item-16 current_page_item menu-item-108">
                          <a href="./" aria-current="page" className="elementor-item elementor-item-active">
                            Home
                          </a>
                        </li>
                      </ul>
                    </nav>
                  </div>
                </div>
              </div>
            </div>
            
            <div 
              className="elementor-column elementor-col-33 elementor-inner-column elementor-element elementor-element-709d9a7c" 
              data-id="709d9a7c" 
              data-element_type="column"
            >
              <div className="elementor-widget-wrap elementor-element-populated">
                {buyButton && (
                  <div 
                    className="elementor-element elementor-element-9a6bb01 elementor-hidden-tablet elementor-hidden-mobile elementor-widget elementor-widget-button" 
                    data-id="9a6bb01" 
                    data-element_type="widget" 
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
                )}
              </div>
            </div>
          </div>
        </section>
      </div>
    </header>
  );
};

export default Header;
