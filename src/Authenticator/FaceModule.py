import threading
import cv2
from deepface import DeepFace

class Biometric:

    def __init__(self):
        self.ref_img_path = "../assets/face_reference/"
        self.ref_img = cv2.imread(self.ref_img_path)

    def check_face(self, frame):
        try:
            return DeepFace.verify(frame, self.ref_img)['verified']
        except ValueError:
            print("Error during DeepFace verification")
            return False

    def verify(self):
        cap = cv2.VideoCapture(0)
        counter = 0
        face_match = False

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if counter % 30 == 0:  # Check face every 30 frames for efficiency
                face_match = self.check_face(frame.copy())
                if face_match:
                    break

            counter += 1
            cv2.putText(frame, "Not Match" if not face_match else "Matching...", (20, 450), cv2.FONT_HERSHEY_PLAIN, 2,
                        (0, 0, 255), 3)

            cv2.namedWindow("LIVE", cv2.WINDOW_GUI_NORMAL)
            cv2.resizeWindow("LIVE", 640, 480)
            cv2.imshow("LIVE", frame)
            key = cv2.waitKey(1)
            if key == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
        return face_match  # Indicate face match result

    def create(self, count):
        cap = cv2.VideoCapture(0)
        filename = self.ref_img_path + "reference_img_" + count + ".jpg"

        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imshow('Webcam Feed', frame)

                # Press 's' to save the image
                if cv2.waitKey(1) == ord('s'):
                    cv2.imwrite(filename, frame)
                    print(f"Image saved at {filename}")
                    break
            else:
                break
        cap.release()

        img = cv2.imread(filename)
        cv2.putText(img, "Saved! Press q to quit ", (20, 450), cv2.QT_FONT_NORMAL, 1, (0, 255, 0))
        cv2.imshow("Saved", img)
        if cv2.waitKey(0) == ord("q"):
            cv2.destroyAllWindows()