import cv2
img = cv2.imread(r"C:\Users\venka\OneDrive\Pictures\Saved Pictures\vehicles_images_.jpg")
x, y = 100, 100
width, height = 200, 150
roi = img[y:y+height, x:x+width]
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
