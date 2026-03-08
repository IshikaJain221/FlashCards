from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extract and return all text from a PDF file as a single string."""
    try:
        reader = PdfReader(pdf_path)
        all_text = []

        for page_num, page in enumerate(reader.pages, start=1):
            text = page.extract_text()
            if text:
                all_text.append(text)
            else:
                print(f"Warning: No text found on page {page_num}.")

        return "\n".join(all_text)

    except FileNotFoundError:
        print(f"Error: File not found at path: {pdf_path}")
        return ""
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""