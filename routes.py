from pathlib import Path

from fastapi import FastAPI, File, UploadFile
from typing import List
from apps.files.Uploader import ImageUploader

app = FastAPI()


@app.post("/images")
async def images(user_images: List[UploadFile] = File(...)):
    uploader = ImageUploader()
    uploaded_files = []
    for image in user_images:
        uploaded_files.append(
            uploader.save_file(
                Path(image.filename),
                image.file
            )
        )

    return {"uploaded_files": uploaded_files}
