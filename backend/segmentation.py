import numpy as np
import cv2 as cv
import glob
import os
import imutils
import pandas as pd
from skimage import color,io 
from skimage.feature import local_binary_pattern
from PIL import Image

def Segmentation(img):

    imagem = "Imagem_Teste"
    
    
    METHOD = 'default'
    radius = 2
    n_points = 8 * radius

    data = []
    data_forma = []
    data_color = []

    mKeys = ['m00',
            'm10',
            'm01',
            'm20',
            'm11',
            'm02',
            'm30',
            'm21',
            'm12',
            'm03',
            'mu20',
            'mu11',
            'mu02',
            'mu30',
            'mu21',
            'mu12',
            'mu03',
            'nu20',
            'nu11',
            'nu02',
            'nu30',
            'nu21',
            'nu12',
            'nu03']

    columns = ['Area', 'Perimetro']+ mKeys + ['cx','cy','B','G',
    'R','H','S','V','L','A','D','LBP','I1','I2','I3','b','g','r','h','s','v','l','a','d','lbp','i1','i2','ir3','classe','imagem']
    columns_forma = ['Area', 'Perimetro']+ mKeys + ['cx','cy','classe','imagem']
    columns_color = ['B','G',
    'R','H','S','V','L','A','D','LBP','I1','I2','I3','b','g','r','h','s','v','l','a','d','lbp','i1','i2','i3','classe','imagem']



    
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    scale_percent = 60
    width = int(640)
    height = int(480)
    dim = (width, height)
    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img2 = gray.copy()
    img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    img_Lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
    img_lbp = local_binary_pattern(gray, n_points, radius, METHOD)
    ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

    kernel = np.ones((3,3),np.uint8)
    opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)

    sure_bg = cv.dilate(opening,kernel,iterations=3)

    dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
    ret, sure_fg = cv.threshold(dist_transform,0.5*dist_transform.max(),255,0)

    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg,sure_fg)
    ret, markers = cv.connectedComponents(sure_fg)

    markers = markers+1
    markers[unknown==255] = 0

    markers = cv.watershed(img,markers)
    img[markers == -1] = [255,0,0]
    arealist = []
    contours = []
    Mlist = []
        

    for marker in np.unique(markers):
        if marker == 0:
            continue
        mask = np.zeros(gray.shape, dtype="uint8")
        mask[markers == marker] = 255
        cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)        
        contours.append(cnts)
        for pic, contour in enumerate(cnts):
            area = cv.contourArea(contour)
            if (100<area<3000):
                

                x,y,w,h = cv.boundingRect(contour)
                mask = np.zeros(img2.shape,np.uint8)
                cv.drawContours(img, cnts, -1, (0, 255, 0), 2, 1)
                cv.drawContours(mask, cnts, 0, 255, -1)
                mean1 = cv.mean(img, mask = mask)
                mean2 = cv.mean(img_hsv, mask = mask)
                mean3 = cv.mean(img_Lab, mask = mask)
                mean4 = cv.mean(img_lbp, mask = mask)        

                B, G, R = mean1[0], mean1[1], mean1[2]
                H, S, V = mean2[0], mean2[1], mean2[2]
                L, A, D = mean3[0], mean3[1], mean3[2]
                LBP = mean4[0]
                        
                I1 = (1/3)*(R + G + B)
                I2 = (1/2)*(R - B)
                I3 = (1/4)*((-R) + 2*G - B)

                (mean01, std) = cv.meanStdDev(img, mask=mask)
                (mean02, std) = cv.meanStdDev(img_hsv, mask=mask)
                (mean03, std) = cv.meanStdDev(img_Lab, mask=mask)
                (mean04, std) = cv.meanStdDev(img_lbp, mask = mask)
                        
                b, g, r = float(mean01[0]), float(mean01[1]), float(mean01[2])
                h, s, v = float(mean02[0]), float(mean02[1]), float(mean02[2])
                l, a, d = float(mean03[0]), float(mean03[1]), float(mean03[2])
                lbp = float(mean04[0])

                i1 = (1/3)*(r + g + b)
                i2 = (1/2)*(r - b)
                i3 = (1/4)*((-r) + 2*g - b)
                        

                arealist.append(area)
                perimetro = cv.arcLength(contour, True)
                M = cv.moments(contour)
                Mlist.append(M)
                if M["m00"] != 0:
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                else:
                    cx, cy = 0, 0
                centroide = (cx,cy)

                      
                classe = "TESTE"
                data.append([area, perimetro]+ [M[key] for key in mKeys] + [cx,cy] + \
                       [B,G,R]+[H,S,V]+[L,A,D]+[LBP]+[I1,I2,I3]+[b,g,r]+[h,s,v]+[l,a,d]+[lbp]+[i1,i2,i3]+ [classe]+ [imagem])
                data_forma.append([area, perimetro]+ [M[key] for key in mKeys] + [cx,cy]+ [classe]+ [imagem])
                data_color.append([B,G,R]+[H,S,V]+[L,A,D]+[LBP]+[I1,I2,I3]+[b,g,r]+[h,s,v]+[l,a,d]+[lbp]+[i1,i2,i3]+[classe]+ [imagem])
    df = pd.DataFrame(data,columns=columns)

    return df