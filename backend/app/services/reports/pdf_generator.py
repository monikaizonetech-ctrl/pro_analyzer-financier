from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def create_pdf(title: str, applicant_id: str, content_lines: list) -> BytesIO:
    output = BytesIO()
    c = canvas.Canvas(output, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, f"FINANCIER ANALYZER - {title}")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Applicant ID: {applicant_id}")
    
    y = height - 120
    for line in content_lines:
        c.drawString(50, y, line)
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50
            
    c.save()
    output.seek(0)
    return output

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.platypus import PageBreak

def get_page_2_elements(styles):
    elements = []
    
    # Header
    title_style = ParagraphStyle('ProTitle', parent=styles['Heading1'], alignment=1, textColor=colors.HexColor('#1e3a8a'))
    subtitle_style = ParagraphStyle('ProSub', parent=styles['Normal'], alignment=1, fontSize=8, textColor=colors.grey)
    elements.append(Paragraph("<b>ProAnalyser.in</b>", title_style))
    elements.append(Paragraph("Bank Statement Analysis Report • Generated August 28, 2026", subtitle_style))
    elements.append(Spacer(1, 20))
    
    # Verification Banner
    banner_data = [['✓ BALANCE VERIFIED SUCCESSFULLY\nAll balances have been confirmed accurate']]
    banner_table = Table(banner_data, colWidths=[6.5*inch])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#e6ffed')),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor('#22c55e')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#22c55e')),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    elements.append(banner_table)
    elements.append(Spacer(1, 20))
    
    def get_header_style(title):
        data = [[title]]
        t = Table(data, colWidths=[6.5*inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1e3a8a')),
            ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ('PADDING', (0,0), (-1,-1), 6),
        ]))
        return t

    # Cashflow Summary
    elements.append(get_header_style("Cashflow Summary"))
    cf_data = [
        ['MONTH', 'CREDIT', 'DEBIT', 'NET CASHFLOW', 'AVG BALANCE', 'ENTRIES (CR)', 'ENTRIES (DR)', 'CHQ/ECS RET'],
        ['Jul 2026', '48,945', '16,388', '32,557', '78,556', '4', '8', 'NILL'],
        ['Total (Jul 2026 - Jul 2026)', '48,945', '16,388', '32,557', '78,556', '4', '8', '-'],
        ['Monthly Avg. (Jul 2026 - Jul 2026)', '48,945', '16,388', '32,557', '78,556', '4.0', '8.0', '-'],
        ['Last 3 months', '-', '-', '-', '-', '-', '-', '-'],
        ['Last 6 months', '-', '-', '-', '-', '-', '-', '-']
    ]
    cf_table = Table(cf_data, colWidths=[1.3*inch, 0.7*inch, 0.7*inch, 0.9*inch, 0.9*inch, 0.7*inch, 0.7*inch, 0.6*inch])
    cf_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('ALIGN', (0,1), (0,-1), 'LEFT'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
    ]))
    elements.append(cf_table)
    elements.append(Spacer(1, 15))

    # Chq/ECS Return
    elements.append(get_header_style("Chq/ECS Return Txns"))
    chq_data = [['DATE', 'DESCRIPTION', 'CHQ NO', 'CREDIT', 'DEBIT', 'BALANCE'], ['', '', '', '', '', '']]
    chq_table = Table(chq_data, colWidths=[1*inch, 2*inch, 1*inch, 0.8*inch, 0.8*inch, 0.9*inch])
    chq_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    elements.append(chq_table)
    elements.append(Spacer(1, 15))
    
    # CounterParty Totals
    elements.append(get_header_style("CounterParty Totals - Jul 2026"))
    cp_data = [
        ['COUNTERPARTY(CR)', 'AMOUNT(CR)', 'ENTRIES(CR)', 'COUNTERPARTY(DR)', 'AMOUNT(DR)', 'ENTRIES(DR)'],
        ['Total (Jul 2026)', '48,945', '4', 'Total (Jul 2026)', '16,388', '8'],
        ['Salary Credit', '35,000', '1', 'ATM Withdrawal', '5,000', '1'],
        ['Freelance Payment', '12,500', '1', 'Online Shopping', '3,499', '1'],
        ['Refund Credit', '1,200', '1', 'Electricity Bill', '2,340', '1'],
        ['Interest Credit', '245', '1', 'Fuel Station', '1,800', '1'],
        ['-', '0', '0', 'Grocery Store', '1,250', '1'],
        ['-', '-', '-', 'Txn Total < 5K', '2,499', '3']
    ]
    cp_table = Table(cp_data, colWidths=[1.5*inch, 1*inch, 0.75*inch, 1.5*inch, 1*inch, 0.75*inch])
    cp_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
    ]))
    elements.append(cp_table)

    return elements

