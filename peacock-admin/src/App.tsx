import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { AuthProvider } from './contexts/AuthContext'
import { ContentProvider } from './contexts/ContentContext'
import Login from './components/auth/Login'
import Dashboard from './components/admin/Dashboard'
import ProtectedRoute from './components/auth/ProtectedRoute'
import Homepage from './components/frontend/Homepage'
import './App.css'

function App() {
  return (
    <AuthProvider>
      <ContentProvider>
        <Router future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
          <div className="App">
            <Routes>
              {/* Frontend Routes */}
              <Route path="/" element={<Homepage />} />
              
              {/* Admin Routes */}
              <Route path="/admin/login" element={<Login />} />
              <Route 
                path="/admin/*" 
                element={
                  <ProtectedRoute>
                    <Dashboard />
                  </ProtectedRoute>
                } 
              />
            </Routes>
          </div>
        </Router>
      </ContentProvider>
    </AuthProvider>
  )
}

export default App
