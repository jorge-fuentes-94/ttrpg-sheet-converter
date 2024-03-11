import cv2
import numpy as np

class ImageRotator:
    def __init__(self, original_image_path, scanned_image_path):
        self.original_image = cv2.imread(original_image_path)
        self.scanned_image = cv2.imread(scanned_image_path)
        self.rotation_angle = None

    def _findRotationImage(self):
        orb = cv2.ORB_create()
        gray_original = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        gray_scanned = cv2.cvtColor(self.scanned_image, cv2.COLOR_BGR2GRAY)
        keypoints1, descriptors1 = orb.detectAndCompute(gray_original, None)
        keypoints2, descriptors2 = orb.detectAndCompute(gray_scanned, None)
        matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
        matches = matcher.match(descriptors1, descriptors2, None)
        matches = sorted(matches, key=lambda x: x.distance)
        good_matches = matches[:50]
        source_points = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        distance_pointss = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        homography_matrix, _ = cv2.findHomography(source_points, distance_pointss, cv2.RANSAC, 5.0)
        angle_rad = -np.arctan2(homography_matrix[0, 1], homography_matrix[0, 0])
        rotation_angle = np.degrees(angle_rad)
        return rotation_angle

    def setRotationImage(self):
        if self.rotation_angle is None:
            self.rotation_angle = self._findRotationImage()
        height, width = self.scanned_image.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), self.rotation_angle, 1)
        rotated_image = cv2.warpAffine(self.scanned_image, rotation_matrix, (width, height))
        return rotated_image


