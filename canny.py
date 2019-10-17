import cv2
import numpy as np
import os
import glob

def ColumnExtract():
    files=glob.glob('columns/*.jpg')
    for f in files:
        os.remove(f)
    listt=[]
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.imread('pic.jpg',0)
    ret,thresh_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
    edges = cv2.Canny(img,100,250)
    kernel = np.ones((9,9),np.uint8)
    dilation = cv2.dilate(edges,kernel,iterations = 1)
    erosion = cv2.erode(dilation,np.ones((5,5),np.uint8),iterations = 3)

    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (7,8))
    morph_img = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel1)
    morph_img = cv2.dilate(morph_img,kernel,iterations = 2)

    im2, contours, hierarchy = cv2.findContours(morph_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[1] + cv2.boundingRect(ctr)[0] * img.shape[1] )
    for i,cnt in enumerate(sorted_ctrs):
        if np.size(cnt)>300:
            listt.append(cnt.shape[0])
            print((listt))
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            roi=img[y:y+h,x:x+w]
            
            cv2.putText(img,str((listt)),(x+50,y-3), font, .5,(0,0,0),1,cv2.LINE_AA)
            cv2.putText(img,str(len(listt)),(x+2,y-3), font, .5,(0,0,0),1,cv2.LINE_AA)
    ##        print((listt))
##            cv2.imshow('roi{}'.format(len(listt)),roi)
            cv2.imwrite(os.path.join('columns','roi{}.jpg'.format(len(listt)) ), roi)
    ##        print(x+w,x,y+h,y)
    cv2.imshow('img',img)
##    tts.OcrTTS()

    ##print(contours.shape)
##    cv2.imshow('img',img)
    ##cv2.imshow('erosion',erosion)
    ##cv2.imshow('morph_img',morph_img)
##ColumnExtract()
