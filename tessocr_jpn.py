

from PIL import ImageGrab, Image
import pyperclip
import pytesseract
from googletrans import Translator


def check_clipboard_for_image():

    try:
        screenshot = ImageGrab.grabclipboard()
        if screenshot:
            return screenshot
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def trans_jp_to_eng(text):
    translator = Translator()
    translated_text = translator.translate(text, src='ja', dest='en')
    return translated_text.text

def main():
    lang = "jpn"

    img = check_clipboard_for_image()

    if img is not None:
        ocr_result = pytesseract.image_to_string(img, lang)
        pyperclip.copy(ocr_result)
        print("OCR Result:")
        ocr_result = ocr_result.replace('\xa9', ' (copyright) ')
        print(ocr_result)
        ocr_result = pyperclip.paste()
        english_text = trans_jp_to_eng(ocr_result)
        print(english_text)
        pyperclip.copy(english_text)

        input("Press enter to exit.")

    else:
        print("No image in the clipboard.")
        input("Press enter to exit.")

if __name__ == "__main__":
    main()
