import cv2

def list_available_cameras():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

available_cameras = list_available_cameras()
print("Available camera indices:", available_cameras)

for i in available_cameras:
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera index {i} is working.")
        cap.release()
    else:
        print(f"Camera index {i} is not working.")
