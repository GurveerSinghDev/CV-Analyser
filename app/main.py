from fastapi import FastAPI, File, UploadFile
from app.pdfParser import parsePdf
import shutil, os

app = FastAPI()

@app.post("/uploadpdf/")
async def upload_pdf(file: UploadFile = File(...)):
    temp_path = f"temp/{file.filename}" # creates a temporary filename
    with open(temp_path, "wb") as f:  
        shutil.copyfileobj(file.file, f)   # copies contents to a new temp file

    try:
        text = parsePdf(temp_path)
    except Exception as e:
        return {"error": str(e)}
    finally:
        os.remove(temp_path) # removes the temp file after processing

    return {"text": text}