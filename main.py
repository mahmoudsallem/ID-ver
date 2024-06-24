from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from utils import ID_verification
import tempfile
import shutil
import os


app = FastAPI()

@app.post("/verify")
async def verify_id(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    if not (file1 and file2):
        raise HTTPException(status_code=400, detail="Please upload both images.")

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            img1_path = os.path.join(temp_dir, file1.filename)
            img2_path = os.path.join(temp_dir, file2.filename)

            with open(img1_path, "wb") as f1, open(img2_path, "wb") as f2:
                shutil.copyfileobj(file1.file, f1)
                shutil.copyfileobj(file2.file, f2)

            result = ID_verification(img1_path, img2_path)
            return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))