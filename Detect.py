#object detection
import cv2
from imageai.Detection import ObjectDetection
import os


def Capture_cam():
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    return_img, img = camera.read()
    cv2.imwrite("img.jpg", img)
    del(camera)
def Detect():
    exec_path = os.getcwd()
    
    object_detect = ObjectDetection()
    object_detect.setModelTypeAsRetinaNet()
    object_detect.setModelPath( os.path.join(exec_path, "model.h5"))
    object_detect.loadModel()
    detections = object_detect.detectObjectsFromImage(input_image=os.path.join(exec_path, "img.jpg"), output_image_path=os.path.join(exec_path, "imgnew.jpg"))

    for Object in detections:
        print(Object["name"], Object["percentage_probability"],Object["box_points"])


    
 
