#!/usr/bin/env python3
'''
cardboard detection from webcam image using keras retinanet
created by Antonius Ringlayer
'''
import cv2, os, time, keras
import numpy as np
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

class Boil:
    obj_num = 0
    x = 0
    y = 0
    def __init__(self, num, x, y, b):
        self.obj_num = num
        self.x = x
        self.y = y
        self.b = b

def get_session():
    config = tf.compat.v1.ConfigProto()
    config.gpu_options.allow_growth = True
    return tf.compat.v1.Session(config=config)

os.system(r"echo '' > C:\Users\sumov\OneDrive\Desktop\Boiling_Milk_Dataset\webcam.txt")
f = open(r"C:\Users\sumov\OneDrive\Desktop\Boiling_Milk_Dataset\webcam.txt", "a")
tf.compat.v1.keras.backend.set_session(get_session())
#model = models.load_model("/home/ringlayer/Desktop/app/retinanet1/models/resnet50_09.h5", backbone_name='resnet50')
model = models.load_model(r"C:\Users\sumov\OneDrive\Desktop\Boiling_Milk_Dataset\model.h5", backbone_name='resnet50')
#model = models.convert_model(model)
print(model.summary())
labels_to_names = {0: 'Boiled', 1: 'Steaming'}

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

while True:
    try:
        current_boil = 0
        box_lists = []
        ret, image = cap.read()
        draw = image.copy()
        draw = cv2.resize(draw,(640,480))
        draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)
        image = preprocess_image(image)
        image, scale = resize_image(image)
        start = time.time()
        boxes, scores, labels = model.predict(np.expand_dims(image, axis=0))

        boxes /= scale

        for box, score, label in zip(boxes[0], scores[0], labels[0]):
            if score < 0.5:
                break
            current_boil += 1
            color = label_color(label)
            b = box.astype(int)
            x = b[0]
            y = b[1]
            box_lists.append(Boil(current_boil, x, y, b))
            draw_box(draw, b, color=color)
            caption = "{} {:.3f}".format(labels_to_names[label], score)
            draw_caption(draw, b, caption)

        draw = cv2.cvtColor(draw, cv2.COLOR_RGB2BGR)
        cv2.imshow('framename', draw)
        if current_boil > 0:
            os.system("cls")
            str_data = "\n\n*******Record of Boiling Milk Data*******"
            for obj in box_lists:
                str_data += "\nMilk Boiled : " + str(obj.obj_num)
                print(obj.obj_num)
                    #print("The Milk is Boiled")
                str_data += "\ngot x : " + str(obj.x)
                str_data += "\ngot y : " + str(obj.y)
                str_data += "\nfull coordinate : " + str(obj.b)
                str_data += "\n"
                decision=str(caption[:4])
                
            f.write(str_data)
            print(str_data)
            if decision =='Boil':
                print('Milk is Boiled')
            
            #print(box_lists)
           
    except:
	    pass

    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
cap.release()
cv2.destroyAllWindows()

f.close()
