// TypeScript interfaces for content management

export interface Metadata {
  title: string;
  description: string;
  keywords: string;
  author: string;
  ogTitle: string;
  ogDescription: string;
  twitterSite: string;
  twitterCreator: string;
}

export interface Company {
  name: string;
  cnpj: string;
  address: string;
  email: string;
  phone: string;
}

export interface SocialMedia {
  facebook: string;
  instagram: string;
  tiktok: string;
}

export interface BuyButton {
  id: string;
  text: string;
  url: string;
  location: string;
}

export interface MainHeadings {
  hero: string;
  whyChoose: string;
  targetAudience: string;
  howToUse: string;
}

export interface ProductFeature {
  title: string;
  description: string;
}

export interface Testimonial {
  id: string;
  name: string;
  quote: string;
  image: string;
}

export interface DetailedTestimonial {
  name: string;
  quote: string;
}

export interface TargetAudienceItem {
  title: string;
  description: string;
}

export interface HowToUseStep {
  step: string;
  instruction: string;
}

export interface FAQ {
  question: string;
  answer: string;
}

export interface Images {
  logo: string;
  anvisaSeal: string;
  productVideo: string;
  efficacyProof: string[];
  beforeAfter: string[];
  trustBadges: string[];
}

export interface ContentData {
  metadata: Metadata;
  company: Company;
  socialMedia: SocialMedia;
  buyButtons: BuyButton[];
  mainHeadings: MainHeadings;
  productFeatures: ProductFeature[];
  testimonials: Testimonial[];
  detailedTestimonials: DetailedTestimonial[];
  targetAudience: TargetAudienceItem[];
  howToUse: HowToUseStep[];
  faq: FAQ[];
  images: Images;
}

// Validation schemas using Zod
export const MetadataSchema = {
  title: { type: 'string', required: true, maxLength: 60 },
  description: { type: 'string', required: true, maxLength: 160 },
  keywords: { type: 'string', required: true, maxLength: 255 },
  author: { type: 'string', required: true, maxLength: 100 },
  ogTitle: { type: 'string', required: true, maxLength: 60 },
  ogDescription: { type: 'string', required: true, maxLength: 160 },
  twitterSite: { type: 'string', required: false, maxLength: 50 },
  twitterCreator: { type: 'string', required: false, maxLength: 50 }
};

export const CompanySchema = {
  name: { type: 'string', required: true, maxLength: 100 },
  cnpj: { type: 'string', required: true, pattern: /^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$/ },
  address: { type: 'string', required: true, maxLength: 255 },
  email: { type: 'email', required: true, maxLength: 100 },
  phone: { type: 'string', required: true, maxLength: 20 }
};

export const SocialMediaSchema = {
  facebook: { type: 'url', required: false },
  instagram: { type: 'url', required: false },
  tiktok: { type: 'url', required: false }
};

export const BuyButtonSchema = {
  id: { type: 'string', required: true },
  text: { type: 'string', required: true, maxLength: 100 },
  url: { type: 'url', required: true },
  location: { type: 'string', required: true, maxLength: 50 }
};

export const TestimonialSchema = {
  id: { type: 'string', required: true },
  name: { type: 'string', required: true, maxLength: 50 },
  quote: { type: 'string', required: true, maxLength: 200 },
  image: { type: 'string', required: true }
};

export const FAQSchema = {
  question: { type: 'string', required: true, maxLength: 200 },
  answer: { type: 'string', required: true, maxLength: 500 }
};

// Content field types for admin interface
export type ContentFieldType = 
  | 'text' 
  | 'textarea' 
  | 'rich-text' 
  | 'url' 
  | 'email' 
  | 'image' 
  | 'video' 
  | 'select' 
  | 'checkbox' 
  | 'number';

export interface ContentField {
  key: string;
  label: string;
  type: ContentFieldType;
  required: boolean;
  maxLength?: number;
  pattern?: RegExp;
  options?: string[];
  placeholder?: string;
  helpText?: string;
}

