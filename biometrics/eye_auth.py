import cv2

def verify_eyes():
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    video_capture = cv2.VideoCapture(0)
    
    ret, frame = video_capture.read()
    video_capture.release()
    
    if not ret:
        print("Failed to capture frame for eye recognition.")
        return False

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(eyes) >= 2:
        print(f"Eye/Iris patterns detected: {len(eyes)}")
        return True
    
    print("Eye authentication failed: Insufficient eye patterns detected.")
    return False
