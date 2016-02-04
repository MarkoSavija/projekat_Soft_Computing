# import potrebnih paketa
import numpy as np
import cv2
 
class RootSIFT:
  def __init__(self):
    # initialize the SIFT feature extractor
    self.extractor = cv2.xfeatures2d.SIFT_create()

  def compute(self, image1, kps1, image2, kps2, eps=1e-7):
    # compute SIFT descriptors
    (kps1, descs1) = self.extractor.detectAndCompute(image1, None)
    (kps2, descs2) = self.extractor.detectAndCompute(image2, None)

    # if there are no keypoints or descriptors, return an empty tuple
    if len(kps1 or kp2) == 0:
      return ([], None)

    # apply the Hellinger kernel by first L1-normalizing and taking the
    # square-root
    descs1 /= (descs1.sum(axis=1, keepdims=True) + eps)
    descs1 = np.sqrt(descs1)

    descs2 /= (descs2.sum(axis=1, keepdims=True) + eps)
    descs2 = np.sqrt(descs2)
    
    # return a tuple of the keypoints and descriptors
    return (kps1, descs1, kps2, descs2) 
