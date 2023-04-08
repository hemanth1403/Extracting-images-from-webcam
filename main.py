import cv2
import os
# print(os.getcwd())
os.mkdir("Images")
path = os.path.abspath("Images")
# print(path)
cap = cv2.VideoCapture(0)
c = 0
while True:
    success, frame = cap.read()
    if (c > 3):
        cv2.imwrite(f"{path}/{c-3}.jpg", frame)
    c += 1
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
