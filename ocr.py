import pytesseract
import cv2

def preprocess_ocr_text(text):
    text = text.lower().replace("\n"," ").strip()
    return text

def get_name_fom_image(img_path, tesseract_file_path="C:/Program Files/Tesseract-OCR/tesseract.exe", preprocess_text_function=preprocess_ocr_text):
    
    img = cv2.imread(img_path)
    pytesseract.pytesseract.tesseract_cmd = tesseract_file_path
#     img = subimg(img, u=0.7)

    # Convert the image to gray scale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    # Performing OTSU threshold 
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY) 

    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 

    # Appplying dilation on the threshold image 
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1) 
    # dilation = thresh1

    # Finding contours 
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  
                                                     cv2.CHAIN_APPROX_NONE) 

    # Creating a copy of image 
    im2 = img.copy() 
    text = None
    for cnt in contours: 
        x, y, w, h = cv2.boundingRect(cnt) 

        # Drawing a rectangle on copied image 
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2) 

        # Cropping the text block for giving input to OCR 
        cropped = im2[y:y + h, x:x + w] 

        # Apply OCR on the cropped image 
        text = pytesseract.image_to_string(cropped)
        text = preprocess_text_function(text)

    return text
