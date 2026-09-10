import pandas as pd
from io import BytesIO

def generate_bank_excel(applicant_id: str) -> BytesIO:
    # Mock data
    data = {
        "Date": ["2026-09-01", "2026-09-03", "2026-09-05"],
        "Description": ["Salary Credit", "Rent Payment", "Utility Bill"],
        "Credit": [5000.00, 0, 0],
        "Debit": [0, 1500.00, 200.00],
        "Balance": [5000.00, 3500.00, 3300.00]
    }
    df = pd.DataFrame(data)
    
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Bank_Analysis', index=False)
    
    output.seek(0)
    return output

def generate_gst_excel(applicant_id: str) -> BytesIO:
    data = {
        "Month": ["Jan", "Feb", "Mar"],
        "Total Sales": [10000, 12000, 15000],
        "GST Paid": [1800, 2160, 2700]
    }
    df = pd.DataFrame(data)
    
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='GST_Analysis', index=False)
    
    output.seek(0)
    return output

def generate_itr_excel(applicant_id: str) -> BytesIO:
    data = {
        "Assessment Year": ["2024-25", "2025-26"],
        "Gross Total Income": [800000, 950000],
        "Tax Paid": [60000, 75000]
    }
    df = pd.DataFrame(data)
    
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='ITR_Analysis', index=False)
    
    output.seek(0)
    return output

def generate_loan_excel(applicant_id: str) -> BytesIO:
    data = {
        "Bank Name": ["HDFC", "SBI"],
        "Loan Type": ["Personal", "Car"],
        "EMI Amount": [15000, 8000],
        "Outstanding Balance": [300000, 150000]
    }
    df = pd.DataFrame(data)
    
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Loan_Analysis', index=False)
    
    output.seek(0)
    return output
