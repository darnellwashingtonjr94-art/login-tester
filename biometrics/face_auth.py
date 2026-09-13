import cv2
import face_recognition

def verify_face(config):
    ref_path = config.get("biometrics_config", {}).get("reference_face")
    if not ref_path:
        print("Reference face path not configured.")
        return False

    # Load reference image and encode
    ref_image = face_recognition.load_image_file(ref_path)
    ref_encodings = face_recognition.face_encodings(ref_image)
    if not ref_encodings:
        print("No face detected in reference image.")
        return False
    ref_encoding = ref_encodings[0]

    # Capture frame from webcam
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    video_capture.release()

    if not ret:
        print("Failed to access camera for facial recognition.")
        return False

    # Find faces in current frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_encodings = face_recognition.face_encodings(rgb_frame)

    for face_encoding in face_encodings:
        match = face_recognition.compare_faces([ref_encoding], face_encoding, tolerance=0.6)
        if match[0]:
            print("Face authentication successful.")
            return True

    print("Face authentication failed.")
    return False
