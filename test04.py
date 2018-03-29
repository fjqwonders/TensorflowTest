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

    print (filenames)

    batch_size = 100
    min_after_dequeue = 200
    capacity = min_after_dequeue + 3 * batch_size

    image_batch, label_batch = tf.train.shuffle_batch([filenames, label_indexes], batch_size = batch_size, capacity = capacity, min_after_dequeue = min_after_dequeue, enqueue_many=True)


    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    print(sess.run(image_batch),sess.run(label_batch))

    coord.request_stop()
    coord.join(threads)


    return

distorted_inputs()
