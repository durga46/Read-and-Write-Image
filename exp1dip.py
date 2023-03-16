#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
cat_img = cv2.imread('cat.jpg',1)
cv2.imshow('cat1',cat_img)
cv2.waitKey(0)
destroyAllWindows()

# To write the image

cv2.imwrite('new image.jpg',cat_img)

# Find the shape of the Image

print(cat_img.shape))

# To access rows and columns
import random
for i in range(100):
    for j in range(cat_img.shape[1]):
       cat_img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow('Cat1',cat_img)
cv2.waitKey(0)
destroyAllWindows()

# To cut and paste portion of image
import cv2
cat_img = cv2.imread('cat.jpg',-1)
tag = cat_img[300:400,300:400]
cat_img[50:150,50:150] = tag
cv2.imshow('Cat1',cat_img)
cv2.waitKey(0)
destroyAllWindows()


# In[ ]:





# In[ ]:




