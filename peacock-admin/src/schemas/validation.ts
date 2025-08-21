import { z } from 'zod';

// Metadata validation schema
export const MetadataSchema = z.object({
  title: z.string()
    .min(1, 'Title is required')
    .max(60, 'Title must be 60 characters or less'),
  description: z.string()
    .min(1, 'Description is required')
    .max(160, 'Description must be 160 characters or less'),
  keywords: z.string()
    .min(1, 'Keywords are required')
    .max(255, 'Keywords must be 255 characters or less'),
  author: z.string()
    .min(1, 'Author is required')
    .max(100, 'Author must be 100 characters or less'),
  ogTitle: z.string()
    .min(1, 'OG Title is required')
    .max(60, 'OG Title must be 60 characters or less'),
  ogDescription: z.string()
    .min(1, 'OG Description is required')
    .max(160, 'OG Description must be 160 characters or less'),
  twitterSite: z.string().max(50, 'Twitter site must be 50 characters or less').optional(),
  twitterCreator: z.string().max(50, 'Twitter creator must be 50 characters or less').optional(),
});

// Company validation schema
export const CompanySchema = z.object({
  name: z.string()
    .min(1, 'Company name is required')
    .max(100, 'Company name must be 100 characters or less'),
  cnpj: z.string()
    .regex(/^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$/, 'CNPJ must be in format XX.XXX.XXX/XXXX-XX'),
  address: z.string()
    .min(1, 'Address is required')
    .max(255, 'Address must be 255 characters or less'),
  email: z.string()
    .email('Invalid email format')
    .max(100, 'Email must be 100 characters or less'),
  phone: z.string()
    .min(1, 'Phone is required')
    .max(20, 'Phone must be 20 characters or less'),
});

// Social Media validation schema
export const SocialMediaSchema = z.object({
  facebook: z.string().url('Invalid Facebook URL').optional().or(z.literal('')),
  instagram: z.string().url('Invalid Instagram URL').optional().or(z.literal('')),
  tiktok: z.string().url('Invalid TikTok URL').optional().or(z.literal('')),
});

// Buy Button validation schema
export const BuyButtonSchema = z.object({
  id: z.string().min(1, 'ID is required'),
  text: z.string()
    .min(1, 'Button text is required')
    .max(100, 'Button text must be 100 characters or less'),
  url: z.string().url('Invalid URL format'),
  location: z.string()
    .min(1, 'Location is required')
    .max(50, 'Location must be 50 characters or less'),
});

// Main Headings validation schema
export const MainHeadingsSchema = z.object({
  hero: z.string().min(1, 'Hero heading is required'),
  whyChoose: z.string().min(1, 'Why choose heading is required'),
  targetAudience: z.string().min(1, 'Target audience heading is required'),
  howToUse: z.string().min(1, 'How to use heading is required'),
});

// Product Feature validation schema
export const ProductFeatureSchema = z.object({
  title: z.string()
    .min(1, 'Feature title is required')
    .max(200, 'Feature title must be 200 characters or less'),
  description: z.string()
    .max(500, 'Feature description must be 500 characters or less')
    .optional(),
});

// Testimonial validation schema
export const TestimonialSchema = z.object({
  id: z.string().min(1, 'ID is required'),
  name: z.string()
    .min(1, 'Customer name is required')
    .max(50, 'Customer name must be 50 characters or less'),
  quote: z.string()
    .min(1, 'Quote is required')
    .max(200, 'Quote must be 200 characters or less'),
  image: z.string().min(1, 'Image is required'),
});

// Detailed Testimonial validation schema
export const DetailedTestimonialSchema = z.object({
  name: z.string()
    .min(1, 'Customer name is required')
    .max(50, 'Customer name must be 50 characters or less'),
  quote: z.string()
    .min(1, 'Quote is required')
    .max(500, 'Quote must be 500 characters or less'),
});

// Target Audience validation schema
export const TargetAudienceSchema = z.object({
  title: z.string()
    .min(1, 'Title is required')
    .max(100, 'Title must be 100 characters or less'),
  description: z.string()
    .min(1, 'Description is required')
    .max(300, 'Description must be 300 characters or less'),
});

// How To Use validation schema
export const HowToUseSchema = z.object({
  step: z.string()
    .min(1, 'Step is required')
    .max(20, 'Step must be 20 characters or less'),
  instruction: z.string()
    .min(1, 'Instruction is required')
    .max(200, 'Instruction must be 200 characters or less'),
});

