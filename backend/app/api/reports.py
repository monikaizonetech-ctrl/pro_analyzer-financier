from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.services.reports import excel_generator, pdf_generator

router = APIRouter()

@router.get("/history")
def get_reports_history():
    return {
        "status": "success",
        "total": 6,
        "items": [
            {
                "id": "REP-9041",
                "applicant_id": "APP-1001",
                "applicant_name": "Suguna Enterprises Private Limited",
                "module": "gst",
                "module_title": "GST Returns (GSTR-3B)",
                "document_name": "GSTR3B_Apr_Sep_2026.pdf",
                "status": "Verified",
                "score": 94,
                "created_at": "2026-09-10T12:45:00Z"
            },
            {
                "id": "REP-9040",
                "applicant_id": "APP-1001",
                "applicant_name": "Suguna M",
                "module": "itr",
                "module_title": "ITR-V Tax Computation",
                "document_name": "ITR_V_AY2025_26_Ack.pdf",
                "status": "Verified",
                "score": 91,
                "created_at": "2026-09-10T12:40:00Z"
            },
            {
                "id": "REP-9039",
                "applicant_id": "APP-1001",
                "applicant_name": "Suguna M",
                "module": "bank",
                "module_title": "Bank Statement Analysis",
                "document_name": "HDFC_Bank_Jul2026_Statement.pdf",
                "status": "Verified",
                "score": 88,
                "created_at": "2026-09-10T12:35:00Z"
            },
            {
                "id": "REP-9038",
                "applicant_id": "APP-1001",
                "applicant_name": "Suguna M",
                "module": "loan",
                "module_title": "Repayment & Bureau Track",
                "document_name": "CIBIL_Repayment_Schedule.xlsx",
                "status": "Verified",
                "score": 95,
                "created_at": "2026-09-10T12:30:00Z"
            }
        ]
    }

@router.get("/{applicant_id}/{module}/excel")
def download_excel(applicant_id: str, module: str):
    module = module.lower()
    
    if module == "bank":
        file_stream = excel_generator.generate_bank_excel(applicant_id)
        filename = f"Bank_Analysis_{applicant_id}.xlsx"
    elif module == "gst":
        file_stream = excel_generator.generate_gst_excel(applicant_id)
        filename = f"GST_Analysis_{applicant_id}.xlsx"
    elif module == "itr":
        file_stream = excel_generator.generate_itr_excel(applicant_id)
        filename = f"ITR_Analysis_{applicant_id}.xlsx"
    elif module == "loan":
        file_stream = excel_generator.generate_loan_excel(applicant_id)
        filename = f"Loan_Analysis_{applicant_id}.xlsx"
    else:
        raise HTTPException(status_code=400, detail="Invalid module specified")

    return StreamingResponse(
        file_stream, 
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )

@router.get("/{applicant_id}/{module}/pdf")
def download_pdf(applicant_id: str, module: str):
    module = module.lower()
    
    if module == "bank":
        file_stream = pdf_generator.generate_bank_pdf(applicant_id)
        filename = f"Bank_Analysis_{applicant_id}.pdf"
    elif module == "gst":
        file_stream = pdf_generator.generate_gst_pdf(applicant_id)
        filename = f"GST_Analysis_{applicant_id}.pdf"
    elif module == "itr":
        file_stream = pdf_generator.generate_itr_pdf(applicant_id)
        filename = f"ITR_Analysis_{applicant_id}.pdf"
    elif module == "loan":
        file_stream = pdf_generator.generate_loan_pdf(applicant_id)
        filename = f"Loan_Analysis_{applicant_id}.pdf"
    else:
        raise HTTPException(status_code=400, detail="Invalid module specified")

    return StreamingResponse(
        file_stream, 
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )
