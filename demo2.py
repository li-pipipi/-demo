import cv2
import numpy as np

# 读取图像
img = cv2.imread('./saved_image.jpg')

# 图像缩放
resized_img = cv2.resize(img,(200,200))#将图像缩放为200x200
# 图像旋转
(h,w) = img.shape[:2] #获取图像的高和宽 :2表示取前两个元素，即高和宽
center = (w//2,h//2) #获取图像的中心点
M = cv2.getRotationMatrix2D(center,120,1.0)#旋转45度
rotated_img = cv2.warpAffine(img,M,(w,h)) #根据旋转矩阵进行旋转
# 图像平移
M = np.float32([[1,0,100],[0,1,50]]) #平移100，50
translated_img = cv2.warpAffine(img,M,(w,h))
# 图像翻转
flipped_img = cv2.flip(img,1) #水平翻转 1表示水平翻转，0表示垂直翻转，-1表示水平垂直翻转
# 显示图像
cv2.imshow('image0',img) #显示原始图像
cv2.imshow('image1',resized_img) #显示缩放后的图像
cv2.imshow('image2',rotated_img) #显示旋转后的图像
cv2.imshow('image3',translated_img) #显示平移后的图像
cv2.imshow('image4',flipped_img) #显示翻转后的图像
cv2.waitKey(0)
cv2.destroyAllWindows()