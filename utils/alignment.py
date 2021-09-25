import os
import numpy as np
from skimage import transform as trans
import cv2
import pickle
from utils import *


class Align:
    def __init__(self):
        self.similarity_transform = trans.SimilarityTransform()
        self.celeba_lms = {"points":np.array([[ 97.085625, 121.54979 ],
                                        [160.92938 , 121.21385 ],
                                        [128.3122  , 160.9326  ],
                                        [100.78094 , 184.17479 ],
                                        [155.54657 , 185.06541 ]], dtype=float), 
                     "shape" :tuple((np.array([256,256])).astype(int))}

    def align (self, x, y, num=68):
        if num==68:
            x = get5landmarksFrom68Landmarks(x)
            y = get5landmarksFrom68Landmarks(y)

        self.similarity_transform.estimate(y,x)
        M = self.similarity_transform.params[0:2, :]
        return M

    def trans_points2d(self, pts, M):
        new_pts = np.zeros(shape=pts.shape, dtype=np.float32)
        for i in range(pts.shape[0]):
            pt = pts[i]
            new_pt = np.array([pt[0], pt[1], 1.], dtype=np.float32)
            new_pt = np.dot(M, new_pt)
            new_pts[i] = new_pt[0:2]

        return new_pts
    
    def align2celeb(self, img, lms68):
        lms5 = get5landmarksFrom68Landmarks(lms68)
        self.similarity_transform.estimate(lms5, self.celeba_lms["points"])
        M = self.similarity_transform.params[0:2, :]
        aligned = cv2.warpAffine(img, M, self.celeba_lms["shape"] )
        return aligned, M

