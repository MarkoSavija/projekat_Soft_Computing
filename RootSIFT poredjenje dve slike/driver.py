# import potrebnih paketa
from rootsift import RootSIFT
import cv2
from matplotlib import pyplot as plt
 
# ucitavanje slike i pretvaranje u grayscale
image1 = cv2.imread("images/pe1.jpg")
image2 = cv2.imread("images/p2.jpg")

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
 
# detect Difference of Gaussian keypoints in the image
detector = cv2.xfeatures2d.SIFT_create()
kps1 = detector.detectAndCompute(gray1, None)
kps2 = detector.detectAndCompute(gray2, None)
 
# extract normal SIFT descriptors
extractor = cv2.xfeatures2d.SIFT_create()
(kps1, descs1) = extractor.detectAndCompute(gray1, None)
(kps2, descs2) = extractor.detectAndCompute(gray2, None)
print "SIFT: kps=%d, descriptors=%s " % (len(kps1), descs1.shape)
print "SIFT: kps=%d, descriptors=%s " % (len(kps2), descs2.shape)
 
# extract RootSIFT descriptors
rs = RootSIFT()
(kps1, descs1, kps2, descs2) = rs.compute(gray1, kps1, gray2, kps2)

print "RootSIFT: kps=%d, descriptors=%s " % (len(kps1), descs1.shape) 
print "RootSIFT: kps=%d, descriptors=%s " % (len(kps2), descs2.shape)
print "========================================================"
print "Slika poklapanja:"
print "========================================================"

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params,search_params)

matches = flann.knnMatch(descs1,descs2,k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in xrange(len(matches))]

# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
  if m.distance < 0.7*n.distance:
    matchesMask[i]=[1,0]

draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)

img3 = cv2.drawMatchesKnn(image1,kps1,image2,kps2,matches,None,**draw_params)

plt.imshow(img3,),plt.show()