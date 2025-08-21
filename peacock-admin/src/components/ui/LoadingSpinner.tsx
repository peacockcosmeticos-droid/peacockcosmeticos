import React from 'react';

interface LoadingSpinnerProps {
  message?: string;
  size?: 'sm' | 'md' | 'lg';
  className?: string;
}

const LoadingSpinner: React.FC<LoadingSpinnerProps> = ({ 
  message = 'Carregando...', 
  size = 'md',
  className = ''
}) => {
  const sizeClasses = {
    sm: 'w-4 h-4',
    md: 'w-8 h-8',
    lg: 'w-12 h-12'
  };

  return (
    <div className={`flex flex-col items-center justify-center min-h-[200px] ${className}`}>
      <div className={`loading-spinner ${sizeClasses[size]} mb-4`}></div>
      {message && (
        <p className="text-gray-600 text-center">{message}</p>
      )}
    </div>
  );
};

export default LoadingSpinner;
