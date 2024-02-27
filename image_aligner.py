import cv2
import numpy as np
import matplotlib.pyplot as plt

def loadReferenceSheet (game,language):
    referenceName = f"{game}_{language}_sheet.jpg"
    referenceImage = cv2.imread(referenceName, cv2.IMREAD_COLOR)
    referenceImage = cv2.cvtColor(referenceImage,cv2.COLOR_BGR2RGB)
    return referenceImage

def loadScanSheet(name):
    readName = name
    scanImage = cv2.imread (readName, cv2.IMREAD_COLOR)
    scanImage = cv2.cvtColor (scanImage, cv2.COLOR_BGR2RGB)
    return scanImage

def grayConverter(reference_image, scan_image):
    reference_image_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
    scan_image_gray = cv2.cvtColor(scan_image, cv2.COLOR_BGR2GRAY)
    return reference_image_gray,scan_image_gray

def keypointFinder (reference_image, scan_image):
    reference_image_gray, scan_image_gray = grayConverter(reference_image,scan_image)
    max_orbs = 500
    
    orb = cv2.ORB_create(max_orbs)
    keypoints_reference, descriptor_reference = orb.detectAndCompute(reference_image_gray, None)
    keypoints_scan, descriptor_scan = orb.detectAndCompute(scan_image_gray, None)
    
    return keypoints_reference, descriptor_reference, keypoints_scan, descriptor_scan

def keypointMatch (descriptor_reference, descriptor_scan):
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    image_matches = list(matcher.match(descriptor_reference,descriptor_scan, None))
    image_matches.sort(key=lambda x: x.distance, reverse = False)
    
    max_good_matches = int(len(image_matches)*0.1)
    
    image_matches = image_matches[:max_good_matches]
    
    return image_matches

def goodmatchesLocator (keypoints_reference, keypoints_scan, image_matches):
    points_reference = np.zeros((len(image_matches),2), dtype=np.float32)
    points_scan = np.zeros((len(image_matches),2), dtype=np.float32)
    
    for i, match in enumerate(image_matches):
        points_reference[i, :] = keypoints_reference[match.queryIdx].pt
        points_scan[i, :] = keypoints_scan[match.queryIdx].pt
        
    return points_reference,points_scan        
    
    
    
def findHomography (points_reference, points_scan):

    homography, mask = cv2.findHomography(points_scan,points_reference, cv2.RANSAC)
    print (homography)
    return homography

def imageWarper (reference_image, scan_image, keypoints_reference, keypoints_scan, image_matches):
    
    points_reference, points_scan = goodmatchesLocator(keypoints_reference,keypoints_scan, image_matches)
    homograpy = findHomography(points_reference, points_scan)
    
    height, width, channels = reference_image.shape
    scan_image_fixed = cv2.warpPerspective(scan_image, homograpy, (width, height))
    
    return scan_image_fixed


#functions to check result, delete at the end
reference_image = loadReferenceSheet("5e","english")
scan_image = loadScanSheet("original.jpg")
keypoints_reference, descriptor_reference, keypoints_scan, descriptor_scan = keypointFinder(reference_image,scan_image)

image_matches = keypointMatch (descriptor_reference,descriptor_scan)
scan_image_fixed = imageWarper(reference_image, scan_image, keypoints_reference, keypoints_scan, image_matches)

#check image
# plt.figure(figsize=[20, 10]); 
# plt.subplot(121); plt.axis('off'); plt.imshow(reference_image); plt.title("Original Form")
# plt.subplot(122); plt.axis('off'); plt.imshow(scan_image); plt.title("Scanned Form")
# plt.show()

# #check keypoints
# im1_display = cv2.drawKeypoints(reference_image, keypoints_reference, outImage=np.array([]), 
#                                 color=(255, 0, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# im2_display = cv2.drawKeypoints(scan_image, keypoints_scan, outImage=np.array([]), 
#                                 color=(255, 0, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# plt.figure(figsize=[20,10])
# plt.subplot(121); plt.axis('off'); plt.imshow(im1_display); plt.title("Original Form");
# plt.subplot(122); plt.axis('off'); plt.imshow(im2_display); plt.title("Scanned Form");
# plt.show()


# #check matches
# im_matches = cv2.drawMatches(reference_image, keypoints_reference, scan_image, keypoints_scan, image_matches, None)

# plt.figure(figsize=[40, 10])
# plt.imshow(im_matches);plt.axis("off");plt.title("Original Form")
# plt.show()

    
#check warp image
plt.figure(figsize=[20, 10])
plt.subplot(121);plt.imshow(reference_image);    plt.axis("off");plt.title("Original Form")
plt.subplot(122);plt.imshow(scan_image_fixed);plt.axis("off");plt.title("Scanned Form")
plt.show()