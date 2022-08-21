import cv2

def detect_black_circle(image_path):
    image = cv2.imread(image_path,0)
    img = cv2.GaussianBlur(image,(21, 21),cv2.BORDER_DEFAULT)
    detected_circles = cv2.HoughCircles(img, 
                       cv2.HOUGH_GRADIENT, 0.9, 120, param1 = 50,
                       param2 = 35, minRadius = 30, maxRadius = 70)
    if detected_circles is not None:
        return True
    return detected_circles
