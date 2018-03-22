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
    print (filenames)
    print (label_indexes)

    num_preprocess_threads = 4
    images_and_labels = []
    for thread_id in range(num_preprocess_threads):
        image_buffer = tf.read_file(filename)
        bbox = []
        train = True
        image = image_preprocessing(image_buffer, bbox, train, thread_id)
        images_and_labels.append([image, label_index])

    for i in filenames:
        print(i)
        file_contents = tf.read_file(i)
        image_read = tf.image.decode_jpeg(file_contents)


    filename, label_index = tf.train.slice_input_producer([filenames, label_indexes], shuffle=True)



    return

print(distorted_inputs())
