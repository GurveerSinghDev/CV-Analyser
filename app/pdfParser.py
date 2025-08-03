import fitz  # PyMuPDF
import sys

#.\venv\Scripts\Activate 
#enter in terminal, to enter VE
#Deactivate to Exit

def parsePdf(pdfPath):
    """Extracts text from a PDF file."""

    doc= fitz.open(pdfPath)#opens pdfs
    fText= [] #empty list to store texts from pages

    for pageNum, page in enumerate(doc, start=1): #loops thorugh each page in the document
        text = page.get_text()  #extract text from the page
        fText.append(f"--- Page {pageNum} ---\n{text.strip()}\n")  #adds extrcated text with pNum

    return "\n".join(fText)  #join all text with newlines







#this part runs only when the file is executed directly, not when it’s imported

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app/pdfParser.py path/to/your.pdf")
        sys.exit(1)

    pdfPath = sys.argv[1]  #get pdf path from command line argument

    try:
        output = parsePdf(pdfPath)  #call parsePdf function
        print(output)
    except Exception as e:
        print(f"An error occurred while parsing the PDF: {e}")
   
