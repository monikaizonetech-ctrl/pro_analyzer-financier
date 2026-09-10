from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.services.reports import excel_generator, pdf_generator

router = APIRouter()

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
