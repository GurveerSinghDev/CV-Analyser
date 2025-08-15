from fastapi import FastAPI, File, UploadFile
from app.pdfParser import parsePdf
import shutil, os

app = FastAPI()

@app.post("/uploadpdf/")
async def upload_pdf(file: UploadFile = File(...)):
    upload_dir = "temp"
    os.makedirs(upload_dir, exist_ok=True)  #ensure the temp directory exists

    temp_path = os.path.join(upload_dir, file.filename)  #creates a temporary filename

    try:
        with open(temp_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        text = parsePdf(temp_path)

    except Exception as e:            #error handling
        return {"error": str(e)}

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return {"text": text}
   