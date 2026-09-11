import pandas as pd
from io import BytesIO

def generate_bank_excel(applicant_id: str) -> BytesIO:
    txn_data = {
        "Date": ["01-07-2026", "02-07-2026", "03-07-2026", "05-07-2026", "08-07-2026", "10-07-2026", "12-07-2026", "15-07-2026", "18-07-2026", "22-07-2026", "25-07-2026", "28-07-2026", "31-07-2026"],
        "Description": ["Opening Balance", "Salary Credit", "UPI - Grocery Store", "Electricity Bill", "UPI - Restaurant", "Online Shopping", "Refund Credit", "ATM Withdrawal", "UPI - Fuel Station", "Freelance Payment", "Mobile Recharge", "UPI - Pharmacy", "Interest Credit"],
        "Reference ID": ["OPEN-0701", "SAL-784512", "UPI-123456", "BILL-457821", "UPI-563214", "ECOM-789654", "REF-321478", "ATM-654987", "UPI-112233", "PAY-445566", "MOB-778899", "UPI-998877", "INT-202607"],
        "Debit (INR)": [0, 0, 1250.00, 2340.00, 780.00, 3499.00, 0, 5000.00, 1800.00, 0, 599.00, 1120.00, 0],
        "Credit (INR)": [0, 35000.00, 0, 0, 0, 0, 1200.00, 0, 0, 12500.00, 0, 0, 245.00],
        "Balance (INR)": [50000.00, 85000.00, 83750.00, 81410.00, 80630.00, 77131.00, 78331.00, 73331.00, 71531.00, 84031.00, 83432.00, 82312.00, 82557.00]
    }
    df_txns = pd.DataFrame(txn_data)
    
    summary_data = {
        "Metric": ["Average Monthly Income", "Existing EMI Obligations", "Estimated Living Expenses", "Net Disposable Income", "FOIR", "Suggested Max EMI"],
        "Value": ["₹ 48,945", "₹ 15,000", "₹ 12,500", "₹ 21,445", "30.64%", "₹ 18,000"],
        "Status": ["Verified", "Active", "Calculated", "Available", "Good", "Recommended"]
    }
    df_sum = pd.DataFrame(summary_data)
    
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_txns.to_excel(writer, sheet_name='Transactions', index=False)
        df_sum.to_excel(writer, sheet_name='Capacity_Summary', index=False)
    
    output.seek(0)
    return output

def generate_gst_excel(applicant_id: str) -> BytesIO:
    gst_data = {
        "Month": ["Apr 2026", "May 2026", "Jun 2026", "Jul 2026", "Aug 2026", "Sep 2026"],
        "Return Type": ["GSTR-3B", "GSTR-3B", "GSTR-3B", "GSTR-3B", "GSTR-3B", "GSTR-3B"],
        "Taxable Turnover (INR)": [450000, 480000, 510000, 495000, 525000, 560000],
        "CGST (INR)": [40500, 43200, 45900, 44550, 47250, 50400],
        "SGST (INR)": [40500, 43200, 45900, 44550, 47250, 50400],
        "IGST (INR)": [0, 0, 0, 0, 0, 0],
        "Total Tax (INR)": [81000, 86400, 91800, 89100, 94500, 100800],
        "ITC Claimed (INR)": [32400, 34560, 36720, 35640, 37800, 40320],
        "Filing Status": ["ON TIME", "ON TIME", "ON TIME", "ON TIME", "ON TIME", "ON TIME"]
    }
    df_gst = pd.DataFrame(gst_data)
    
    summary_data = {
        "Metric": ["Annualized Turnover", "Average Monthly Sales", "ITC Utilization Rate", "Compliance Rate", "Estimated Margin", "Suggested WC Limit"],
        "Value": ["₹ 60,40,000", "₹ 5,03,333", "40.0%", "100% (6/6)", "16.50%", "₹ 15,00,000"],
        "Status": ["Verified & Healthy", "Consistent Growth", "Optimal ITC Flow", "On-time", "Healthy Margin", "Recommended"]
    }
    df_sum = pd.DataFrame(summary_data)
    
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_gst.to_excel(writer, sheet_name='Monthly_GST_Returns', index=False)
        df_sum.to_excel(writer, sheet_name='GST_Capacity_Assessment', index=False)
    
    output.seek(0)
    return output

def generate_itr_excel(applicant_id: str) -> BytesIO:
    itr_data = {
        "Assessment Year": ["AY 2025-26", "AY 2024-25", "AY 2023-24"],
        "Financial Year": ["FY 2024-25", "FY 2023-24", "FY 2022-23"],
        "Gross Total Income (INR)": [1250000, 1080000, 950000],
        "Chapter VI-A Deductions (INR)": [150000, 150000, 150000],
        "Net Taxable Income (INR)": [1100000, 930000, 800000],
        "Total Tax Paid (INR)": [122408, 98500, 72500],
        "YoY Growth Rate": ["+15.7%", "+13.7%", "-"],
        "Filing Status": ["ON TIME", "ON TIME", "ON TIME"]
    }
    df_itr = pd.DataFrame(itr_data)
    
    summary_data = {
        "Metric": ["3-Year Average Income", "3-Year Income CAGR", "Monthly Net Disposable", "Existing Debt Commitment", "FOIR", "Max Loan Eligibility"],
        "Value": ["₹ 10,93,333", "+14.7%", "₹ 93,966", "₹ 1,80,000", "15.96%", "₹ 45,00,000"],
        "Status": ["Verified", "Strong Growth", "Calculated", "Active", "Excellent (< 50%)", "Approved Limit"]
    }
    df_sum = pd.DataFrame(summary_data)
    
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_itr.to_excel(writer, sheet_name='ITR_Multi_Year_Summary', index=False)
        df_sum.to_excel(writer, sheet_name='Income_Capacity_Assessment', index=False)
    
    output.seek(0)
    return output

def generate_loan_excel(applicant_id: str) -> BytesIO:
    loan_data = {
        "Lender Institution": ["HDFC Bank Ltd", "State Bank of India"],
        "Loan Type": ["Auto / Car Loan", "Personal Loan"],
        "Sanction Amount (INR)": [450000, 300000],
        "Outstanding Balance (INR)": [275000, 175000],
        "Monthly EMI (INR)": [15000, 8000],
        "Tenure Left (Months)": [21, 26],
        "DPD / Overdue Status": ["0 DPD (Clean)", "0 DPD (Clean)"]
    }
    df_loan = pd.DataFrame(loan_data)
    
    summary_data = {
        "Metric": ["Monthly Verified Income", "Total Existing EMIs", "Current FOIR", "Net Available Cashflow", "CIBIL Bureau Track", "Max Additional Loan"],
        "Value": ["₹ 93,966", "₹ 23,000", "24.47%", "₹ 70,966", "785 (Clean Track)", "₹ 20,00,000"],
        "Status": ["Active", "Active Commitments", "Healthy (< 50%)", "Sufficient Buffer", "Excellent", "Recommended Eligible"]
    }
    df_sum = pd.DataFrame(summary_data)
    
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df_loan.to_excel(writer, sheet_name='Active_Loan_Accounts', index=False)
        df_sum.to_excel(writer, sheet_name='FOIR_Debt_Assessment', index=False)
    
    output.seek(0)
    return output
