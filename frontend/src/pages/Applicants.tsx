import { Plus, Filter, Download, FileText, FileSpreadsheet, Upload, CheckCircle, Loader2 } from 'lucide-react';
import { Link } from 'react-router-dom';
import { useState } from 'react';

type UploadStatus = 'idle' | 'uploading' | 'success';

interface DocumentModule {
  id: string;
  title: string;
  description: string;
  color: string;
  bgColor: string;
  borderColor: string;
}

const MODULES: DocumentModule[] = [
  { id: 'bank', title: 'Bank Statement', description: 'Upload PDF or CSV statement', color: 'text-blue-600', bgColor: 'bg-blue-100', borderColor: 'border-blue-200' },
  { id: 'itr', title: 'ITR Documents', description: 'Upload ITR-V or Computation', color: 'text-purple-600', bgColor: 'bg-purple-100', borderColor: 'border-purple-200' },
  { id: 'gst', title: 'GST Returns', description: 'Upload GSTR-3B or GSTR-1', color: 'text-indigo-600', bgColor: 'bg-indigo-100', borderColor: 'border-indigo-200' },
  { id: 'loan', title: 'Repayment Capacity', description: 'Upload Existing Loan/EMI Details', color: 'text-amber-600', bgColor: 'bg-amber-100', borderColor: 'border-amber-200' },
];

export default function Applicants() {
  const [files, setFiles] = useState<Record<string, File | null>>({});
  const [statuses, setStatuses] = useState<Record<string, UploadStatus>>({});

  const downloadReport = (module: string, type: 'excel' | 'pdf') => {
    window.open(`http://127.0.0.1:8000/api/reports/APP-1001/${module}/${type}`, '_blank');
  };

  const handleFileChange = (moduleId: string, e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFiles(prev => ({ ...prev, [moduleId]: e.target.files![0] }));
      setStatuses(prev => ({ ...prev, [moduleId]: 'idle' }));
    }
  };

  const handleUpload = (moduleId: string) => {
    if (!files[moduleId]) return;
    setStatuses(prev => ({ ...prev, [moduleId]: 'uploading' }));
    
    // Simulate upload delay
    setTimeout(() => {
      setStatuses(prev => ({ ...prev, [moduleId]: 'success' }));
    }, 1500);
  };

  return (
    <div className="p-8 space-y-8">
      <div className="flex justify-between items-end">
        <div>
          <h1 className="text-3xl font-bold text-slate-900 tracking-tight">Applicant Management</h1>
          <p className="text-slate-500 mt-1">Manage, analyze, and process all loan applicants.</p>
        </div>
        <div className="flex gap-3">
          <button className="px-4 py-2 bg-white border border-slate-200 text-slate-700 font-semibold rounded-xl shadow-sm hover:bg-slate-50 transition-all flex items-center gap-2">
            <Filter size={18} /> Filters
          </button>
          <Link to="/applications/new" className="px-5 py-2.5 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-xl shadow-lg shadow-blue-600/20 transition-all flex items-center gap-2">
            <Plus size={20} /> Add Applicant
          </Link>
        </div>
      </div>

      <div className="space-y-6">
        {MODULES.map((mod) => {
          const file = files[mod.id];
          const status = statuses[mod.id] || 'idle';
          
          return (
            <div key={mod.id} className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden p-8">
              <div className="flex items-center gap-3 mb-6">
                <div className={`${mod.bgColor} p-2.5 rounded-xl ${mod.color}`}>
                  <FileText size={24} />
                </div>
                <div>
                  <h2 className="text-xl font-bold text-slate-900">{mod.title}</h2>
                  <p className="text-slate-500 text-sm mt-1">{mod.description}</p>
                </div>
              </div>
              
              <div className="max-w-2xl">
                {status !== 'success' ? (
                  <div className="flex-1 flex flex-col items-center justify-center border-2 border-dashed border-slate-300 rounded-xl p-8 bg-slate-50 transition-colors hover:border-blue-400">
                    <div className="bg-white shadow-sm p-4 rounded-full mb-4 text-slate-500">
                      <Upload size={24} />
                    </div>
                    <p className="text-sm font-medium text-slate-700 mb-6 text-center">Click or drag file to upload</p>
                    
                    <div className="flex flex-col items-center w-full max-w-sm gap-4">
                      <label className="cursor-pointer bg-white border border-slate-300 px-6 py-2.5 rounded-xl text-sm font-semibold text-slate-700 hover:bg-slate-50 hover:border-slate-400 transition-all w-full text-center shadow-sm">
                        Choose File
                        <input type="file" className="hidden" accept=".pdf,.csv,.xlsx,.zip" onChange={(e) => handleFileChange(mod.id, e)} />
                      </label>
                      
                      {file && (
                        <div className="w-full flex flex-col gap-3 animate-in fade-in">
                          <div className="bg-blue-50 border border-blue-100 rounded-lg py-2 px-3 flex items-center justify-between">
                            <span className="text-xs font-semibold text-blue-700 truncate mr-2">{file.name}</span>
                            <span className="text-[10px] text-blue-500 font-medium px-2 py-0.5 bg-blue-100 rounded-full">{(file.size / 1024).toFixed(0)} KB</span>
                          </div>
                          <button 
                            onClick={() => handleUpload(mod.id)}
                            disabled={status === 'uploading'}
                            className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2.5 rounded-xl text-sm font-bold transition-all disabled:opacity-70 disabled:cursor-not-allowed flex items-center justify-center gap-2 w-full shadow-md shadow-blue-600/20"
                          >
                            {status === 'uploading' && <Loader2 size={18} className="animate-spin" />}
                            {status === 'uploading' ? 'Processing Document...' : 'Generate Reports'}
                          </button>
                        </div>
                      )}
                    </div>
                  </div>
                ) : (
                  <div className="flex-1 flex flex-col bg-emerald-50/50 border border-emerald-200 rounded-xl p-8 animate-in slide-in-from-bottom-4 duration-500">
                    <div className="flex items-center gap-3 mb-8 text-emerald-700 bg-emerald-100/50 p-4 rounded-lg border border-emerald-200/50">
                      <CheckCircle size={24} />
                      <div>
                        <span className="font-bold block text-sm">Processing Complete</span>
                        <span className="text-xs font-medium opacity-80">Your documents have been analyzed successfully.</span>
                      </div>
                    </div>
                    
                    <div>
                      <h4 className="text-xs font-bold text-slate-500 uppercase tracking-wider mb-3">Download Results</h4>
                      <div className="flex flex-col sm:flex-row gap-3">
                        <button onClick={() => downloadReport(mod.id, 'pdf')} className="flex-1 flex items-center justify-center gap-2 px-4 py-3 bg-white border-2 border-slate-200 rounded-xl text-sm font-bold hover:border-blue-400 hover:text-blue-700 hover:shadow-md hover:shadow-blue-500/10 transition-all text-slate-700">
                          PDF Report <Download size={18} />
                        </button>
                        <button onClick={() => downloadReport(mod.id, 'excel')} className="flex-1 flex items-center justify-center gap-2 px-4 py-3 bg-white border-2 border-slate-200 rounded-xl text-sm font-bold hover:border-emerald-400 hover:text-emerald-700 hover:shadow-md hover:shadow-emerald-500/10 transition-all text-slate-700">
                          Excel Data <FileSpreadsheet size={18} />
                        </button>
                      </div>
                    </div>
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}