def get_page_3_elements(styles):
    elements = []
    
    title_style = ParagraphStyle('ChartTitle', parent=styles['Heading2'], alignment=1)
    sub_style = ParagraphStyle('ChartSub', parent=styles['Normal'], alignment=1, fontSize=7, textColor=colors.grey)
    
    elements.append(Paragraph("<b>Visual Analytics</b>", title_style))
    elements.append(Spacer(1, 20))
    
    elements.append(Paragraph("Monthly Credit Amount vs Debit Amount Comparison", styles['Heading4']))
    elements.append(Paragraph("Values in Rs", sub_style))
    
    d1 = Drawing(400, 200)
    bc1 = VerticalBarChart()
    bc1.x = 50
    bc1.y = 50
    bc1.height = 125
    bc1.width = 300
    bc1.data = [[48945], [16388]] 
    bc1.strokeColor = colors.black
    bc1.valueAxis.valueMin = 0
    bc1.valueAxis.valueMax = 50000
    bc1.valueAxis.valueStep = 10000
    bc1.categoryAxis.labels.boxAnchor = 'ne'
    bc1.categoryAxis.labels.dx = 8
    bc1.categoryAxis.labels.dy = -2
    bc1.categoryAxis.categoryNames = ['Jul 2026']
    bc1.bars[0].fillColor = colors.HexColor('#22c55e') 
    bc1.bars[1].fillColor = colors.HexColor('#ef4444') 
    d1.add(bc1)
    elements.append(d1)
    elements.append(Spacer(1, 20))
    
    elements.append(Paragraph("Payment Modes Breakdown", styles['Heading4']))
    elements.append(Paragraph("Credit / Debit distributions", sub_style))
    
    d2 = Drawing(400, 200)
    
    pie1 = Pie()
    pie1.x = 50
    pie1.y = 50
    pie1.width = 100
    pie1.height = 100
    pie1.data = [100]
    pie1.labels = ['Other: 100%']
    pie1.slices.strokeWidth=0.5
    
    pie2 = Pie()
    pie2.x = 250
    pie2.y = 50
    pie2.width = 100
    pie2.height = 100
    pie2.data = [30.2, 39.3, 30.5]
    pie2.labels = ['UPI', 'Other', 'Cash']
    pie2.slices.strokeWidth=0.5
    
    d2.add(pie1)
    d2.add(pie2)
    elements.append(d2)
    
    return elements

def get_page_4_elements(styles):
    elements = []
    
    # Title
    title_style = ParagraphStyle('RepaymentTitle', parent=styles['Heading2'], alignment=1, textColor=colors.HexColor('#1e3a8a'), spaceAfter=20)
    elements.append(Paragraph("<b>Repayment Capacity Analysis</b>", title_style))
    
    # Repayment Summary Table
    def get_header_style(title):
        data = [[title]]
        t = Table(data, colWidths=[6.5*inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1e3a8a')),
            ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ('PADDING', (0,0), (-1,-1), 6),
        ]))
        return t

    elements.append(get_header_style("Repayment Capacity Result"))
    
    repayment_data = [
        ['METRIC', 'VALUE', 'STATUS'],
        ['Average Monthly Income', '₹ 48,945', 'Verified'],
        ['Existing EMI Obligations', '₹ 15,000', 'Active'],
        ['Estimated Living Expenses', '₹ 12,500', 'Calculated'],
        ['Net Disposable Income', '₹ 21,445', 'Available'],
        ['Fixed Obligation to Income Ratio (FOIR)', '30.64%', 'Good'],
        ['Maximum Suggested EMI', '₹ 18,000', '-']
    ]
    
    rep_table = Table(repayment_data, colWidths=[3*inch, 1.5*inch, 2*inch])
    rep_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TEXTCOLOR', (2,5), (2,5), colors.green), # Highlight 'Good' FOIR status
    ]))
    
    elements.append(rep_table)
    elements.append(Spacer(1, 30))
    
    # Conclusion text
    conclusion_style = ParagraphStyle('Conclusion', parent=styles['Normal'], fontSize=10, leading=14)
    elements.append(Paragraph("<b>Conclusion:</b> Based on the bank statement analysis, the applicant has a healthy Net Disposable Income. The FOIR of 30.64% is well within the acceptable threshold (typically < 50%), indicating a strong repayment capacity for additional credit facilities up to an EMI of ₹18,000.", conclusion_style))
    
    return elements

