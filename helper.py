import pickle
from pathlib import Path

import cv2

def preprocess(img):
  
    img_resize = cv2.resize(img,(28,28))

    #Convert to reversed binary image (blank space contains value)
    threshold = 150
    binarized = 255 * (img_resize[:,:,0] < threshold)

    img_reshape = binarized.reshape(1,-1)
    return img_reshape



def load_model():
    PROJECT_PATH = Path(__file__).parent.resolve()
    MODEL_SAVEPATH = Path(PROJECT_PATH,'model')
    MODEL_NAME = "mnist_clf"
    FILENAME = Path(MODEL_SAVEPATH,MODEL_NAME+'.pickle')
    
    with open(FILENAME, 'rb') as f:
        model = pickle.load(f)
    return model