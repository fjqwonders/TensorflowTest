import tensorflow as tf
import time
import matplotlib.pyplot as plt
from image_processing import image_preprocessing
import csv

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('train_file','D:\ProgramData\PycharmProjects\Test03\list.csv','train file path')
sess = tf.Session()

def load_data(train_file):
    data = []
    i = 0
    files = []
    labels = []
    start_time = time.time()
    with open(train_file,"r") as fr:
        for line in fr.readlines():
            infos = line.split(",")
            data.append({"filename": infos[0],"label_name": int(infos[1]),})
    return data

def distorted_inputs():
    data = load_data(FLAGS.train_file)

    filenames = [ d['filename'] for d in data ]
    label_indexes = [ d['label_name'] for d in data ]
    sess.run(tf.global_variables_initializer())
    x=0

    for i in filenames:
        x+=1
        file_contents = tf.read_file(i)
        image_read = tf.image.decode_jpeg(file_contents)
        imagesize = tf.constant([333,333])
        img_data = tf.image.resize_images(image_read,imagesize,method=0)
        print (img_data)
        plt.figure()
        plt.imshow(sess.run(img_data))
        plt.show()
        if x == 2:
            break



    return

print(distorted_inputs())
