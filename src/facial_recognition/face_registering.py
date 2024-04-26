import cv2


def add_face(count):
    cap = cv2.VideoCapture(0)
    filename = "face_reference/reference_img_" + count + ".jpg"

    if not cap.isOpened():
        print("Error opening webcam!")
        exit()

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


# Example Usage
if __name__ == "__main__":
    add_face("3")
