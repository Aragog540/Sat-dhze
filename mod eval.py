# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:35:10 2024

@author: swaro
"""

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
import statistics
import os

# Define the paths to your datasets
base_dir = 'C:\\Users\\swaro\\Desktop\\sat dehze\\Distributed_haze1k'
paths = {
    'Moderate': os.path.join(base_dir, 'test_moderate'),
    'Thick': os.path.join(base_dir, 'test_thick'),
    'Thin': os.path.join(base_dir, 'test_thin')
}

# Load the .keras model without extra quotes or special formatting for compatibility
loaded_generator = tf.keras.models.load_model(r"C:\Users\swaro\Desktop\sat dehze\results\generator_model.keras")

print("Model loaded successfully.")

ssim_list = []
psnr_list = []

def ssim_evaluation(img1, img2):
    ssim_value = ssim(img1, img2, channel_axis=2, data_range=img2.max() - img2.min())
    ssim_list.append(ssim_value)
    
def psnr_evaluation(img1, img2):
    psnr_value = psnr(img1, img2)
    psnr_list.append(psnr_value)

def evaluate_model(model, inp, tar, sno):
    pred = model(inp, training=True)
    plt.figure(figsize=(15, 15))
    
    inp = inp[0].numpy()
    inp = (inp + 1) / 2.0
    tar = tar[0].numpy()
    tar = (tar + 1) / 2.0
    pred = pred[0].numpy()
    pred = (pred + 1) / 2.0
    
    ssim_evaluation(tar, pred)
    psnr_evaluation(tar, pred)
    
    display_list = [inp, tar, pred]
    title = ['Haze Image', 'Ground Truth', 'Predicted Image']
   
    if sno <= 5:
        for i in range(3):
            plt.subplot(1, 3, i + 1)
            plt.title(title[i])
            plt.imshow(display_list[i])
            plt.axis('off')
        plt.show()
    plt.close()

skeleton = {
    'SSIM': [],
    'PSNR': []
}

def evaluate_test(data_dir, name):
    datagen = ImageDataGenerator(rescale=1.0 / 255)
    test_data = datagen.flow_from_directory(
        data_dir,
        target_size=(256, 256),
        batch_size=1,
        class_mode=None,
        shuffle=False
    )
    
    for i in range(len(test_data)):
        inp, tar = test_data[i]  # Adjust according to your image setup
        evaluate_model(loaded_generator, inp, tar, i)
        
    ssim_mean = statistics.mean(ssim_list)
    psnr_mean = statistics.mean(psnr_list)
    
    print('Dataset-{}'.format(name))
    print(f'SSIM Mean: {ssim_mean}')
    print(f'PSNR Mean: {psnr_mean}')
    
    skeleton['SSIM'].append(ssim_mean)
    skeleton['PSNR'].append(psnr_mean)
        
    ssim_list.clear()
    psnr_list.clear()

# Evaluate each dataset
for name, path in paths.items():
    evaluate_test(path, name)
