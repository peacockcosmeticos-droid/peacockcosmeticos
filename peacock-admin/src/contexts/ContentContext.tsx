import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { contentApi, handleApiError } from '../services/api';
import { ContentDataType } from '../schemas/validation';

interface ContentContextType {
  content: ContentDataType | null;
  isLoading: boolean;
  error: string | null;
  lastUpdated: string | null;
  
  // Content operations
  loadContent: () => Promise<void>;
  updateSection: (section: string, data: any) => Promise<void>;
  updateAllContent: (content: ContentDataType) => Promise<void>;
  
  // Section-specific operations
  getSection: (section: string) => any;
  
  // Error handling
  clearError: () => void;
  
  // Validation
  validateSection: (section: string, data: any) => { isValid: boolean; errors: string[] };
}

const ContentContext = createContext<ContentContextType | undefined>(undefined);

interface ContentProviderProps {
  children: ReactNode;
}

export const ContentProvider: React.FC<ContentProviderProps> = ({ children }) => {
  const [content, setContent] = useState<ContentDataType | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [lastUpdated, setLastUpdated] = useState<string | null>(null);

  // Load content on mount
  useEffect(() => {
    loadContent();
  }, []);

  const loadContent = async () => {
    try {
      setIsLoading(true);
      setError(null);
      
      const data = await contentApi.getAll();
      setContent(data);
      setLastUpdated(data.lastUpdated || new Date().toISOString());
    } catch (error) {
      const errorMessage = handleApiError(error);
      setError(errorMessage);
      console.error('Failed to load content:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const updateSection = async (section: string, data: any) => {
    try {
      setIsLoading(true);
      setError(null);

      // Validate the section data
      const validation = validateSection(section, data);
      if (!validation.isValid) {
        throw new Error(`Validation failed: ${validation.errors.join(', ')}`);
      }

      // Update on server
      await contentApi.updateSection(section, data);
      
      // Update local state
      if (content) {
        const updatedContent = {
          ...content,
          [section]: data,
          lastUpdated: new Date().toISOString(),
        };
        setContent(updatedContent);
        setLastUpdated(updatedContent.lastUpdated);
      }
    } catch (error) {
      const errorMessage = handleApiError(error);
      setError(errorMessage);
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  const updateAllContent = async (newContent: ContentDataType) => {
    try {
      setIsLoading(true);
      setError(null);

      // Update on server
      await contentApi.updateAll(newContent);
      
      // Update local state
      const updatedContent = {
        ...newContent,
        lastUpdated: new Date().toISOString(),
      };
      setContent(updatedContent);
      setLastUpdated(updatedContent.lastUpdated);
    } catch (error) {
      const errorMessage = handleApiError(error);
      setError(errorMessage);
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  const getSection = (section: string) => {
    return content ? content[section as keyof ContentDataType] : null;
  };

  const clearError = () => {
    setError(null);
  };

  const validateSection = (section: string, data: any): { isValid: boolean; errors: string[] } => {
    const errors: string[] = [];

    try {
      switch (section) {
        case 'metadata':
          if (!data.title || data.title.length > 60) {
            errors.push('Title is required and must be 60 characters or less');
          }
          if (!data.description || data.description.length > 160) {
            errors.push('Description is required and must be 160 characters or less');
          }
          if (!data.keywords || data.keywords.length > 255) {
            errors.push('Keywords are required and must be 255 characters or less');
          }
          break;

        case 'company':
          if (!data.name || data.name.length > 100) {
            errors.push('Company name is required and must be 100 characters or less');
          }
          if (!data.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) {
            errors.push('Valid email is required');
          }
          if (!data.cnpj || !/^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$/.test(data.cnpj)) {
            errors.push('Valid CNPJ format is required (XX.XXX.XXX/XXXX-XX)');
          }
          break;

        case 'socialMedia':
          if (data.facebook && !/^https?:\/\/.+/.test(data.facebook)) {
            errors.push('Facebook URL must be a valid URL');
          }
          if (data.instagram && !/^https?:\/\/.+/.test(data.instagram)) {
            errors.push('Instagram URL must be a valid URL');
          }
          if (data.tiktok && !/^https?:\/\/.+/.test(data.tiktok)) {
            errors.push('TikTok URL must be a valid URL');
          }
          break;

        case 'buyButtons':
          if (!Array.isArray(data)) {
            errors.push('Buy buttons must be an array');
            break;
          }
          data.forEach((button: any, index: number) => {
            if (!button.id) {
              errors.push(`Button ${index + 1}: ID is required`);
            }
            if (!button.text || button.text.length > 100) {
              errors.push(`Button ${index + 1}: Text is required and must be 100 characters or less`);
            }
            if (!button.url || !/^https?:\/\/.+/.test(button.url)) {
              errors.push(`Button ${index + 1}: Valid URL is required`);
            }
          });
          break;

        case 'testimonials':
          if (!Array.isArray(data)) {
            errors.push('Testimonials must be an array');
            break;
          }
          data.forEach((testimonial: any, index: number) => {
            if (!testimonial.name || testimonial.name.length > 50) {
              errors.push(`Testimonial ${index + 1}: Name is required and must be 50 characters or less`);
            }
            if (!testimonial.quote || testimonial.quote.length > 200) {
              errors.push(`Testimonial ${index + 1}: Quote is required and must be 200 characters or less`);
            }
            if (!testimonial.image) {
              errors.push(`Testimonial ${index + 1}: Image is required`);
            }
          });
          break;

        case 'faq':
          if (!Array.isArray(data)) {
            errors.push('FAQ must be an array');
            break;
          }
          data.forEach((faq: any, index: number) => {
            if (!faq.question || faq.question.length > 200) {
              errors.push(`FAQ ${index + 1}: Question is required and must be 200 characters or less`);
            }
            if (!faq.answer || faq.answer.length > 500) {
              errors.push(`FAQ ${index + 1}: Answer is required and must be 500 characters or less`);
            }
          });
          break;

        default:
          // For other sections, perform basic validation
          if (data === null || data === undefined) {
            errors.push('Data cannot be null or undefined');
          }
          break;
      }
    } catch (error) {
      errors.push('Validation error occurred');
    }

    return {
      isValid: errors.length === 0,
      errors,
    };
  };

  const value: ContentContextType = {
    content,
    isLoading,
    error,
    lastUpdated,
    loadContent,
    updateSection,
    updateAllContent,
    getSection,
    clearError,
    validateSection,
  };

  return (
    <ContentContext.Provider value={value}>
      {children}
    </ContentContext.Provider>
  );
};

export const useContent = (): ContentContextType => {
  const context = useContext(ContentContext);
  if (context === undefined) {
    throw new Error('useContent must be used within a ContentProvider');
  }
  return context;
};
