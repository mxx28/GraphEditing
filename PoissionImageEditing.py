import cv2
import numpy as np

# Read images : src image will be cloned into dst
bkg = cv2.imread("C:\\Users\\mxx\\Desktop\\FILE\\Study\\OUT\\Graph editing\\Poisson Image Editing\\bkg.jpg")
src1 = cv2.imread("C:\\Users\\mxx\\Desktop\\FILE\\Study\\OUT\\Graph editing\\Poisson Image Editing\\src1.jpg")
src2 = cv2.imread("C:\\Users\\mxx\\Desktop\\FILE\\Study\\OUT\\Graph editing\\Poisson Image Editing\\src2.jpg")

# # Reshape
# src1 = cv2.resize(src1, dsize=None, fx=1.5, fy=1.5)
# src2 = cv2.resize(src2, dsize=None, fx=1.5, fy=1.5)

# Read mask
src1_mask = cv2.imread("C:\\Users\\mxx\\Desktop\\FILE\\Study\\OUT\\Graph editing\\Poisson Image Editing\\src1_mask.jpg")
src2_mask = cv2.imread("C:\\Users\\mxx\\Desktop\\FILE\\Study\\OUT\\Graph editing\\Poisson Image Editing\\src2_mask.jpg")
# src1_mask = src1_mask[:, :, 0]
# src2_mask = src2_mask[:, :, 0]

# The location of the src in the dst
width, height, channels = bkg.shape
loc_1 = (int(height/3), int((width*2) / 3))
loc_2 = (int((height*2) / 3), int(width/3))

# Seamlessly clone src with normal_clone
normal_clone_1 = cv2.seamlessClone(src1, bkg, src1_mask, loc_1, cv2.NORMAL_CLONE)
normal_clone_2 = cv2.seamlessClone(src2, normal_clone_1, src2_mask, loc_2, cv2.NORMAL_CLONE)

# Seamlessly clone src with normal_clone
mixed_clone_1 = cv2.seamlessClone(src1, bkg, src1_mask, loc_1, cv2.MIXED_CLONE)
mixed_clone_2 = cv2.seamlessClone(src2, normal_clone_1, src2_mask, loc_2, cv2.MIXED_CLONE)

# Write results
cv2.imwrite("C:\\Users\\mxx\\Desktop\\FILE\\Study\\OUT\\Graph editing\\Poisson Image Editing\\opencv-normal-clone-example.jpg", normal_clone_2)
cv2.imwrite("C:\\Users\\mxx\\Desktop\\FILE\\Study\\OUT\\Graph editing\\Poisson Image Editing\\opencv-mixed-clone-example.jpg", mixed_clone_2)

# Reference:
# https://zhuanlan.zhihu.com/p/453095752
# https://www.cnblogs.com/3-louise-wang/p/16671316.html
# https://zhuanlan.zhihu.com/p/68349210
