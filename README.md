# Extracting license plate content with OpenCV
---
-Our program extracts and displays letters and numbers on overseas license plates.
-Who participated: 양수겸, 서우석, 지승민, 이현우

**Packages Used**
---
cv2, pytesseract, num py (need install)

**How to execute**
---
1. Enter the address by selecting the desired license plate image
2. Drag the desired part of the image file and extract the letters and numbers of that part.
3. The borders of the letters are recognized
4. Convert boundies of the letters to text
5. Check the car's affiliation or number on the license plate and boundaries of the letters

**Results**
---
*Results may not be accurate depending on the state of the image file.

![car plate img1](https://github.com/SuGyeomY/Convert-handwriting-to-text/blob/main/Result_image/1.png?raw=true)
![car plate r1](https://github.com/SuGyeomY/Convert-handwriting-to-text/blob/main/Result_image/1-1.png?raw=true)
![car plate img2](https://github.com/SuGyeomY/Convert-handwriting-to-text/blob/main/Result_image/2.png?raw=true)
![car plate r2](https://github.com/SuGyeomY/Convert-handwriting-to-text/blob/main/Result_image/2-2.png?raw=true)
![car plate img3](https://github.com/SuGyeomY/Convert-handwriting-to-text/blob/main/Result_image/3.png?raw=true)
![car plate r3](https://github.com/SuGyeomY/Convert-handwriting-to-text/blob/main/Result_image/3-1.png?raw=true)

**Reference**
---
Text detection by python : 
<https://hemon.tistory.com/75>
<https://yunwoong.tistory.com/75>
