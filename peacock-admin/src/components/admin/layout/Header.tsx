import React from 'react';
import { Menu, ExternalLink, Save, Eye } from 'lucide-react';
import { useContent } from '../../../contexts/ContentContext';

interface HeaderProps {
  onMenuClick: () => void;
}

const Header: React.FC<HeaderProps> = ({ onMenuClick }) => {
  const { lastUpdated, isLoading } = useContent();

  const handleViewSite = () => {
    window.open('/', '_blank');
  };

  const formatLastUpdated = (dateString: string | null) => {
    if (!dateString) return 'Nunca';
    
    const date = new Date(dateString);
    return date.toLocaleString('pt-BR', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="flex items-center justify-between px-4 py-3">
        
        {/* Left Side */}
        <div className="flex items-center">
          <button
            onClick={onMenuClick}
            className="lg:hidden p-2 text-gray-400 hover:text-gray-600 transition-colors"
          >
            <Menu className="h-6 w-6" />
          </button>
          
          <div className="ml-4 lg:ml-0">
            <h1 className="text-xl font-semibold text-gray-900">
              Sistema de Administração
            </h1>
            <p className="text-sm text-gray-500">
              Gerencie o conteúdo do site Peacock Cosméticos
            </p>
          </div>
        </div>

        {/* Right Side */}
        <div className="flex items-center space-x-4">
          
          {/* Last Updated */}
          <div className="hidden md:block text-sm text-gray-500">
            <span className="font-medium">Última atualização:</span>
            <br />
            <span>{formatLastUpdated(lastUpdated)}</span>
          </div>

          {/* Loading Indicator */}
          {isLoading && (
            <div className="flex items-center space-x-2 text-sm text-gray-500">
              <div className="loading-spinner w-4 h-4"></div>
              <span className="hidden sm:inline">Salvando...</span>
            </div>
          )}

          {/* Action Buttons */}
          <div className="flex items-center space-x-2">
            
            {/* View Site Button */}
            <button
              onClick={handleViewSite}
              className="btn btn-outline flex items-center space-x-2"
              title="Ver site"
            >
              <Eye className="h-4 w-4" />
              <span className="hidden sm:inline">Ver Site</span>
            </button>

            {/* Quick Save Button */}
            <button
              className="btn btn-primary flex items-center space-x-2"
              disabled={isLoading}
              title="Salvar alterações"
            >
              <Save className="h-4 w-4" />
              <span className="hidden sm:inline">Salvar</span>
            </button>

          </div>
        </div>

      </div>

      {/* Mobile Last Updated */}
      <div className="md:hidden px-4 pb-3">
        <div className="text-xs text-gray-500">
          <span className="font-medium">Última atualização:</span> {formatLastUpdated(lastUpdated)}
        </div>
      </div>

    </header>
  );
};

export default Header;
