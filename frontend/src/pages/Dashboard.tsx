import { TrendingUp, Clock, CheckCircle2, AlertCircle } from 'lucide-react';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'Jan', applications: 40, approved: 24 },
  { name: 'Feb', applications: 30, approved: 13 },
  { name: 'Mar', applications: 20, approved: 98 },
  { name: 'Apr', applications: 27, approved: 39 },
  { name: 'May', applications: 18, approved: 48 },
  { name: 'Jun', applications: 23, approved: 38 },
  { name: 'Jul', applications: 34, approved: 43 },
];

const recentApplicants = [
  { id: 'APP-1001', name: 'Acme Corp', type: 'Business', status: 'Completed', score: 85, date: '2026-09-08' },
  { id: 'APP-1002', name: 'John Doe', type: 'Individual', status: 'Processing', score: null, date: '2026-09-08' },
  { id: 'APP-1003', name: 'TechFlow Inc', type: 'Business', status: 'High Risk', score: 42, date: '2026-09-07' },
  { id: 'APP-1004', name: 'Jane Smith', type: 'Individual', status: 'Completed', score: 92, date: '2026-09-06' },
];

import { Link } from 'react-router-dom';

export default function Dashboard() {
  return (
    <div className="p-8 space-y-8">
      <div className="flex justify-between items-end">
        <div>
          <h1 className="text-3xl font-bold text-slate-900 tracking-tight">Overview</h1>
          <p className="text-slate-500 mt-1">Here is the latest financial data and application status.</p>
        </div>
        <Link to="/applications/new" className="px-5 py-2.5 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-xl shadow-lg shadow-blue-600/20 transition-all flex items-center gap-2">
          <span className="text-xl leading-none">+</span> New Application
        </Link>
      </div>

      {/* KPI Stats */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden group">
          <div className="absolute -right-4 -top-4 w-24 h-24 bg-blue-50 rounded-full group-hover:scale-150 transition-transform duration-500 ease-out"></div>
          <p className="text-slate-500 text-sm font-medium relative z-10">Total Applications</p>
          <h3 className="text-3xl font-black text-slate-900 mt-2 relative z-10">1,284</h3>
          <div className="flex items-center gap-2 mt-4 relative z-10 text-emerald-600 text-sm font-medium">
            <TrendingUp size={16} /> <span>+12.5% from last month</span>
          </div>
        </div>
        <div className="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden group">
          <div className="absolute -right-4 -top-4 w-24 h-24 bg-amber-50 rounded-full group-hover:scale-150 transition-transform duration-500 ease-out"></div>
          <p className="text-slate-500 text-sm font-medium relative z-10">Pending Review</p>
          <h3 className="text-3xl font-black text-slate-900 mt-2 relative z-10">42</h3>
          <div className="flex items-center gap-2 mt-4 relative z-10 text-amber-600 text-sm font-medium">
            <Clock size={16} /> <span>Requires attention</span>
          </div>
        </div>
        <div className="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden group">
          <div className="absolute -right-4 -top-4 w-24 h-24 bg-emerald-50 rounded-full group-hover:scale-150 transition-transform duration-500 ease-out"></div>
          <p className="text-slate-500 text-sm font-medium relative z-10">Approved Loans</p>
          <h3 className="text-3xl font-black text-slate-900 mt-2 relative z-10">892</h3>
          <div className="flex items-center gap-2 mt-4 relative z-10 text-emerald-600 text-sm font-medium">
            <CheckCircle2 size={16} /> <span>$42.5M Total Disbursed</span>
          </div>
        </div>
        <div className="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm hover:shadow-md transition-shadow relative overflow-hidden group">
          <div className="absolute -right-4 -top-4 w-24 h-24 bg-red-50 rounded-full group-hover:scale-150 transition-transform duration-500 ease-out"></div>
          <p className="text-slate-500 text-sm font-medium relative z-10">High Risk Alerts</p>
          <h3 className="text-3xl font-black text-slate-900 mt-2 relative z-10">14</h3>
          <div className="flex items-center gap-2 mt-4 relative z-10 text-red-600 text-sm font-medium">
            <AlertCircle size={16} /> <span>Critical FOIR/DSCR flags</span>
          </div>
        </div>
      </div>

      {/* Charts & Tables Section */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Chart */}
        <div className="bg-white p-6 rounded-2xl border border-slate-100 shadow-sm lg:col-span-2">
          <h3 className="text-lg font-bold text-slate-900 mb-6">Application Trends</h3>
          <div className="h-72">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={data} margin={{ top: 10, right: 30, left: 0, bottom: 0 }}>
                <defs>
                  <linearGradient id="colorUv" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
                <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{fill: '#64748b'}} dy={10} />
                <YAxis axisLine={false} tickLine={false} tick={{fill: '#64748b'}} dx={-10} />
                <Tooltip 
                  contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }}
                />
                <Area type="monotone" dataKey="applications" stroke="#3b82f6" strokeWidth={3} fillOpacity={1} fill="url(#colorUv)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Recent Table */}
        <div className="bg-white rounded-2xl border border-slate-100 shadow-sm overflow-hidden flex flex-col">
          <div className="p-6 border-b border-slate-100 flex justify-between items-center">
            <h3 className="text-lg font-bold text-slate-900">Recent Assessments</h3>
            <button className="text-sm font-semibold text-blue-600 hover:text-blue-700">View All</button>
          </div>
          <div className="flex-1 overflow-auto">
            <table className="w-full text-sm text-left">
              <thead className="bg-slate-50 text-slate-500 font-medium">
                <tr>
                  <th className="px-6 py-3">Applicant</th>
                  <th className="px-6 py-3">Status</th>
                  <th className="px-6 py-3 text-right">Score</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {recentApplicants.map((app) => (
                  <tr key={app.id} className="hover:bg-slate-50 transition-colors cursor-pointer">
                    <td className="px-6 py-4">
                      <p className="font-bold text-slate-900">{app.name}</p>
                      <p className="text-xs text-slate-500">{app.id}</p>
                    </td>
                    <td className="px-6 py-4">
                      <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold
                        ${app.status === 'Completed' ? 'bg-emerald-100 text-emerald-700' : 
                          app.status === 'Processing' ? 'bg-blue-100 text-blue-700' : 
                          'bg-red-100 text-red-700'}`}>
                        {app.status}
                      </span>
                    </td>
                    <td className="px-6 py-4 text-right">
                      {app.score ? (
                        <span className={`font-bold ${app.score > 70 ? 'text-emerald-600' : 'text-red-600'}`}>
                          {app.score}/100
                        </span>
                      ) : (
                        <span className="text-slate-400 font-medium">-</span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
