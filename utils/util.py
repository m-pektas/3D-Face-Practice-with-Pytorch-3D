import numpy as np
import pickle

def readpkls(path):
    with open(path, 'rb') as f:
        db = pickle.load(f)
                
    return db

def get5landmarksFrom68Landmarks( landmark):
        # landmark=np.array(landmark).squeeze(0)
        left_eye = np.array([36, 37, 38, 39, 40, 41])
        right_eye = np.array([42, 43, 44, 45, 46, 47])
        left_eye_center = np.mean(landmark[left_eye], axis=0)
        right_eye_center = np.mean(landmark[right_eye], axis=0)

        leftEyeX, leftEyeY = left_eye_center[0], left_eye_center[1]
        rightEyeX, rightEyeY = right_eye_center[0], right_eye_center[1]
        noseX, noseY = landmark[30][0],  landmark[30][1]
        rightMouthX, rightMouthY = landmark[54][0],  landmark[54][1]
        leftMouthX, leftMouthY = landmark[48][0],  landmark[48][1]

        affine_points = [[leftEyeX, leftEyeY], [rightEyeX, rightEyeY], [noseX, noseY], [leftMouthX, leftMouthY],
                            [rightMouthX, rightMouthY]]
        return np.array(affine_points).astype(np.float32)
