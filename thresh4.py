import cv2
import numpy as np
from matplotlib import pyplot as plt
#import necessary packages

img = cv2.imread('Image 11.JPG',0)#read image

ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)#apply threshold


titles = ['Original Image','TOZERO']#Apply titles
images = [img, thresh4]

for i in xrange(2):#Apply for loop
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()#show Image
