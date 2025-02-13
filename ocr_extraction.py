import pytesseract
import cv2
from pdf2image import convert_from_path
import os

def extract_text_from_image(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    extracted_text = ""
    for img in images:
        text = pytesseract.image_to_string(img)
        extracted_text += text + "\n"
    return extracted_text

# Example usage
# print(extract_text_from_image("sample.jpg"))
# print(extract_text_from_pdf("sample.pdf"))
