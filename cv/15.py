import cv2 
import numpy as np 
# Load images 
img1 = cv2.imread(r"C:\Users\venka\OneDrive\Pictures\Saved Pictures\windows-11-dark-mode-blue-stock-official-3840x2400-5630.jpg") 
img2 = cv2.imread(r"C:\Users\venka\OneDrive\Pictures\Saved Pictures\OIP.jpg") 
img3 = cv2.resize(img1,(300,300))
img4 = cv2.resize(img2,(300,300))
# Define corresponding points 
pts1 = np.array([[50, 50], [200, 50], [50, 200], [200, 200]]) 
pts2 = np.array([[100, 100], [300, 100], [100, 300], [300, 300]]) 
# Estimate projective transformation matrix using DLT 
H, _ = cv2.findHomography(pts1, pts2) 
# Apply projective transformation to img1 
dst = cv2.warpPerspective(img1, H, (img4.shape[1], img4.shape[0]))

# Display images 
cv2.imshow('img1', img3) 
cv2.imshow('img2', img4) 
cv2.imshow('dst', dst) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
