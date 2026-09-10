import { Link } from 'react-router-dom';
import { ShieldCheck, BarChart3, FileSpreadsheet, ArrowRight, Zap } from 'lucide-react';

export default function Landing() {
  return (
    <div className="min-h-screen bg-slate-900 text-white selection:bg-blue-500/30">
      {/* Navigation */}
      <nav className="container mx-auto px-6 py-6 flex justify-between items-center">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-blue-500 to-indigo-500 flex items-center justify-center">
            <Zap size={20} className="text-white" />
          </div>
          <span className="text-xl font-bold tracking-tight">FINANCIER <span className="text-blue-400">ANALYZER</span></span>
        </div>
        <div className="hidden md:flex gap-8 text-sm font-medium text-slate-300">
          <a href="#features" className="hover:text-white transition-colors">Features</a>
          <a href="#how-it-works" className="hover:text-white transition-colors">How it works</a>
          <a href="#security" className="hover:text-white transition-colors">Security</a>
        </div>
        <div className="flex items-center gap-4">
          <Link to="/login" className="text-sm font-medium text-slate-300 hover:text-white transition-colors">Sign in</Link>
          <Link to="/login" className="px-5 py-2.5 bg-blue-600 hover:bg-blue-500 text-sm font-semibold rounded-full transition-all shadow-[0_0_20px_-5px_rgba(37,99,235,0.5)]">
            Get Started
          </Link>
        </div>
      </nav>

      {/* Hero Section */}
      <main className="container mx-auto px-6 pt-32 pb-24 text-center">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-blue-400 text-sm font-medium mb-8">
          <span className="flex h-2 w-2 rounded-full bg-blue-500"></span>
          Now available for early access
        </div>
        
        <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight mb-8 leading-tight">
          Financial intelligence <br />
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-400">
            at your fingertips.
          </span>
        </h1>
        
        <p className="text-lg md:text-xl text-slate-400 max-w-2xl mx-auto mb-12 leading-relaxed">
          The ultimate Pro-grade analyzer for financiers. Upload bank statements, GST, and ITR documents to instantly generate comprehensive risk assessments and eligibility scores.
        </p>
        
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
          <Link to="/login" className="px-8 py-4 bg-white text-slate-900 hover:bg-slate-100 font-bold rounded-full transition-all flex items-center gap-2 w-full sm:w-auto justify-center">
            Start analyzing <ArrowRight size={20} />
          </Link>
          <button className="px-8 py-4 bg-slate-800 text-white hover:bg-slate-700 font-bold rounded-full transition-all border border-slate-700 w-full sm:w-auto">
            Book a demo
          </button>
        </div>

        {/* Mockup Image Area */}
        <div className="mt-24 relative max-w-5xl mx-auto">
          <div className="absolute inset-0 bg-gradient-to-t from-slate-900 via-transparent to-transparent z-10 h-full"></div>
          <div className="rounded-2xl border border-slate-800 bg-slate-900/50 p-2 shadow-2xl relative overflow-hidden backdrop-blur-sm">
            <div className="absolute inset-0 bg-gradient-to-br from-blue-500/10 to-purple-500/10"></div>
            <img 
              src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=2000&q=80" 
              alt="Dashboard Preview" 
              className="rounded-xl opacity-80 mix-blend-luminosity hover:mix-blend-normal transition-all duration-700"
            />
          </div>
        </div>
      </main>

      {/* Features Grid */}
      <section className="border-t border-slate-800 bg-slate-900/50 relative">
        <div className="container mx-auto px-6 py-24">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold mb-4">Everything you need to assess risk</h2>
            <p className="text-slate-400">Powerful engines built specifically for modern lending.</p>
          </div>
          
          <div className="grid md:grid-cols-3 gap-8">
            <div className="p-8 rounded-2xl bg-slate-800/50 border border-slate-700/50 hover:bg-slate-800 transition-colors">
              <div className="w-12 h-12 rounded-xl bg-blue-500/20 flex items-center justify-center mb-6">
                <BarChart3 className="text-blue-400" size={24} />
              </div>
              <h3 className="text-xl font-bold mb-3">FOIR & DSCR Engine</h3>
              <p className="text-slate-400 leading-relaxed">
                Automatically calculate Fixed Obligation to Income Ratio and Debt Service Coverage Ratio from raw bank statements.
              </p>
            </div>
            
            <div className="p-8 rounded-2xl bg-slate-800/50 border border-slate-700/50 hover:bg-slate-800 transition-colors">
              <div className="w-12 h-12 rounded-xl bg-indigo-500/20 flex items-center justify-center mb-6">
                <FileSpreadsheet className="text-indigo-400" size={24} />
              </div>
              <h3 className="text-xl font-bold mb-3">Smart OCR Extraction</h3>
              <p className="text-slate-400 leading-relaxed">
                Process scanned PDFs, GST returns, and ITR documents with 99% accuracy using our custom OCR models.
              </p>
            </div>

            <div className="p-8 rounded-2xl bg-slate-800/50 border border-slate-700/50 hover:bg-slate-800 transition-colors">
              <div className="w-12 h-12 rounded-xl bg-purple-500/20 flex items-center justify-center mb-6">
                <ShieldCheck className="text-purple-400" size={24} />
              </div>
              <h3 className="text-xl font-bold mb-3">Fraud Detection</h3>
              <p className="text-slate-400 leading-relaxed">
                Identify circular transactions, forged bank statements, and hidden liabilities instantly.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
