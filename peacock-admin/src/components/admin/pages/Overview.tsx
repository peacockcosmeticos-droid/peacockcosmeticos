import React from 'react';
import { Link } from 'react-router-dom';
import { 
  Search, 
  Building, 
  ShoppingCart, 
  Type, 
  MessageSquare, 
  HelpCircle, 
  Image,
  TrendingUp,
  Users,
  Eye,
  Clock
} from 'lucide-react';
import { useContent } from '../../../contexts/ContentContext';

const Overview: React.FC = () => {
  const { content, lastUpdated } = useContent();

  const quickStats = [
    {
      name: 'Botões de Compra',
      value: content?.buyButtons?.length || 0,
      icon: ShoppingCart,
      color: 'text-green-600 bg-green-100'
    },
    {
      name: 'Depoimentos',
      value: content?.testimonials?.length || 0,
      icon: Users,
      color: 'text-blue-600 bg-blue-100'
    },
    {
      name: 'Perguntas FAQ',
      value: content?.faq?.length || 0,
      icon: HelpCircle,
      color: 'text-purple-600 bg-purple-100'
    },
    {
      name: 'Imagens',
      value: Object.keys(content?.images || {}).length,
      icon: Image,
      color: 'text-orange-600 bg-orange-100'
    }
  ];

  const quickActions = [
    {
      name: 'SEO & Metadata',
      description: 'Configure título, descrição e palavras-chave',
      href: '/admin/metadata',
      icon: Search,
      color: 'bg-blue-500'
    },
    {
      name: 'Informações da Empresa',
      description: 'Atualize dados da empresa e contato',
      href: '/admin/company',
      icon: Building,
      color: 'bg-green-500'
    },
    {
      name: 'Botões de Compra',
      description: 'Gerencie links de compra em todo o site',
      href: '/admin/buy-buttons',
      icon: ShoppingCart,
      color: 'bg-purple-500'
    },
    {
      name: 'Títulos Principais',
      description: 'Edite os títulos das seções principais',
      href: '/admin/headings',
      icon: Type,
      color: 'bg-indigo-500'
    },
    {
      name: 'Depoimentos',
      description: 'Adicione e edite depoimentos de clientes',
      href: '/admin/testimonials',
      icon: MessageSquare,
      color: 'bg-pink-500'
    },
    {
      name: 'FAQ',
      description: 'Gerencie perguntas frequentes',
      href: '/admin/faq',
      icon: HelpCircle,
      color: 'bg-yellow-500'
    }
  ];

  const formatLastUpdated = (dateString: string | null) => {
    if (!dateString) return 'Nunca atualizado';
    
    const date = new Date(dateString);
    const now = new Date();
    const diffInHours = Math.floor((now.getTime() - date.getTime()) / (1000 * 60 * 60));
    
    if (diffInHours < 1) return 'Atualizado há poucos minutos';
    if (diffInHours < 24) return `Atualizado há ${diffInHours} hora${diffInHours > 1 ? 's' : ''}`;
    
    return date.toLocaleDateString('pt-BR', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="space-y-6">
      
      {/* Page Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">
            Visão Geral
          </h1>
          <p className="text-gray-600">
            Bem-vindo ao painel de administração do Peacock Cosméticos
          </p>
        </div>
        
        <div className="flex items-center space-x-4">
          <button
            onClick={() => window.open('/', '_blank')}
            className="btn btn-outline flex items-center space-x-2"
          >
            <Eye className="h-4 w-4" />
            <span>Ver Site</span>
          </button>
        </div>
      </div>

      {/* Quick Stats */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {quickStats.map((stat) => (
          <div key={stat.name} className="admin-card p-6">
            <div className="flex items-center">
              <div className={`p-3 rounded-lg ${stat.color}`}>
                <stat.icon className="h-6 w-6" />
              </div>
              <div className="ml-4">
                <p className="text-sm font-medium text-gray-600">
                  {stat.name}
                </p>
                <p className="text-2xl font-bold text-gray-900">
                  {stat.value}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Last Updated Info */}
      <div className="admin-card p-6">
        <div className="flex items-center space-x-3">
          <div className="p-2 bg-gray-100 rounded-lg">
            <Clock className="h-5 w-5 text-gray-600" />
          </div>
          <div>
            <h3 className="text-lg font-medium text-gray-900">
              Status do Conteúdo
            </h3>
            <p className="text-gray-600">
              {formatLastUpdated(lastUpdated)}
            </p>
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div>
        <h2 className="text-lg font-medium text-gray-900 mb-4">
          Ações Rápidas
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {quickActions.map((action) => (
            <Link
              key={action.name}
              to={action.href}
              className="admin-card p-6 hover:shadow-lg transition-shadow group"
            >
              <div className="flex items-start space-x-4">
                <div className={`p-3 rounded-lg ${action.color} text-white group-hover:scale-110 transition-transform`}>
                  <action.icon className="h-6 w-6" />
                </div>
                <div className="flex-1">
                  <h3 className="text-lg font-medium text-gray-900 group-hover:text-primary-600 transition-colors">
                    {action.name}
                  </h3>
                  <p className="text-gray-600 text-sm mt-1">
                    {action.description}
                  </p>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>

      {/* Recent Activity */}
      <div className="admin-card p-6">
        <h2 className="text-lg font-medium text-gray-900 mb-4">
          Atividade Recente
        </h2>
        <div className="space-y-3">
          <div className="flex items-center space-x-3 text-sm">
            <div className="w-2 h-2 bg-green-500 rounded-full"></div>
            <span className="text-gray-600">Sistema inicializado com sucesso</span>
            <span className="text-gray-400">•</span>
            <span className="text-gray-400">Agora</span>
          </div>
          <div className="flex items-center space-x-3 text-sm">
            <div className="w-2 h-2 bg-blue-500 rounded-full"></div>
            <span className="text-gray-600">Conteúdo carregado do arquivo de dados</span>
            <span className="text-gray-400">•</span>
            <span className="text-gray-400">Agora</span>
          </div>
          <div className="flex items-center space-x-3 text-sm">
            <div className="w-2 h-2 bg-purple-500 rounded-full"></div>
            <span className="text-gray-600">Painel de administração pronto para uso</span>
            <span className="text-gray-400">•</span>
            <span className="text-gray-400">Agora</span>
          </div>
        </div>
      </div>

    </div>
  );
};

export default Overview;
