import cv2
import os
import tts
import canny
import tessOCR

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    frame=cv2.flip(frame,-1)
    cv2.imshow("OCR window", frame)
    
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
##        print("Image captured")
        cv2.imwrite('pic.jpg', frame)
        canny.ColumnExtract()
        
        
        try:
            os.remove('audio.mp3')
            os.remove('pic.jpg')
        except:
            os.remove('pic.jpg')
            pass
    elif k%256 == 114 or k%256 == 82:
        print('r pressed')
        tts.OcrTTS()
        tessOCR.EmptyList()
        
        
        
        
        

cam.release()

cv2.destroyAllWindows()