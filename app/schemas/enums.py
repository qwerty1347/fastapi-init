from enum import Enum


class OcrEngine(str, Enum):
    easyocr = "easyocr"
    paddleocr = "paddleocr"
    clovaocr = "clovaocr"