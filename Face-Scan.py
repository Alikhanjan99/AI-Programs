import cv2

# Load the image and create a Haar cascade classifier
image = cv2.imread('image.jpg')
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Detect faces in the image
faces = classifier.detectMultiScale(image, scaleFactor=1.3, minNeighbors=5)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image with the detected faces
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