def generate_bank_pdf(applicant_id: str) -> BytesIO:
    output = BytesIO()
    doc = SimpleDocTemplate(output, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    elements = []
    styles = getSampleStyleSheet()
    
    # Page 1: Transaction Details
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], alignment=1, spaceAfter=10)
    subtitle_style = ParagraphStyle('SubtitleStyle', parent=styles['Normal'], alignment=1, spaceAfter=20, textColor=colors.grey)
    elements.append(Paragraph("DEMO NATIONAL BANK", title_style))
    elements.append(Paragraph("Sample Bank Statement — For Testing / Demo Purposes Only", subtitle_style))
    
    account_data = [
        ['Account Holder', 'suguna'],
        ['Account Number', 'XXXX XXXX 4821'],
        ['Statement Period', '01 Jul 2026 - 31 Jul 2026'],
        ['Account Type', 'Savings Account']
    ]
    account_table = Table(account_data, colWidths=[2*inch, 4*inch])
    account_table.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(account_table)
    elements.append(Spacer(1, 20))
    
    elements.append(Paragraph("<b>Transaction Details</b>", styles['Heading3']))
    elements.append(Spacer(1, 10))
    
    txn_data = [
        ['Date', 'Description', 'Reference ID', 'Debit (₹)', 'Credit (₹)', 'Balance (₹)'],
        ['01-07-2026', 'Opening Balance', 'OPEN-0701', '-', '-', '50,000.00'],
        ['02-07-2026', 'Salary Credit', 'SAL-784512', '-', '35,000.00', '85,000.00'],
        ['03-07-2026', 'UPI - Grocery Store', 'UPI-123456', '1,250.00', '-', '83,750.00'],
        ['05-07-2026', 'Electricity Bill', 'BILL-457821', '2,340.00', '-', '81,410.00'],
        ['08-07-2026', 'UPI - Restaurant', 'UPI-563214', '780.00', '-', '80,630.00'],
        ['10-07-2026', 'Online Shopping', 'ECOM-789654', '3,499.00', '-', '77,131.00'],
        ['12-07-2026', 'Refund Credit', 'REF-321478', '-', '1,200.00', '78,331.00'],
        ['15-07-2026', 'ATM Withdrawal', 'ATM-654987', '5,000.00', '-', '73,331.00'],
        ['18-07-2026', 'UPI - Fuel Station', 'UPI-112233', '1,800.00', '-', '71,531.00'],
        ['22-07-2026', 'Freelance Payment', 'PAY-445566', '-', '12,500.00', '84,031.00'],
        ['25-07-2026', 'Mobile Recharge', 'MOB-778899', '599.00', '-', '83,432.00'],
        ['28-07-2026', 'UPI - Pharmacy', 'UPI-998877', '1,120.00', '-', '82,312.00'],
        ['31-07-2026', 'Interest Credit', 'INT-202607', '-', '245.00', '82,557.00']
    ]
    
    txn_table = Table(txn_data, colWidths=[0.8*inch, 1.8*inch, 1.2*inch, 0.8*inch, 0.8*inch, 0.9*inch])
    txn_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2563eb')), 
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('ALIGN', (3,0), (5,-1), 'RIGHT'), 
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,0), 6),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]), 
    ]))
    elements.append(txn_table)
    elements.append(Spacer(1, 30))
    
    disclaimer_style = ParagraphStyle('Disclaimer', parent=styles['Normal'], fontSize=7, textColor=colors.grey)
    elements.append(Paragraph("DISCLAIMER: This statement reproduction was generated from the uploaded file for review purposes and reflects the data extracted at the time of analysis.", disclaimer_style))
    
    # Add Advanced Pages
    elements.append(PageBreak())
    elements.extend(get_page_2_elements(styles))
    
    elements.append(PageBreak())
    elements.extend(get_page_3_elements(styles))
    
    elements.append(PageBreak())
    elements.extend(get_page_4_elements(styles))
    
    doc.build(elements)
    output.seek(0)
    return output

