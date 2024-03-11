import cv2
import numpy as np
from image_aligner import ImageRotator
from image_selector import ImageSelector


#Images = ImageSelector()
#Images.setSheet()
#Images.setScannedImage()

#original_image = Images.getOriginalImage()
#scanned_image = Images.getScannedImage()

original_image = "originals/5e_sheet_1.jpg"
scanned_image = "image 2.png"
    
rotator = ImageRotator(original_image, scanned_image)
rotated_image = rotator.setRotationImage()

cv2.imshow("Original Image", rotator.original_image)
cv2.imshow("Scanned Image", rotator.scanned_image)
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()