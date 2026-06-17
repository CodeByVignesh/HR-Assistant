from pypdf import PdfReader
import os

def read_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")
    
    reader = PdfReader(pdf_path)
    pdf_text = [page.extract_text() for page in reader.pages]
    return pdf_text