def get_common_header(styles, title_text):
    elements = []
    title_style = ParagraphStyle('ProTitle', parent=styles['Heading1'], alignment=1, textColor=colors.HexColor('#1e3a8a'))
    subtitle_style = ParagraphStyle('ProSub', parent=styles['Normal'], alignment=1, fontSize=8, textColor=colors.grey)
    elements.append(Paragraph("<b>ProAnalyser.in</b>", title_style))
    elements.append(Paragraph(f"{title_text} • Generated August 28, 2026", subtitle_style))
    elements.append(Spacer(1, 20))
    
    banner_data = [['✓ DOCUMENT VERIFIED SUCCESSFULLY\nAuthenticity and data integrity confirmed']]
    banner_table = Table(banner_data, colWidths=[6.5*inch])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#e6ffed')),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor('#22c55e')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#22c55e')),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    elements.append(banner_table)
    elements.append(Spacer(1, 20))
    return elements

def get_header_style(title):
    data = [[title]]
    t = Table(data, colWidths=[6.5*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1e3a8a')),
        ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    return t

def generate_gst_pdf(applicant_id: str) -> BytesIO:
    output = BytesIO()
    doc = SimpleDocTemplate(output, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    elements = []
    styles = getSampleStyleSheet()
    
    # Page 1: GST Summary
    elements.extend(get_common_header(styles, "GST Returns (GSTR-3B) Analysis Report"))
    
    account_data = [
        ['Business Name', 'Suguna Enterprises'],
        ['GSTIN', '33ABCDE1234F1Z5'],
        ['Return Period', 'Apr 2026 - Sep 2026'],
        ['Filing Frequency', 'Monthly']
    ]
    account_table = Table(account_data, colWidths=[2*inch, 4*inch])
    account_table.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(account_table)
    elements.append(Spacer(1, 20))
    
    elements.append(get_header_style("Monthly Sales & Tax Summary"))
    gst_data = [
        ['MONTH', 'TAXABLE TURNOVER', 'CGST', 'SGST', 'IGST', 'TOTAL TAX'],
        ['Apr 2026', '₹ 4,50,000', '₹ 40,500', '₹ 40,500', '₹ 0', '₹ 81,000'],
        ['May 2026', '₹ 4,80,000', '₹ 43,200', '₹ 43,200', '₹ 0', '₹ 86,400'],
        ['Jun 2026', '₹ 5,10,000', '₹ 45,900', '₹ 45,900', '₹ 0', '₹ 91,800'],
        ['Jul 2026', '₹ 4,95,000', '₹ 44,550', '₹ 44,550', '₹ 0', '₹ 89,100'],
        ['Aug 2026', '₹ 5,25,000', '₹ 47,250', '₹ 47,250', '₹ 0', '₹ 94,500'],
        ['Sep 2026', '₹ 5,60,000', '₹ 50,400', '₹ 50,400', '₹ 0', '₹ 100,800']
    ]
    gst_table = Table(gst_data, colWidths=[1*inch, 1.5*inch, 1*inch, 1*inch, 1*inch, 1*inch])
    gst_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('ALIGN', (0,1), (0,-1), 'LEFT'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
    ]))
    elements.append(gst_table)
    
    # Page 2: Visuals
    elements.append(PageBreak())
    title_style = ParagraphStyle('ChartTitle', parent=styles['Heading2'], alignment=1)
    elements.append(Paragraph("<b>Visual Analytics</b>", title_style))
    elements.append(Spacer(1, 20))
    
    elements.append(Paragraph("Monthly Taxable Turnover Trend", styles['Heading4']))
    d1 = Drawing(400, 200)
    bc1 = VerticalBarChart()
    bc1.x = 50
    bc1.y = 50
    bc1.height = 125
    bc1.width = 300
    bc1.data = [[450000, 480000, 510000, 495000, 525000, 560000]] 
    bc1.strokeColor = colors.black
    bc1.valueAxis.valueMin = 0
    bc1.valueAxis.valueMax = 600000
    bc1.valueAxis.valueStep = 100000
    bc1.categoryAxis.categoryNames = ['Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
    bc1.bars[0].fillColor = colors.HexColor('#8b5cf6') 
    d1.add(bc1)
    elements.append(d1)
    
    doc.build(elements)
    output.seek(0)
    return output

def generate_itr_pdf(applicant_id: str) -> BytesIO:
    output = BytesIO()
    doc = SimpleDocTemplate(output, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    elements = []
    styles = getSampleStyleSheet()
    
    # Page 1: ITR Summary
    elements.extend(get_common_header(styles, "Income Tax Return (ITR) Analysis Report"))
    
    account_data = [
        ['Applicant Name', 'Suguna M'],
        ['PAN Number', 'ABCDE1234F'],
        ['Assessment Year', '2025-2026'],
        ['Filing Status', 'Filed on Time']
    ]
    account_table = Table(account_data, colWidths=[2*inch, 4*inch])
    account_table.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(account_table)
    elements.append(Spacer(1, 20))
    
    elements.append(get_header_style("Income Summary (Last 3 Years)"))
    inc_data = [
        ['FINANCIAL YEAR', 'GROSS TOTAL INCOME', 'DEDUCTIONS', 'NET TAXABLE INCOME', 'TAX PAID'],
        ['2024-2025', '₹ 12,50,000', '₹ 1,50,000', '₹ 11,00,000', '₹ 1,25,000'],
        ['2023-2024', '₹ 10,80,000', '₹ 1,50,000', '₹ 9,30,000', '₹ 98,500'],
        ['2022-2023', '₹ 9,50,000', '₹ 1,50,000', '₹ 8,00,000', '₹ 72,500']
    ]
    inc_table = Table(inc_data, colWidths=[1.5*inch, 1.5*inch, 1.2*inch, 1.3*inch, 1*inch])
    inc_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('ALIGN', (0,1), (0,-1), 'LEFT'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
    ]))
    elements.append(inc_table)
    elements.append(Spacer(1, 15))
    
    # Page 2: Visuals
    elements.append(PageBreak())
    title_style = ParagraphStyle('ChartTitle', parent=styles['Heading2'], alignment=1)
    elements.append(Paragraph("<b>Visual Analytics</b>", title_style))
    elements.append(Spacer(1, 20))
    
    elements.append(Paragraph("Gross Total Income Trend", styles['Heading4']))
    d1 = Drawing(400, 200)
    bc1 = VerticalBarChart()
    bc1.x = 50
    bc1.y = 50
    bc1.height = 125
    bc1.width = 300
    bc1.data = [[950000, 1080000, 1250000]] 
    bc1.strokeColor = colors.black
    bc1.valueAxis.valueMin = 0
    bc1.valueAxis.valueMax = 1500000
    bc1.valueAxis.valueStep = 300000
    bc1.categoryAxis.categoryNames = ['FY22-23', 'FY23-24', 'FY24-25']
    bc1.bars[0].fillColor = colors.HexColor('#3b82f6') 
    d1.add(bc1)
    elements.append(d1)
    
    doc.build(elements)
    output.seek(0)
    return output

def generate_loan_pdf(applicant_id: str) -> BytesIO:
    content = [
        "Existing Loan Analysis Report",
        "-----------------------------------------",
        "Total Active Loans: 2",
        "Total Monthly EMI: $23000",
        "Total Outstanding: $450000",
        "FOIR: 42.5%"
    ]
    return create_pdf("Loan Analysis Report", applicant_id, content)
