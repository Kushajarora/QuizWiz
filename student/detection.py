import cv2

# Initialize the face and eye classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
class CameraStream:
    def __iter__(self):
# Initialize the webcam
        print("hello")
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            # Flag to check if the face is detected
            face_detected = False

            for (x, y, w, h) in faces:
                # Draw a rectangle around the detected face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                # Set the flag to indicate that the face is detected
                face_detected = True

                # Crop the region of interest for the eyes
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                # Detect eyes within the region of interest
                eyes = eye_cascade.detectMultiScale(roi_gray)

                for (ex, ey, ew, eh) in eyes:
                    # Draw rectangles around the detected eyes
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            # Display warning if face is not detected or both face and eyes are not on the screen
            if not face_detected or len(faces) == 0:
                cv2.putText(frame, "WARNING: Look at the screen!", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            #cv2.imshow('Frame', frame)

            #if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
        cap.release()
# cv2.destroyAllWindows()
