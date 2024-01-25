import cv2, json, numpy as np
image = cv2.imread("main2.jpg", cv2.IMREAD_GRAYSCALE)

list = image.tolist()
string = json.dumps(list)

list2 = json.loads(string)
image2 = np.array(list2, dtype=np.uint8)

cv2.imshow("Image", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()