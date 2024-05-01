import cv2

sift = cv2.SIFT_create()

bf = cv2.BFMatcher(cv2.NORM_L2,crossCheck=True)

img1 = cv2.imread('../src/assets/face_reference/reference_img_1.jpg', 0)
# img2 = cv2.imread('face_reference/reference_img_2.jpg', 0)
cap = cv2.VideoCapture(0)

cv2.namedWindow("LIVE", cv2.WINDOW_NORMAL)
cv2.resizeWindow("LIVE", 640, 480)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    img2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    keypoints_1, desc_1 = sift.detectAndCompute(img1, None)
    keypoints_2, desc_2 = sift.detectAndCompute(img2, None)

    matches = bf.match(desc_1,desc_2)
    matches = sorted(matches,key = lambda x:x.distance)
    good_matches = matches[:20]

    print(len(good_matches))
    img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[300:600], None)

    cv2.imshow("LIVE", img3)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()









