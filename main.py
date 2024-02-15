import cv2, json, numpy as np, sqlite3 as sql, os
from src.make_db import makeDB, insertData
from src.detect import anyone


def main():
    if not os.path.exists("face-recognition.db"):
        makeDB.init()
        insertData.init()

    anyone.detect()

    image = cv2.imread("main2.jpg", cv2.IMREAD_GRAYSCALE)

    list = image.tolist()
    string = json.dumps(list)

    list2 = json.loads(string)
    image2 = np.array(list2, dtype=np.uint8)

    cv2.imshow("Image", image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # cv2.imdecode(np.fromstring(string, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)


if __name__ == "__main__":
    main()
