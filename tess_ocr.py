from PIL import ImageGrab, Image
import pyperclip
import pytesseract


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

def main():
    in_lang = input("Pick a language \n1=English 2=Japanese 3=Simplified_Chinese:").strip()
    
    while True:
        if in_lang == "1":
            lang = "eng"
            break
        elif in_lang == "2":
            lang = "jpn"
            break
        elif in_lang == "3":
            lang = "chi_sim"
            break
        else:
            print("incorrect input")
            in_lang = input("Pick a language \n1=English 2=Japanese 3=Simplified Chinese:")

    img = check_clipboard_for_image()

    if img is not None:
        ocr_result = pytesseract.image_to_string(img, lang)
        pyperclip.copy(ocr_result)
        print("OCR Result:")
        ocr_result = ocr_result.replace('\xa9', ' (copyright) ')
        print(ocr_result)
        input("Press enter to exit.")

    else:
        print("No image in the clipboard.")
        input("Press enter to exit.")

if __name__ == "__main__":
    main()
