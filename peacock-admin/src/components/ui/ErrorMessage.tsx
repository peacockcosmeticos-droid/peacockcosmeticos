import React from 'react';
import { AlertCircle, RefreshCw } from 'lucide-react';

interface ErrorMessageProps {
  message: string;
  title?: string;
  onRetry?: () => void;
  className?: string;
}

const ErrorMessage: React.FC<ErrorMessageProps> = ({ 
  message, 
  title = 'Erro',
  onRetry,
  className = ''
}) => {
  return (
    <div className={`flex flex-col items-center justify-center min-h-[200px] p-8 ${className}`}>
      <div className="text-center max-w-md">
        <div className="mx-auto h-16 w-16 bg-red-100 rounded-full flex items-center justify-center mb-4">
          <AlertCircle className="h-8 w-8 text-red-600" />
        </div>
        
        <h3 className="text-lg font-semibold text-gray-900 mb-2">
          {title}
        </h3>
        
        <p className="text-gray-600 mb-6">
          {message}
        </p>
        
        {onRetry && (
          <button
            onClick={onRetry}
            className="btn btn-primary flex items-center space-x-2"
          >
            <RefreshCw className="h-4 w-4" />
            <span>Tentar novamente</span>
          </button>
        )}
      </div>
    </div>
  );
};

export default ErrorMessage;
