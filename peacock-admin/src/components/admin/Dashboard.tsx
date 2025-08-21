import React, { useState } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from './layout/Sidebar';
import Header from './layout/Header';
import Overview from './pages/Overview';
import MetadataEditor from './pages/MetadataEditor';
import CompanyEditor from './pages/CompanyEditor';
import BuyButtonsEditor from './pages/BuyButtonsEditor';
import HeadingsEditor from './pages/HeadingsEditor';
import TestimonialsEditor from './pages/TestimonialsEditor';
import FAQEditor from './pages/FAQEditor';
import ImagesEditor from './pages/ImagesEditor';
import Settings from './pages/Settings';

const Dashboard: React.FC = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className="admin-panel min-h-screen bg-gray-50">
      <div className="flex h-screen overflow-hidden">
        
        {/* Sidebar */}
        <Sidebar 
          isOpen={sidebarOpen} 
          onClose={() => setSidebarOpen(false)} 
        />

        {/* Main Content */}
        <div className="flex-1 flex flex-col overflow-hidden">
          
          {/* Header */}
          <Header onMenuClick={() => setSidebarOpen(true)} />

          {/* Page Content */}
          <main className="flex-1 overflow-x-hidden overflow-y-auto bg-gray-50 p-6">
            <div className="max-w-7xl mx-auto">
              <Routes>
                <Route path="/" element={<Overview />} />
                <Route path="/overview" element={<Overview />} />
                <Route path="/metadata" element={<MetadataEditor />} />
                <Route path="/company" element={<CompanyEditor />} />
                <Route path="/buy-buttons" element={<BuyButtonsEditor />} />
                <Route path="/headings" element={<HeadingsEditor />} />
                <Route path="/testimonials" element={<TestimonialsEditor />} />
                <Route path="/faq" element={<FAQEditor />} />
                <Route path="/images" element={<ImagesEditor />} />
                <Route path="/settings" element={<Settings />} />
                <Route path="*" element={<Navigate to="/admin/overview" replace />} />
              </Routes>
            </div>
          </main>

        </div>

        {/* Mobile Sidebar Overlay */}
        {sidebarOpen && (
          <div 
            className="fixed inset-0 z-40 bg-black bg-opacity-50 lg:hidden"
            onClick={() => setSidebarOpen(false)}
          />
        )}

      </div>
    </div>
  );
};

export default Dashboard;
