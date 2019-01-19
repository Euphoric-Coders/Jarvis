import cv2
from imageai.Detection import ObjectDetection
import os

object_dictn = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train',
                7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter',
                13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant',
                21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie',
                28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite',
                34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket',
                39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl',
                46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog',
                53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed',
                60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard',
                67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator',
                73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier',
                79: 'toothbrush'}

exec_path = os.getcwd()
object_detect = ObjectDetection()
object_detect.setModelTypeAsRetinaNet()
object_detect.setModelPath( os.path.join(exec_path, "model.h5"))
object_detect.loadModel()
    
def Detect(file = "img.jpg"):
    detections = object_detect.detectObjectsFromImage(input_image=os.path.join(exec_path, file), output_image_path=os.path.join(exec_path, "clf.jpg"))
    values = []
    for Object in detections:
        nm = Object["name"]
        crds = Object["box_points"]
        prob = Object["percentage_probability"]
        pixel_dst = crds[2]-crds[1]
        data = [nm, pixel_dst]
        values.append(data)
    return values

#focus_list = [Pixel_width,Actual_dist, Actual_width ]
#object_dictionary = {}

def Dist(data = [["obj", "pxl_dst"]]):
    for each in data:
        obj, pxl_dst = each
        focus_list = object_dictionary[obj]
        focus = ((focus_list[0]*focus_list[1])/focus_list[2])
        distance = ((focus_list[2]*focus)/pxl_dst)
    return dist
