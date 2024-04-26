import threading
import cv2
from deepface import DeepFace

face_match = False


def check_face(frame, ref_img):
    """
    Args:
        frame (numpy.ndarray): The current frame from the video capture.
        ref_img (numpy.ndarray): The reference image for face comparison.

    Returns:
        bool: True if a face match is detected, False otherwise.

    Reference:
        https://youtu.be/FavHtxgP4l4?si=9YdtNPT_KpijM5Z4
    """
    global face_match
    try:
        if DeepFace.verify(frame, ref_img)['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False

    # return face_match


def face_recognition(img):
    """
    Continuously captures video frames, checks for face matches periodically,
    and returns True upon successful recognition.

    Args:
        img (str): Path to the reference image.

    Returns:
        bool: True if a face match is found, False otherwise.
    """

    cap = cv2.VideoCapture(0)
    ref_img = cv2.imread('face_reference/' + img)
    counter = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Check face every 30 frames for efficiency
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(), ref_img.copy())).start()
            except ValueError:
                pass

        counter += 1
        if face_match:
            cap.release()
            cv2.destroyAllWindows()
            return True
        else:
            cv2.putText(frame, "Not Match", (20, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

        cv2.namedWindow("LIVE", cv2.WINDOW_GUI_NORMAL)
        cv2.resizeWindow("LIVE", 640, 480)
        cv2.imshow("LIVE", frame)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    return False  # Indicate no face match found


# Example usage:
if __name__ == "__main__":
    img = "reference_img_1.jpg"
    if face_recognition(img):
        print("Face match detected!")
    else:
        print("No face match found.")
    # check_face(cv2.imread('face_reference/reference_img_1.jpg'), cv2.imread('face_reference/reference_img_3.jpg'))
    # print(face_match)
