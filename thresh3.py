import cv2
import numpy as np
from matplotlib import pyplot as plt
#import necessary packages

img = cv2.imread('Image 11.JPG',0)#read image

ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)#apply threshold


titles = ['Original Image','TRUNC']#Apply titles
images = [img, thresh3]

for i in xrange(2):#Apply for loop
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()#show Image
