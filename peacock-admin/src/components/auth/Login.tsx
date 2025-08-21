import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { Eye, EyeOff, Lock, User, AlertCircle } from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';
import { LoginSchema, LoginType } from '../../schemas/validation';

const Login: React.FC = () => {
  const [showPassword, setShowPassword] = useState(false);
  const { login, isAuthenticated, isLoading, error, clearError } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const from = (location.state as any)?.from?.pathname || '/admin';

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    setError: setFormError,
  } = useForm<LoginType>({
    resolver: zodResolver(LoginSchema),
    defaultValues: {
      username: '',
      password: '',
    },
  });

  // Redirect if already authenticated
  useEffect(() => {
    if (isAuthenticated) {
      navigate(from, { replace: true });
    }
  }, [isAuthenticated, navigate, from]);

  // Clear errors when component mounts
  useEffect(() => {
    clearError();
  }, [clearError]);

  const onSubmit = async (data: LoginType) => {
    try {
      clearError();
      await login(data);
      navigate(from, { replace: true });
    } catch (error) {
      // Error is handled by AuthContext
      setFormError('root', {
        type: 'manual',
        message: 'Login failed. Please check your credentials.',
      });
    }
  };

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-peacock-50 to-primary-50">
        <div className="flex items-center space-x-2">
          <div className="loading-spinner"></div>
          <span className="text-gray-600">Verificando autenticação...</span>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-peacock-50 to-primary-50 px-4">
      <div className="max-w-md w-full space-y-8">
        {/* Header */}
        <div className="text-center">
          <div className="mx-auto h-16 w-16 bg-gradient-to-r from-primary-500 to-peacock-500 rounded-full flex items-center justify-center">
            <Lock className="h-8 w-8 text-white" />
          </div>
          <h2 className="mt-6 text-3xl font-bold text-gray-900">
            Peacock Admin
          </h2>
          <p className="mt-2 text-sm text-gray-600">
            Sistema de Administração
          </p>
        </div>

        {/* Login Form */}
        <div className="admin-card p-8">
          <form className="space-y-6" onSubmit={handleSubmit(onSubmit)}>
            {/* Error Alert */}
            {(error || errors.root) && (
              <div className="alert alert-error">
                <AlertCircle className="h-5 w-5" />
                <span>{error || errors.root?.message}</span>
              </div>
            )}

            {/* Username Field */}
            <div className="form-group">
              <label htmlFor="username" className="form-label">
                Usuário
              </label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <User className="h-5 w-5 text-gray-400" />
                </div>
                <input
                  {...register('username')}
                  type="text"
                  id="username"
                  className={`form-input pl-10 ${errors.username ? 'border-red-500' : ''}`}
                  placeholder="Digite seu usuário"
                  autoComplete="username"
                />
              </div>
              {errors.username && (
                <p className="form-error">{errors.username.message}</p>
              )}
            </div>

            {/* Password Field */}
            <div className="form-group">
              <label htmlFor="password" className="form-label">
                Senha
              </label>
              <div className="relative">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <Lock className="h-5 w-5 text-gray-400" />
                </div>
                <input
                  {...register('password')}
                  type={showPassword ? 'text' : 'password'}
                  id="password"
                  className={`form-input pl-10 pr-10 ${errors.password ? 'border-red-500' : ''}`}
                  placeholder="Digite sua senha"
                  autoComplete="current-password"
                />
                <button
                  type="button"
                  className="absolute inset-y-0 right-0 pr-3 flex items-center"
                  onClick={togglePasswordVisibility}
                >
                  {showPassword ? (
                    <EyeOff className="h-5 w-5 text-gray-400 hover:text-gray-600" />
                  ) : (
                    <Eye className="h-5 w-5 text-gray-400 hover:text-gray-600" />
                  )}
                </button>
              </div>
              {errors.password && (
                <p className="form-error">{errors.password.message}</p>
              )}
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full btn btn-primary flex items-center justify-center space-x-2"
            >
              {isSubmitting ? (
                <>
                  <div className="loading-spinner"></div>
                  <span>Entrando...</span>
                </>
              ) : (
                <span>Entrar</span>
              )}
            </button>
          </form>

          {/* Footer */}
          <div className="mt-6 text-center">
            <p className="text-xs text-gray-500">
              Sistema seguro protegido por autenticação JWT
            </p>
          </div>
        </div>

        {/* Demo Credentials */}
        <div className="text-center">
          <div className="inline-block bg-yellow-50 border border-yellow-200 rounded-lg p-4 text-sm">
            <p className="font-medium text-yellow-800 mb-2">Credenciais de Demonstração:</p>
            <p className="text-yellow-700">
              <strong>Usuário:</strong> admin<br />
              <strong>Senha:</strong> PeacockAdmin2025!
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
