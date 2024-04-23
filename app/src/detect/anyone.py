import cv2


def detect():
    face_cascade = cv2.CascadeClassifier("public/haarcascade_frontalface_default.xml")

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4, minSize=(100, 100))

        color_green = (0, 255, 0)

        for x, y, w, h in faces:
            cv2.rectangle(
                frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color_green, 1
            )

            cv2.putText(
                frame,
                "Face",
                (x, y - 16),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (255, 255, 255),
                5,
            )
            cv2.putText(
                frame, "Face", (x, y - 16), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2
            )
            print(w)

        cv2.imshow("frame", frame)
        if cv2.waitKey(50) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect()
