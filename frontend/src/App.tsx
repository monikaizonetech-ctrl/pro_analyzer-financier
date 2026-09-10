import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';

import Landing from './pages/Landing';

import DashboardLayout from './layouts/DashboardLayout';
import Applicants from './pages/Applicants';
import NewApplication from './pages/NewApplication';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<Login />} />
          <Route element={<DashboardLayout />}>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/applicants" element={<Applicants />} />
            <Route path="/applications/new" element={<NewApplication />} />
            <Route path="/reports" element={<div className="p-8"><h1 className="text-3xl font-bold">Reports</h1></div>} />
          </Route>
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  );
}

export default App;
