import React, { useState, useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { Save, AlertCircle, CheckCircle } from 'lucide-react';
import { useContent } from '../../../contexts/ContentContext';
import { MetadataSchema, MetadataType } from '../../../schemas/validation';

const MetadataEditor: React.FC = () => {
  const { content, updateSection, isLoading } = useContent();
  const [saveStatus, setSaveStatus] = useState<'idle' | 'saving' | 'success' | 'error'>('idle');

  const {
    register,
    handleSubmit,
    formState: { errors, isDirty },
    reset,
    watch
  } = useForm<MetadataType>({
    resolver: zodResolver(MetadataSchema),
    defaultValues: content?.metadata || {}
  });

  // Reset form when content loads
  useEffect(() => {
    if (content?.metadata) {
      reset(content.metadata);
    }
  }, [content?.metadata, reset]);

  // Watch form values for character counting
  const watchedValues = watch();

  const onSubmit = async (data: MetadataType) => {
    try {
      setSaveStatus('saving');
      await updateSection('metadata', data);
      setSaveStatus('success');
      setTimeout(() => setSaveStatus('idle'), 3000);
    } catch (error) {
      setSaveStatus('error');
      setTimeout(() => setSaveStatus('idle'), 5000);
    }
  };

  const getCharacterCount = (field: keyof MetadataType, maxLength: number) => {
    const value = watchedValues[field] || '';
    const count = value.length;
    const isOverLimit = count > maxLength;
    
    return (
      <span className={`text-xs ${isOverLimit ? 'text-red-500' : 'text-gray-500'}`}>
        {count}/{maxLength}
      </span>
    );
  };

  return (
    <div className="space-y-6">
      
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">
            SEO & Metadata
          </h1>
          <p className="text-gray-600">
            Configure título, descrição e palavras-chave para otimização de busca
          </p>
        </div>
        
        {/* Save Status */}
        {saveStatus !== 'idle' && (
          <div className="flex items-center space-x-2">
            {saveStatus === 'saving' && (
              <>
                <div className="loading-spinner w-4 h-4"></div>
                <span className="text-sm text-gray-600">Salvando...</span>
              </>
            )}
            {saveStatus === 'success' && (
              <>
                <CheckCircle className="h-4 w-4 text-green-600" />
                <span className="text-sm text-green-600">Salvo com sucesso!</span>
              </>
            )}
            {saveStatus === 'error' && (
              <>
                <AlertCircle className="h-4 w-4 text-red-600" />
                <span className="text-sm text-red-600">Erro ao salvar</span>
              </>
            )}
          </div>
        )}
      </div>

      {/* Form */}
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        
        <div className="admin-card p-6">
          <h2 className="text-lg font-medium text-gray-900 mb-4">
            Informações Básicas
          </h2>
          
          <div className="space-y-4">
            
            {/* Page Title */}
            <div className="form-group">
              <div className="flex justify-between items-center mb-2">
                <label htmlFor="title" className="form-label">
                  Título da Página *
                </label>
                {getCharacterCount('title', 60)}
              </div>
              <input
                {...register('title')}
                type="text"
                id="title"
                className={`form-input ${errors.title ? 'border-red-500' : ''}`}
                placeholder="Peecock - Sérum vegano para crescimento de cílios"
              />
              {errors.title && (
                <p className="form-error">{errors.title.message}</p>
              )}
              <p className="text-xs text-gray-500 mt-1">
                Aparece na aba do navegador e nos resultados de busca
              </p>
            </div>

            {/* Meta Description */}
            <div className="form-group">
              <div className="flex justify-between items-center mb-2">
                <label htmlFor="description" className="form-label">
                  Descrição Meta *
                </label>
                {getCharacterCount('description', 160)}
              </div>
              <textarea
                {...register('description')}
                id="description"
                rows={3}
                className={`form-input ${errors.description ? 'border-red-500' : ''}`}
                placeholder="Transforme seus cílios em apenas 7 dias com o sérum Peecock..."
              />
              {errors.description && (
                <p className="form-error">{errors.description.message}</p>
              )}
              <p className="text-xs text-gray-500 mt-1">
                Aparece nos resultados de busca abaixo do título
              </p>
            </div>

            {/* Keywords */}
            <div className="form-group">
              <div className="flex justify-between items-center mb-2">
                <label htmlFor="keywords" className="form-label">
                  Palavras-chave *
                </label>
                {getCharacterCount('keywords', 255)}
              </div>
              <textarea
                {...register('keywords')}
                id="keywords"
                rows={2}
                className={`form-input ${errors.keywords ? 'border-red-500' : ''}`}
                placeholder="sérum para cílios, crescimento de cílios, cílios longos..."
              />
              {errors.keywords && (
                <p className="form-error">{errors.keywords.message}</p>
              )}
              <p className="text-xs text-gray-500 mt-1">
                Separe as palavras-chave com vírgulas
              </p>
            </div>

            {/* Author */}
            <div className="form-group">
              <label htmlFor="author" className="form-label">
                Autor *
              </label>
              <input
                {...register('author')}
                type="text"
                id="author"
                className={`form-input ${errors.author ? 'border-red-500' : ''}`}
                placeholder="Peecock Cosméticos"
              />
              {errors.author && (
                <p className="form-error">{errors.author.message}</p>
              )}
            </div>

          </div>
        </div>

        <div className="admin-card p-6">
          <h2 className="text-lg font-medium text-gray-900 mb-4">
            Open Graph (Redes Sociais)
          </h2>
          
          <div className="space-y-4">
            
            {/* OG Title */}
            <div className="form-group">
              <div className="flex justify-between items-center mb-2">
                <label htmlFor="ogTitle" className="form-label">
                  Título para Redes Sociais *
                </label>
                {getCharacterCount('ogTitle', 60)}
              </div>
              <input
                {...register('ogTitle')}
                type="text"
                id="ogTitle"
                className={`form-input ${errors.ogTitle ? 'border-red-500' : ''}`}
                placeholder="Peecock - Sérum vegano para crescimento de cílios"
              />
              {errors.ogTitle && (
                <p className="form-error">{errors.ogTitle.message}</p>
              )}
            </div>

            {/* OG Description */}
            <div className="form-group">
              <div className="flex justify-between items-center mb-2">
                <label htmlFor="ogDescription" className="form-label">
                  Descrição para Redes Sociais *
                </label>
                {getCharacterCount('ogDescription', 160)}
              </div>
              <textarea
                {...register('ogDescription')}
                id="ogDescription"
                rows={3}
                className={`form-input ${errors.ogDescription ? 'border-red-500' : ''}`}
                placeholder="Transforme seus cílios em apenas 7 dias..."
              />
              {errors.ogDescription && (
                <p className="form-error">{errors.ogDescription.message}</p>
              )}
            </div>

            {/* Twitter Site */}
            <div className="form-group">
              <label htmlFor="twitterSite" className="form-label">
                Twitter Site
              </label>
              <input
                {...register('twitterSite')}
                type="text"
                id="twitterSite"
                className={`form-input ${errors.twitterSite ? 'border-red-500' : ''}`}
                placeholder="@peecockbr"
              />
              {errors.twitterSite && (
                <p className="form-error">{errors.twitterSite.message}</p>
              )}
            </div>

            {/* Twitter Creator */}
            <div className="form-group">
              <label htmlFor="twitterCreator" className="form-label">
                Twitter Creator
              </label>
              <input
                {...register('twitterCreator')}
                type="text"
                id="twitterCreator"
                className={`form-input ${errors.twitterCreator ? 'border-red-500' : ''}`}
                placeholder="@peecockbr"
              />
              {errors.twitterCreator && (
                <p className="form-error">{errors.twitterCreator.message}</p>
              )}
            </div>

          </div>
        </div>

        {/* Save Button */}
        <div className="flex justify-end">
          <button
            type="submit"
            disabled={!isDirty || isLoading}
            className="btn btn-primary flex items-center space-x-2"
          >
            <Save className="h-4 w-4" />
            <span>Salvar Alterações</span>
          </button>
        </div>

      </form>

    </div>
  );
};

export default MetadataEditor;
