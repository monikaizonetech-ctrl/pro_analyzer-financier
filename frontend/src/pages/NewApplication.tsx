import { useState } from 'react';
import { ArrowLeft, Upload, CheckCircle2 } from 'lucide-react';
import { Link, useNavigate } from 'react-router-dom';

export default function NewApplication() {
  const navigate = useNavigate();
  const [step, setStep] = useState(1);
  const [files, setFiles] = useState<Record<string, File>>({});

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (step < 3) {
      setStep(step + 1);
    } else {
      // Final submission
      alert('Application submitted for processing!');
      navigate('/dashboard');
    }
  };

  return (
    <div className="p-8 max-w-4xl mx-auto space-y-8">
      <div className="flex items-center gap-4">
        <Link to="/dashboard" className="p-2 bg-white rounded-full border border-slate-200 text-slate-500 hover:text-slate-900 shadow-sm transition-all">
          <ArrowLeft size={20} />
        </Link>
        <div>
          <h1 className="text-3xl font-bold text-slate-900 tracking-tight">New Loan Application</h1>
          <p className="text-slate-500 mt-1">Follow the steps below to initialize a new financial assessment.</p>
        </div>
      </div>

      {/* Progress Steps */}
      <div className="flex items-center justify-between relative">
        <div className="absolute left-0 top-1/2 -translate-y-1/2 w-full h-1 bg-slate-200 -z-10 rounded-full"></div>
        <div className="absolute left-0 top-1/2 -translate-y-1/2 h-1 bg-blue-600 -z-10 rounded-full transition-all duration-500" style={{ width: `${((step - 1) / 2) * 100}%` }}></div>
        
        {[
          { num: 1, title: 'Applicant Details' },
          { num: 2, title: 'Loan Requirements' },
          { num: 3, title: 'Document Upload' }
        ].map((s) => (
          <div key={s.num} className="flex flex-col items-center gap-2 bg-slate-50 px-2">
            <div className={`w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm border-2 transition-colors ${step >= s.num ? 'bg-blue-600 border-blue-600 text-white' : 'bg-white border-slate-300 text-slate-400'}`}>
              {step > s.num ? <CheckCircle2 size={20} /> : s.num}
            </div>
            <span className={`text-xs font-semibold ${step >= s.num ? 'text-blue-700' : 'text-slate-400'}`}>{s.title}</span>
          </div>
        ))}
      </div>

      <form onSubmit={handleSubmit} className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
        <div className="p-8">
          {step === 1 && (
            <div className="space-y-6 animate-in fade-in slide-in-from-right-4 duration-500">
              <h2 className="text-xl font-bold text-slate-900 border-b pb-4">Applicant Information</h2>
              <div className="grid grid-cols-2 gap-6">
                <div className="col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">Applicant / Company Name *</label>
                  <input type="text" required className="w-full rounded-xl border border-slate-300 px-4 py-2.5 focus:ring-2 focus:ring-blue-500 outline-none transition-all" placeholder="Acme Corporation" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Entity Type *</label>
                  <select required className="w-full rounded-xl border border-slate-300 px-4 py-2.5 focus:ring-2 focus:ring-blue-500 outline-none transition-all bg-white">
                    <option value="">Select Type</option>
                    <option value="Private Limited">Private Limited</option>
                    <option value="Proprietorship">Proprietorship</option>
                    <option value="Partnership">Partnership</option>
                    <option value="Individual">Individual</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Industry</label>
                  <input type="text" className="w-full rounded-xl border border-slate-300 px-4 py-2.5 focus:ring-2 focus:ring-blue-500 outline-none transition-all" placeholder="Manufacturing" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Email Address *</label>
                  <input type="email" required className="w-full rounded-xl border border-slate-300 px-4 py-2.5 focus:ring-2 focus:ring-blue-500 outline-none transition-all" placeholder="contact@acme.com" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Mobile Number *</label>
                  <input type="tel" required className="w-full rounded-xl border border-slate-300 px-4 py-2.5 focus:ring-2 focus:ring-blue-500 outline-none transition-all" placeholder="+91 9876543210" />
                </div>
              </div>
            </div>
          )}

          {step === 2 && (
            <div className="space-y-6 animate-in fade-in slide-in-from-right-4 duration-500">
              <h2 className="text-xl font-bold text-slate-900 border-b pb-4">Loan Requirements</h2>
              <div className="grid grid-cols-2 gap-6">
                <div className="col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-1">Loan Purpose *</label>
                  <input type="text" required className="w-full rounded-xl border border-slate-300 px-4 py-2.5 focus:ring-2 focus:ring-blue-500 outline-none transition-all" placeholder="Working Capital Expansion" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Requested Amount ($) *</label>
                  <input type="number" required min="1000" className="w-full rounded-xl border border-slate-300 px-4 py-2.5 focus:ring-2 focus:ring-blue-500 outline-none transition-all" placeholder="500000" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Proposed Tenure (Months) *</label>
                  <input type="number" required min="6" max="360" className="w-full rounded-xl border border-slate-300 px-4 py-2.5 focus:ring-2 focus:ring-blue-500 outline-none transition-all" placeholder="60" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Proposed Interest Rate (%) *</label>
                  <input type="number" step="0.1" required className="w-full rounded-xl border border-slate-300 px-4 py-2.5 focus:ring-2 focus:ring-blue-500 outline-none transition-all" placeholder="10.5" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">Loan Type *</label>
                  <select required className="w-full rounded-xl border border-slate-300 px-4 py-2.5 focus:ring-2 focus:ring-blue-500 outline-none transition-all bg-white">
                    <option value="">Select Type</option>
                    <option value="Term Loan">Term Loan</option>
                    <option value="Working Capital">Working Capital</option>
                    <option value="Overdraft">Overdraft</option>
                    <option value="Mortgage">Mortgage</option>
                  </select>
                </div>
              </div>
            </div>
          )}

          {step === 3 && (
            <div className="space-y-6 animate-in fade-in slide-in-from-right-4 duration-500">
              <h2 className="text-xl font-bold text-slate-900 border-b pb-4">Document Upload</h2>
              <p className="text-slate-500 text-sm">Upload financial documents. Our OCR engine will automatically extract and categorize transactions.</p>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {[
                  { id: 'bank', name: 'Bank Statement (Last 12 Months)', req: true },
                  { id: 'gst', name: 'GST Returns (GSTR-3B)', req: true },
                  { id: 'itr', name: 'Income Tax Returns (ITR)', req: true },
                  { id: 'loan', name: 'Existing Loan Schedules', req: false },
                ].map((doc) => (
                  <label key={doc.id} className="border-2 border-dashed border-slate-300 rounded-xl p-6 flex flex-col items-center justify-center text-center hover:bg-slate-50 hover:border-blue-400 transition-all cursor-pointer group relative overflow-hidden">
                    <input 
                      type="file" 
                      className="hidden" 
                      onChange={(e) => {
                        if (e.target.files?.[0]) {
                          setFiles({...files, [doc.id]: e.target.files[0]});
                        }
                      }}
                    />
                    
                    {files[doc.id] ? (
                      <div className="flex flex-col items-center">
                        <div className="w-12 h-12 bg-emerald-50 rounded-full flex items-center justify-center text-emerald-600 mb-3">
                          <CheckCircle2 size={24} />
                        </div>
                        <p className="font-bold text-emerald-700 text-sm truncate max-w-[200px]">{files[doc.id].name}</p>
                        <p className="text-xs text-emerald-600 mt-1">{(files[doc.id].size / 1024 / 1024).toFixed(2)} MB</p>
                      </div>
                    ) : (
                      <>
                        <div className="w-12 h-12 bg-blue-50 rounded-full flex items-center justify-center text-blue-600 mb-3 group-hover:scale-110 transition-transform">
                          <Upload size={24} />
                        </div>
                        <p className="font-semibold text-slate-900 text-sm">{doc.name}</p>
                        <p className="text-xs text-slate-500 mt-1">{doc.req ? '*Required' : 'Optional'} (PDF, CSV, Excel)</p>
                      </>
                    )}
                  </label>
                ))}
              </div>
            </div>
          )}
        </div>

        <div className="px-8 py-5 bg-slate-50 border-t border-slate-200 flex justify-between items-center">
          <button 
            type="button" 
            onClick={() => setStep(Math.max(1, step - 1))}
            className={`px-6 py-2.5 font-semibold rounded-xl transition-all ${step === 1 ? 'opacity-0 pointer-events-none' : 'text-slate-600 hover:bg-slate-200 bg-slate-100'}`}
          >
            Back
          </button>
          
          <button type="submit" className="px-8 py-2.5 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-xl shadow-lg shadow-blue-600/20 transition-all">
            {step === 3 ? 'Submit for Processing' : 'Continue Next Step'}
          </button>
        </div>
      </form>
    </div>
  );
}
