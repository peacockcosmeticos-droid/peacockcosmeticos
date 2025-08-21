import React from 'react';
import { Building } from 'lucide-react';

const CompanyEditor: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Informações da Empresa</h1>
          <p className="text-gray-600">Gerencie dados da empresa e informações de contato</p>
        </div>
      </div>
      
      <div className="admin-card p-6">
        <div className="flex items-center justify-center h-64">
          <div className="text-center">
            <Building className="h-12 w-12 text-gray-400 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-900 mb-2">Editor de Empresa</h3>
            <p className="text-gray-600">Esta funcionalidade será implementada em breve.</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CompanyEditor;
