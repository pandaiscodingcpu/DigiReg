import cv2 as cv
import joblib


'''
Users are required to bring the digit close to the camera.
This is the latest version of DigiReg -v 1.0.0 
completed on 13-08-2025 at 09:00 hrs

Next version will fix:-
1. Accuracy of the model (probably use of Neural network)
2. More convenient way of reading digits such as use of mobile phone in real time.

EXPECTED DATE FOR NEXT RELEASE -v 1.1: OCTOBER 15, 2025
'''
# Read and resize
# image = cv.imread()

image = cv.VideoCapture(0) # reading the live image

digireg = joblib.load('Digi_reg.pkl')
while True:
    ret,frame = image.read()

    img_resize = cv.resize(frame, (28, 28))

    # Convert to grayscale
    gray = cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)

    # Invert
    gray = cv.bitwise_not(gray)

    # Optional: Threshold to ensure clear digit
    _, gray = cv.threshold(gray, 128, 255, cv.THRESH_BINARY)

    # Flatten the image
    flat = gray.flatten().reshape(1, -1)

    # predict in real time
    predict_digit = digireg.predict(flat)

    # Show prediction on frame
    cv.putText(frame, f"Prediction: {predict_digit[0]}", (10, 40),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display video feed
    cv.imshow("Live Digit Recognition", frame)

    # Exit on 'q' key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

image.release()
cv.destroyAllWindows()
