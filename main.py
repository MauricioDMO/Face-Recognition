import cv2, json, numpy as np, sqlite3 as sql, os
from src.make_db import makeDB

def main():
  if not os.path.exists("face-recognition.db"):
    makeDB.init()
    
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

if __name__ == "__main__":
  main()