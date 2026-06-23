from fastapi import File, HTTPException, UploadFile, status

from app.core.utils.file import is_allowed_extension


def get_ocr_validated_file(file: UploadFile = File(...)):
    ALLOWED_EXTENSIONS = ('jpg', 'jpeg', 'png', 'pdf')

    if not is_allowed_extension(file.filename, ALLOWED_EXTENSIONS):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unsupported file type")

    return file