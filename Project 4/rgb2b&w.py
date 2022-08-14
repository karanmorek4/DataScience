import cv2

image = cv2.imread("img.png")
cv2.namedWindow("Input", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Input", 650, 800)
cv2.imshow("Input", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

invert = 255 - gray

blur = cv2.GaussianBlur(invert, (21, 21), 0)

invert_blur = 255 - blur
sketch = cv2.divide(gray, invert_blur, scale=256)

cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Output", 650, 800)
cv2.imshow("Output", sketch)
cv2.waitKey(0)