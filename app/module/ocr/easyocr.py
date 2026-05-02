import easyocr

from fastapi import UploadFile

from app.core.utils.file import delete_file, save_file
from app.module.ocr.base import BaseEngine


class EasyOcr(BaseEngine):
    def __init__(self):
        self.ocr = easyocr.Reader(['ko', 'en'])


    async def recognize(self, file: UploadFile):
        file_path = await save_file(file)
        response = self.ocr.readtext(str(file_path))
        await delete_file(file_path)
        return self.convert_to_json(response)


    def convert_to_json(self, response):
        result = {
            "images": []
        }

        for poly, text, confidence in response:
            bounding_poly = [[int(vertex[0]), int(vertex[1])] for vertex in poly]
            result['images'].append({
                "boundingPoly": bounding_poly,
                "text": text,
                "confidence": float(confidence)
            })

        return result