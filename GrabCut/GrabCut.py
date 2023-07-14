import cv2
import numpy as np

# Load the image
src = cv2.imread("C:\\Users\\mxx\\Desktop\\src2.jpg")
src = cv2.resize(src, None, fx=1/4, fy=1/4)

# Create mask
mask = np.zeros(src.shape[:2], np.uint8)

# Set the parameters for GrabCut
bgd = np.zeros((1, 65), np.float64)
fgd = np.zeros((1, 65), np.float64)

r = cv2.selectROI('selectROI', src, False, None)
rec = (r[0], r[1], r[0]+r[2], r[1]+r[3])

cv2.grabCut(src, mask, rec, bgd, fgd, 10, cv2.GC_INIT_WITH_RECT)

# The result is stored in 'mask' with only (0, 1, 2, 3) value
# np.where() use | and  & when we have multiple conditions! Not OR!!
mask2 = np.where((mask == 0) | (mask == 2), 0, 1).astype(np.uint8)

# NEED TO ADD AN AXIS!!!!!!!
result = src * mask2[:, :, np.newaxis]
cv2.imshow('origin', src)
cv2.imshow('result', result)
cv2.waitKey()
cv2.destroyAllWindows()
