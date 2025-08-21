import React, { useState } from 'react';
import { ChevronDown, ChevronUp } from 'lucide-react';
import { FAQType } from '../../../schemas/validation';

interface FAQSectionProps {
  faq: FAQType[];
}

const FAQSection: React.FC<FAQSectionProps> = ({ faq }) => {
  const [openItems, setOpenItems] = useState<Set<number>>(new Set());

  const toggleItem = (index: number) => {
    const newOpenItems = new Set(openItems);
    if (newOpenItems.has(index)) {
      newOpenItems.delete(index);
    } else {
      newOpenItems.add(index);
    }
    setOpenItems(newOpenItems);
  };

  if (!faq || faq.length === 0) {
    return null;
  }

  return (
    <section 
      className="elementor-section elementor-top-section elementor-element elementor-element-faq elementor-section-full_width elementor-section-height-default" 
      data-id="faq" 
      data-element_type="section"
    >
      <div className="elementor-container elementor-column-gap-default">
        <div 
          className="elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-faq-col" 
          data-id="faq-col" 
          data-element_type="column"
        >
          <div className="elementor-widget-wrap elementor-element-populated">
            
            {/* FAQ Heading */}
            <div 
              className="elementor-element elementor-element-faq-heading elementor-widget elementor-widget-elementskit-heading" 
              data-id="faq-heading" 
              data-element_type="widget" 
              data-widget_type="elementskit-heading.default"
            >
              <div className="elementor-widget-container">
                <div className="ekit-wid-con">
                  <div className="ekit-heading elementskit-section-title-wraper center ekit_heading_tablet- ekit_heading_mobile-">
                    <h2 className="ekit-heading--title elementskit-section-title peacock-heading">
                      Perguntas Frequentes
                    </h2>
                  </div>
                </div>
              </div>
            </div>

            {/* FAQ Accordion */}
            <div 
              className="elementor-element elementor-element-faq-accordion elementor-widget elementor-widget-elementskit-accordion" 
              data-id="faq-accordion" 
              data-element_type="widget" 
              data-widget_type="elementskit-accordion.default"
            >
              <div className="elementor-widget-container">
                <div className="ekit-wid-con">
                  <div className="elementskit-accordion" id="accordion-faq">
                    
                    {faq.map((item, index) => {
                      const isOpen = openItems.has(index);
                      const itemId = `faq-item-${index}`;
                      
                      return (
                        <div 
                          key={index}
                          className="elementskit-card"
                        >
                          <div 
                            className="elementskit-card-header" 
                            id={`heading-${itemId}`}
                          >
                            <button
                              className={`ekit-accordion--toggler elementskit-btn-link ${isOpen ? '' : 'collapsed'}`}
                              type="button"
                              onClick={() => toggleItem(index)}
                              aria-expanded={isOpen}
                              aria-controls={`collapse-${itemId}`}
                            >
                              <span className="ekit-accordion-title peacock-text">
                                {item.question}
                              </span>
                              <div className="ekit-accordion-icon">
                                {isOpen ? (
                                  <ChevronUp className="h-5 w-5" />
                                ) : (
                                  <ChevronDown className="h-5 w-5" />
                                )}
                              </div>
                            </button>
                          </div>

                          <div
                            id={`collapse-${itemId}`}
                            className={`elementskit-card-body ekit-accordion--content ${
                              isOpen ? 'show' : 'collapse'
                            }`}
                            aria-labelledby={`heading-${itemId}`}
                            style={{
                              display: isOpen ? 'block' : 'none',
                              transition: 'all 0.3s ease'
                            }}
                          >
                            <p className="peacock-text">
                              {item.answer}
                            </p>
                          </div>
                        </div>
                      );
                    })}

                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>

      <style jsx>{`
        .elementskit-card {
          border: 1px solid #e5e7eb;
          border-radius: 8px;
          margin-bottom: 1rem;
          overflow: hidden;
          background: white;
          box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }

        .elementskit-card-header {
          background: #f9fafb;
          border-bottom: 1px solid #e5e7eb;
        }

        .ekit-accordion--toggler {
          width: 100%;
          padding: 1.5rem;
          background: none;
          border: none;
          text-align: left;
          cursor: pointer;
          display: flex;
          justify-content: space-between;
          align-items: center;
          font-size: 1rem;
          font-weight: 500;
          color: #374151;
          transition: all 0.3s ease;
        }

        .ekit-accordion--toggler:hover {
          background: #f3f4f6;
          color: var(--peacock-primary);
        }

        .ekit-accordion-title {
          flex: 1;
          margin-right: 1rem;
        }

        .ekit-accordion-icon {
          flex-shrink: 0;
          color: var(--peacock-primary);
        }

        .elementskit-card-body {
          padding: 1.5rem;
          background: white;
        }

        .elementskit-card-body p {
          margin: 0;
          line-height: 1.6;
          color: #6b7280;
        }

        .show {
          animation: slideDown 0.3s ease;
        }

        .collapse {
          animation: slideUp 0.3s ease;
        }

        @keyframes slideDown {
          from {
            opacity: 0;
            max-height: 0;
          }
          to {
            opacity: 1;
            max-height: 200px;
          }
        }

        @keyframes slideUp {
          from {
            opacity: 1;
            max-height: 200px;
          }
          to {
            opacity: 0;
            max-height: 0;
          }
        }
      `}</style>
    </section>
  );
};

export default FAQSection;
