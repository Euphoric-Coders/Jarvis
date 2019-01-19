#object detection
import cv2
from imageai.Detection import ObjectDetection


def Capture_cam():
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    return_img, img = camera.read()
    cv2.imwrite("img.jpg", img)
    del(camera)
while True:
    object_detect = 
