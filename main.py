import cv2
import numpy as np
import pytesseract

# 이미지 업로드
src = cv2.imread('img.png')

# Resize the image
scale_percent = 50  # adjust the scale factor as needed
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
src = cv2.resize(src, (width, height))

# 마우스 구역 지정
x, y, w, h = cv2.selectROI('src', src, False)

if w and h:
    roi = src[y:y + h, x:x + w]

    # Draw a rectangle around the selected ROI
    cv2.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Use Tesseract to extract text
    ocr = pytesseract.image_to_string(roi, lang='eng')

    # Find contours in the binary image (inverse of the text)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours around the detected text
    cv2.drawContours(src, contours, -1, (0, 0, 255), 1)

cv2.imshow('src', src)  # Show the original image with the rectangle and contours
cv2.imshow('captured', roi)
cv2.imwrite('test/captured.jpg', roi)

print("Detected Text:", ocr)

cv2.waitKey(0)
cv2.destroyAllWindows()
