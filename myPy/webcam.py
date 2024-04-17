import cv2

def get_webcam(): 
    try:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("C:\\Min\\webcam.png", frame)
        cap.release()
    
    except Exception as e:
        pass