// Admin interface configuration
export interface AdminSection {
  id: string;
  title: string;
  description: string;
  fields: ContentField[];
  icon?: string;
}

export const ADMIN_SECTIONS: AdminSection[] = [
  {
    id: 'metadata',
    title: 'SEO & Metadata',
    description: 'Configure page title, description, and SEO settings',
    icon: 'Search',
    fields: [
      { key: 'title', label: 'Page Title', type: 'text', required: true, maxLength: 60, placeholder: 'Peecock - Sérum vegano para crescimento de cílios' },
      { key: 'description', label: 'Meta Description', type: 'textarea', required: true, maxLength: 160, placeholder: 'Transforme seus cílios em apenas 7 dias...' },
      { key: 'keywords', label: 'Keywords', type: 'textarea', required: true, maxLength: 255, helpText: 'Separate keywords with commas' },
      { key: 'author', label: 'Author', type: 'text', required: true, maxLength: 100 },
    ]
  },
  {
    id: 'company',
    title: 'Company Information',
    description: 'Update company details and contact information',
    icon: 'Building',
    fields: [
      { key: 'name', label: 'Company Name', type: 'text', required: true, maxLength: 100 },
      { key: 'cnpj', label: 'CNPJ', type: 'text', required: true, pattern: /^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$/ },
      { key: 'address', label: 'Address', type: 'textarea', required: true, maxLength: 255 },
      { key: 'email', label: 'Email', type: 'email', required: true, maxLength: 100 },
      { key: 'phone', label: 'Phone', type: 'text', required: true, maxLength: 20 },
    ]
  },
  {
    id: 'buyButtons',
    title: 'Buy Buttons',
    description: 'Manage all purchase button links throughout the site',
    icon: 'ShoppingCart',
    fields: [
      { key: 'text', label: 'Button Text', type: 'text', required: true, maxLength: 100 },
      { key: 'url', label: 'Purchase URL', type: 'url', required: true },
      { key: 'location', label: 'Location', type: 'text', required: true, maxLength: 50 },
    ]
  },
  {
    id: 'headings',
    title: 'Main Headings',
    description: 'Edit the main section headings on the homepage',
    icon: 'Type',
    fields: [
      { key: 'hero', label: 'Hero Heading', type: 'rich-text', required: true },
      { key: 'whyChoose', label: 'Why Choose Heading', type: 'rich-text', required: true },
      { key: 'targetAudience', label: 'Target Audience Heading', type: 'rich-text', required: true },
      { key: 'howToUse', label: 'How To Use Heading', type: 'rich-text', required: true },
    ]
  },
  {
    id: 'testimonials',
    title: 'Customer Testimonials',
    description: 'Manage customer reviews and testimonials',
    icon: 'MessageSquare',
    fields: [
      { key: 'name', label: 'Customer Name', type: 'text', required: true, maxLength: 50 },
      { key: 'quote', label: 'Testimonial Quote', type: 'textarea', required: true, maxLength: 200 },
      { key: 'image', label: 'Customer Image', type: 'image', required: true },
    ]
  },
  {
    id: 'faq',
    title: 'FAQ Section',
    description: 'Manage frequently asked questions',
    icon: 'HelpCircle',
    fields: [
      { key: 'question', label: 'Question', type: 'text', required: true, maxLength: 200 },
      { key: 'answer', label: 'Answer', type: 'textarea', required: true, maxLength: 500 },
    ]
  },
  {
    id: 'images',
    title: 'Images & Media',
    description: 'Upload and manage website images',
    icon: 'Image',
    fields: [
      { key: 'logo', label: 'Company Logo', type: 'image', required: true },
      { key: 'anvisaSeal', label: 'ANVISA Seal', type: 'image', required: true },
      { key: 'productVideo', label: 'Product Video', type: 'video', required: false },
    ]
  }
];
