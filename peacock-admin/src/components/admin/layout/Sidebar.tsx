import React from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { 
  Home, 
  Search, 
  Building, 
  ShoppingCart, 
  Type, 
  MessageSquare, 
  HelpCircle, 
  Image, 
  Settings,
  X,
  LogOut
} from 'lucide-react';
import { useAuth } from '../../../contexts/AuthContext';

interface SidebarProps {
  isOpen: boolean;
  onClose: () => void;
}

const Sidebar: React.FC<SidebarProps> = ({ isOpen, onClose }) => {
  const { user, logout } = useAuth();
  const location = useLocation();

  const navigation = [
    { name: 'Visão Geral', href: '/admin/overview', icon: Home },
    { name: 'SEO & Metadata', href: '/admin/metadata', icon: Search },
    { name: 'Empresa', href: '/admin/company', icon: Building },
    { name: 'Botões de Compra', href: '/admin/buy-buttons', icon: ShoppingCart },
    { name: 'Títulos Principais', href: '/admin/headings', icon: Type },
    { name: 'Depoimentos', href: '/admin/testimonials', icon: MessageSquare },
    { name: 'FAQ', href: '/admin/faq', icon: HelpCircle },
    { name: 'Imagens & Mídia', href: '/admin/images', icon: Image },
    { name: 'Configurações', href: '/admin/settings', icon: Settings },
  ];

  const handleLogout = () => {
    logout();
    onClose();
  };

  return (
    <>
      {/* Desktop Sidebar */}
      <div className={`
        hidden lg:flex lg:flex-shrink-0 lg:w-64 lg:flex-col
        ${isOpen ? 'lg:translate-x-0' : 'lg:translate-x-0'}
      `}>
        <div className="flex flex-col flex-grow bg-white border-r border-gray-200 pt-5 pb-4 overflow-y-auto">
          
          {/* Logo */}
          <div className="flex items-center flex-shrink-0 px-4">
            <div className="h-8 w-8 bg-gradient-to-r from-primary-500 to-peacock-500 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-sm">P</span>
            </div>
            <span className="ml-3 text-lg font-semibold text-gray-900">
              Peacock Admin
            </span>
          </div>

          {/* Navigation */}
          <nav className="mt-8 flex-1 px-2 space-y-1">
            {navigation.map((item) => {
              const isActive = location.pathname === item.href;
              return (
                <NavLink
                  key={item.name}
                  to={item.href}
                  className={`nav-link ${isActive ? 'active' : ''}`}
                >
                  <item.icon className="mr-3 h-5 w-5" />
                  {item.name}
                </NavLink>
              );
            })}
          </nav>

          {/* User Info & Logout */}
          <div className="flex-shrink-0 px-4 py-4 border-t border-gray-200">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <div className="h-8 w-8 bg-gray-300 rounded-full flex items-center justify-center">
                  <span className="text-gray-600 font-medium text-sm">
                    {user?.username?.charAt(0).toUpperCase()}
                  </span>
                </div>
              </div>
              <div className="ml-3 flex-1">
                <p className="text-sm font-medium text-gray-900">
                  {user?.username}
                </p>
                <p className="text-xs text-gray-500">
                  {user?.role}
                </p>
              </div>
              <button
                onClick={handleLogout}
                className="ml-2 p-1 text-gray-400 hover:text-gray-600 transition-colors"
                title="Sair"
              >
                <LogOut className="h-4 w-4" />
              </button>
            </div>
          </div>

        </div>
      </div>

      {/* Mobile Sidebar */}
      <div className={`
        lg:hidden fixed inset-y-0 left-0 z-50 w-64 bg-white transform transition-transform duration-300 ease-in-out
        ${isOpen ? 'translate-x-0' : '-translate-x-full'}
      `}>
        <div className="flex flex-col h-full">
          
          {/* Header */}
          <div className="flex items-center justify-between flex-shrink-0 px-4 py-4 border-b border-gray-200">
            <div className="flex items-center">
              <div className="h-8 w-8 bg-gradient-to-r from-primary-500 to-peacock-500 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-sm">P</span>
              </div>
              <span className="ml-3 text-lg font-semibold text-gray-900">
                Peacock Admin
              </span>
            </div>
            <button
              onClick={onClose}
              className="p-1 text-gray-400 hover:text-gray-600 transition-colors"
            >
              <X className="h-6 w-6" />
            </button>
          </div>

          {/* Navigation */}
          <nav className="flex-1 px-2 py-4 space-y-1 overflow-y-auto">
            {navigation.map((item) => {
              const isActive = location.pathname === item.href;
              return (
                <NavLink
                  key={item.name}
                  to={item.href}
                  onClick={onClose}
                  className={`nav-link ${isActive ? 'active' : ''}`}
                >
                  <item.icon className="mr-3 h-5 w-5" />
                  {item.name}
                </NavLink>
              );
            })}
          </nav>

          {/* User Info & Logout */}
          <div className="flex-shrink-0 px-4 py-4 border-t border-gray-200">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <div className="h-8 w-8 bg-gray-300 rounded-full flex items-center justify-center">
                  <span className="text-gray-600 font-medium text-sm">
                    {user?.username?.charAt(0).toUpperCase()}
                  </span>
                </div>
              </div>
              <div className="ml-3 flex-1">
                <p className="text-sm font-medium text-gray-900">
                  {user?.username}
                </p>
                <p className="text-xs text-gray-500">
                  {user?.role}
                </p>
              </div>
              <button
                onClick={handleLogout}
                className="ml-2 p-1 text-gray-400 hover:text-gray-600 transition-colors"
                title="Sair"
              >
                <LogOut className="h-4 w-4" />
              </button>
            </div>
          </div>

        </div>
      </div>
    </>
  );
};

export default Sidebar;
