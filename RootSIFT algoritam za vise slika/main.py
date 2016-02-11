# import potrebnih paketa
from rootsift import RootSIFT
import cv2
import glob
from matplotlib import pyplot as plt

#obrada test slike
def readFromFile(testImagePath):
  imgTest = cv2.imread(testImagePath)

  imgPath = 'data_images'
  testImagePath = 'test_images'

  detector = cv2.xfeatures2d.SIFT_create() 	#inicijalizacija detektora za kljucne tacke    
  extractor = cv2.xfeatures2d.SIFT_create()	#inicijalizacija ekstraktora preko koga cemo uzimati osobine slike - deskriptor

  rs = RootSIFT()

  #======================================================================
  #funkcija koja nalazi broj pozitivnih preklapanja kljucnih tacaka

  def findPosMatches(dscTest, dscData):
    pozPoklapanja = []
    
    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 100)

    flann = cv2.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(dscTest,dscData,k=2)
    
    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in xrange(len(matches))]
    
    #pozPoklapanja = []
    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
      if m.distance < 0.7*n.distance:
	matchesMask[i]=[1,0]
	pozPoklapanja.append(len(matchesMask[i]))
    x = len(pozPoklapanja)
	
    return x, matches, matchesMask
  #======================================================================    
  
  #obrada ucitane slike
  gray2 = cv2.cvtColor(imgTest, cv2.COLOR_BGR2GRAY)
  kptsTest = detector.detectAndCompute(gray2, None)
  (kptsTest, dscTest) = extractor.detectAndCompute(gray2, None)
  (kptsTest, dscTest) = rs.compute(gray2, kptsTest)

  #  inicijalizacija osnovnih parametara u koje cu smestati podatke one slike
  #  koja ima najvise pozitivnih poklapanja kljucnih tacaka
  maxBrojPozPoklapanja = 0
  kptsDataBest = []
  poklapanja = []
  slikaData = imgTest
  matchesMask = []

  #obrada slika iz dataseta

  for imgPath in glob.glob(folderPath + '/*.jpg'):
    imgData = cv2.imread(imgPath)
    gray1 = cv2.cvtColor(imgData, cv2.COLOR_BGR2GRAY)
    kptsData = detector.detectAndCompute(gray1, None)
    (kptsData, dscData) = extractor.detectAndCompute(gray1, None)
    (kptsData, dscData) = rs.compute(gray1, kptsData)

    brPozPoklapanjaSlike, matchesData, matchesMaskData = findPosMatches(dscTest, dscData)

    if brPozPoklapanjaSlike > maxBrojPozPoklapanja:	#ukoliko slika ima najvise pozitivnih poklapanja
      maxBrojPozPoklapanja = brPozPoklapanjaSlike		#ona postaje glavni kandidat za "pobednika"
      poklapanja = matchesData
      slikaData = imgData
      kptsDataBest = kptsData
      matchesMask = matchesMaskData

  print "Slika poklapanja:"

  draw_params = dict(matchColor = (0,255,0),
		    singlePointColor = (255,0,0),
		    matchesMask = matchesMask,
		    flags = 0)

  img3 = cv2.drawMatchesKnn(imgTest,kptsTest,slikaData,kptsDataBest,poklapanja,None,**draw_params)

  plt.imshow(img3,),plt.show()
  
  return img3, slikaData
