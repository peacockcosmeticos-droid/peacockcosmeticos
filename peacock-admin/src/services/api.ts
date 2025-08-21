import axios, { AxiosResponse } from 'axios';
import { ContentDataType, LoginType } from '../schemas/validation';

// API Configuration
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:3001/api';

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('peacock_admin_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle auth errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('peacock_admin_token');
      localStorage.removeItem('peacock_admin_user');
      window.location.href = '/admin/login';
    }
    return Promise.reject(error);
  }
);

// Types
export interface ApiResponse<T = any> {
  data: T;
  message?: string;
}

export interface LoginResponse {
  token: string;
  user: {
    username: string;
    role: string;
  };
  expiresIn: string;
}

export interface UploadResponse {
  message: string;
  filename: string;
  originalName: string;
  url: string;
  size: number;
  mimetype: string;
}

// Authentication API
export const authApi = {
  login: async (credentials: LoginType): Promise<LoginResponse> => {
    const response: AxiosResponse<LoginResponse> = await api.post('/auth/login', credentials);
    return response.data;
  },

  verify: async (): Promise<{ user: any }> => {
    const response: AxiosResponse<{ user: any }> = await api.get('/auth/verify');
    return response.data;
  },

  logout: () => {
    localStorage.removeItem('peacock_admin_token');
    localStorage.removeItem('peacock_admin_user');
  },
};

// Content API
export const contentApi = {
  // Get all content
  getAll: async (): Promise<ContentDataType> => {
    const response: AxiosResponse<ContentDataType> = await api.get('/content');
    return response.data;
  },

  // Get specific section
  getSection: async (section: string): Promise<any> => {
    const response: AxiosResponse<any> = await api.get(`/content/${section}`);
    return response.data;
  },

  // Update specific section
  updateSection: async (section: string, data: any): Promise<ApiResponse> => {
    const response: AxiosResponse<ApiResponse> = await api.put(`/content/${section}`, data);
    return response.data;
  },

  // Update all content
  updateAll: async (content: ContentDataType): Promise<ApiResponse<ContentDataType>> => {
    const response: AxiosResponse<ApiResponse<ContentDataType>> = await api.put('/content', content);
    return response.data;
  },

  // Metadata operations
  getMetadata: async () => contentApi.getSection('metadata'),
  updateMetadata: async (data: any) => contentApi.updateSection('metadata', data),

  // Company operations
  getCompany: async () => contentApi.getSection('company'),
  updateCompany: async (data: any) => contentApi.updateSection('company', data),

  // Social Media operations
  getSocialMedia: async () => contentApi.getSection('socialMedia'),
  updateSocialMedia: async (data: any) => contentApi.updateSection('socialMedia', data),

  // Buy Buttons operations
  getBuyButtons: async () => contentApi.getSection('buyButtons'),
  updateBuyButtons: async (data: any) => contentApi.updateSection('buyButtons', data),

  // Main Headings operations
  getMainHeadings: async () => contentApi.getSection('mainHeadings'),
  updateMainHeadings: async (data: any) => contentApi.updateSection('mainHeadings', data),

  // Product Features operations
  getProductFeatures: async () => contentApi.getSection('productFeatures'),
  updateProductFeatures: async (data: any) => contentApi.updateSection('productFeatures', data),

  // Testimonials operations
  getTestimonials: async () => contentApi.getSection('testimonials'),
  updateTestimonials: async (data: any) => contentApi.updateSection('testimonials', data),

  // Detailed Testimonials operations
  getDetailedTestimonials: async () => contentApi.getSection('detailedTestimonials'),
  updateDetailedTestimonials: async (data: any) => contentApi.updateSection('detailedTestimonials', data),

  // Target Audience operations
  getTargetAudience: async () => contentApi.getSection('targetAudience'),
  updateTargetAudience: async (data: any) => contentApi.updateSection('targetAudience', data),

  // How To Use operations
  getHowToUse: async () => contentApi.getSection('howToUse'),
  updateHowToUse: async (data: any) => contentApi.updateSection('howToUse', data),

  // FAQ operations
  getFAQ: async () => contentApi.getSection('faq'),
  updateFAQ: async (data: any) => contentApi.updateSection('faq', data),

  // Images operations
  getImages: async () => contentApi.getSection('images'),
  updateImages: async (data: any) => contentApi.updateSection('images', data),
};

// File Upload API
export const uploadApi = {
  uploadFile: async (file: File): Promise<UploadResponse> => {
    const formData = new FormData();
    formData.append('file', file);

    const response: AxiosResponse<UploadResponse> = await api.post('/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });

    return response.data;
  },

  uploadImage: async (file: File): Promise<UploadResponse> => {
    // Validate image file
    const allowedTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];
    if (!allowedTypes.includes(file.type)) {
      throw new Error('Only JPEG, PNG, and WebP images are allowed');
    }

    if (file.size > 5 * 1024 * 1024) { // 5MB
      throw new Error('Image size must be less than 5MB');
    }

    return uploadApi.uploadFile(file);
  },

  uploadVideo: async (file: File): Promise<UploadResponse> => {
    // Validate video file
    const allowedTypes = ['video/mp4', 'video/webm', 'video/ogg'];
    if (!allowedTypes.includes(file.type)) {
      throw new Error('Only MP4, WebM, and OGG videos are allowed');
    }

    if (file.size > 50 * 1024 * 1024) { // 50MB
      throw new Error('Video size must be less than 50MB');
    }

    return uploadApi.uploadFile(file);
  },
};

// Health Check API
export const healthApi = {
  check: async (): Promise<{ status: string; timestamp: string }> => {
    const response: AxiosResponse<{ status: string; timestamp: string }> = await api.get('/health');
    return response.data;
  },
};

// Error handling utility
export const handleApiError = (error: any): string => {
  if (error.response?.data?.error) {
    return error.response.data.error;
  }
  if (error.message) {
    return error.message;
  }
  return 'An unexpected error occurred';
};

// Export default api instance for custom requests
export default api;
