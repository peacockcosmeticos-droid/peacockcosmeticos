import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { authApi, handleApiError } from '../services/api';
import { LoginType } from '../schemas/validation';

interface User {
  username: string;
  role: string;
}

interface AuthContextType {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (credentials: LoginType) => Promise<void>;
  logout: () => void;
  error: string | null;
  clearError: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const isAuthenticated = !!user;

  // Check if user is already logged in on app start
  useEffect(() => {
    const checkAuth = async () => {
      try {
        const token = localStorage.getItem('peacock_admin_token');
        const savedUser = localStorage.getItem('peacock_admin_user');

        if (token && savedUser) {
          // Verify token with server
          const response = await authApi.verify();
          setUser(response.user);
        }
      } catch (error) {
        // Token is invalid, clear storage
        localStorage.removeItem('peacock_admin_token');
        localStorage.removeItem('peacock_admin_user');
        setUser(null);
      } finally {
        setIsLoading(false);
      }
    };

    checkAuth();
  }, []);

  const login = async (credentials: LoginType) => {
    try {
      setIsLoading(true);
      setError(null);

      const response = await authApi.login(credentials);
      
      // Store token and user data
      localStorage.setItem('peacock_admin_token', response.token);
      localStorage.setItem('peacock_admin_user', JSON.stringify(response.user));
      
      setUser(response.user);
    } catch (error) {
      const errorMessage = handleApiError(error);
      setError(errorMessage);
      throw new Error(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  const logout = () => {
    authApi.logout();
    setUser(null);
    setError(null);
  };

  const clearError = () => {
    setError(null);
  };

  const value: AuthContextType = {
    user,
    isAuthenticated,
    isLoading,
    login,
    logout,
    error,
    clearError,
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