// FAQ validation schema
export const FAQSchema = z.object({
  question: z.string()
    .min(1, 'Question is required')
    .max(200, 'Question must be 200 characters or less'),
  answer: z.string()
    .min(1, 'Answer is required')
    .max(500, 'Answer must be 500 characters or less'),
});

// Images validation schema
export const ImagesSchema = z.object({
  logo: z.string().min(1, 'Logo is required'),
  anvisaSeal: z.string().min(1, 'ANVISA seal is required'),
  productVideo: z.string().optional(),
  efficacyProof: z.array(z.string()).optional(),
  beforeAfter: z.array(z.string()).optional(),
  trustBadges: z.array(z.string()).optional(),
});

// Complete content validation schema
export const ContentDataSchema = z.object({
  metadata: MetadataSchema,
  company: CompanySchema,
  socialMedia: SocialMediaSchema,
  buyButtons: z.array(BuyButtonSchema),
  mainHeadings: MainHeadingsSchema,
  productFeatures: z.array(ProductFeatureSchema),
  testimonials: z.array(TestimonialSchema),
  detailedTestimonials: z.array(DetailedTestimonialSchema),
  targetAudience: z.array(TargetAudienceSchema),
  howToUse: z.array(HowToUseSchema),
  faq: z.array(FAQSchema),
  images: ImagesSchema,
});

// Authentication schemas
export const LoginSchema = z.object({
  username: z.string()
    .min(1, 'Username is required')
    .min(3, 'Username must be at least 3 characters'),
  password: z.string()
    .min(1, 'Password is required')
    .min(8, 'Password must be at least 8 characters')
    .regex(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]/, 
           'Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character'),
});

export const ChangePasswordSchema = z.object({
  currentPassword: z.string().min(1, 'Current password is required'),
  newPassword: z.string()
    .min(8, 'New password must be at least 8 characters')
    .regex(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]/, 
           'Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character'),
  confirmPassword: z.string().min(1, 'Please confirm your password'),
}).refine((data) => data.newPassword === data.confirmPassword, {
  message: "Passwords don't match",
  path: ["confirmPassword"],
});

// File upload schema
export const FileUploadSchema = z.object({
  file: z.instanceof(File)
    .refine((file) => file.size <= 5 * 1024 * 1024, 'File size must be less than 5MB')
    .refine((file) => ['image/jpeg', 'image/png', 'image/webp'].includes(file.type), 
             'Only JPEG, PNG, and WebP images are allowed'),
  alt: z.string()
    .min(1, 'Alt text is required')
    .max(100, 'Alt text must be 100 characters or less'),
});

export const VideoUploadSchema = z.object({
  file: z.instanceof(File)
    .refine((file) => file.size <= 50 * 1024 * 1024, 'Video size must be less than 50MB')
    .refine((file) => ['video/mp4', 'video/webm', 'video/ogg'].includes(file.type), 
             'Only MP4, WebM, and OGG videos are allowed'),
});

// Export types
export type MetadataType = z.infer<typeof MetadataSchema>;
export type CompanyType = z.infer<typeof CompanySchema>;
export type SocialMediaType = z.infer<typeof SocialMediaSchema>;
export type BuyButtonType = z.infer<typeof BuyButtonSchema>;
export type MainHeadingsType = z.infer<typeof MainHeadingsSchema>;
export type ProductFeatureType = z.infer<typeof ProductFeatureSchema>;
export type TestimonialType = z.infer<typeof TestimonialSchema>;
export type DetailedTestimonialType = z.infer<typeof DetailedTestimonialSchema>;
export type TargetAudienceType = z.infer<typeof TargetAudienceSchema>;
export type HowToUseType = z.infer<typeof HowToUseSchema>;
export type FAQType = z.infer<typeof FAQSchema>;
export type ImagesType = z.infer<typeof ImagesSchema>;
export type ContentDataType = z.infer<typeof ContentDataSchema>;
export type LoginType = z.infer<typeof LoginSchema>;
export type ChangePasswordType = z.infer<typeof ChangePasswordSchema>;
export type FileUploadType = z.infer<typeof FileUploadSchema>;
export type VideoUploadType = z.infer<typeof VideoUploadSchema>;
