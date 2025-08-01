# [cite\_start]Enhanced Satellite Image Dehazing Using a CNN-Based cGAN with Cross-Scale Feature Fusion Block (CSFFB) [cite: 1, 2]

[cite\_start]This repository contains the implementation of a deep learning framework for enhancing satellite images degraded by haze, using a *CNN-based conditional Generative Adversarial Network (cGAN)* architecture with a novel *Cross-Scale Feature Fusion Block (CSFFB)*[cite: 5, 6]. [cite\_start]The goal is to provide a robust, single-sensor dehazing solution that eliminates the complexities of multi-sensor fusion[cite: 4, 5].

## 🛰 Overview

[cite\_start]Hazy satellite images severely impact the quality and usability of remote sensing data[cite: 15]. This project introduces a deep learning approach that integrates:

  - [cite\_start]A *Conditional GAN (cGAN)* architecture [cite: 5, 6, 74]
  - [cite\_start]A *Cross-Scale Feature Fusion Block (CSFFB)* for multi-scale feature learning and fine detail preservation [cite: 5, 7, 27, 33]
  - [cite\_start]*Progressive CNNs* and *skip connections* to preserve structural details [cite: 7, 94]
  - [cite\_start]A combined loss function of adversarial loss and L1 reconstruction loss to balance perceptual realism and pixel-level fidelity [cite: 102, 105]

## 🔍 Key Features

  - [cite\_start]✅ CNN-based cGAN hybrid structure for realistic image generation [cite: 5, 10]
  - [cite\_start]✅ Cross-Scale Feature Fusion Blocks (CSFFBs) to enhance multi-scale feature extraction and preserve structural details [cite: 5, 7, 20]
  - [cite\_start]✅ The architecture is designed for single-sensor (RGB-only) inputs, removing the need for auxiliary data like SAR images [cite: 5, 6, 7, 19]
  - [cite\_start]✅ PatchGAN discriminator to encourage finer texture generation in local image patches [cite: 96]
  - [cite\_start]✅ Benchmarked on the Hazelk dataset, which includes images with thin, moderate, and thick haze levels [cite: 8, 21]

## 🧠 Model Architecture

The proposed architecture includes:

  - [cite\_start]A generator with a U-Net structure enhanced with Cross-Scale Feature Fusion Blocks (CSFFBs) and skip connections[cite: 91, 94]. [cite\_start]The CSFFB uses parallel convolutional paths with kernel sizes of $1\\times1$, $3\\times3$, $1\\times3$, and $3\\times1$, as well as a max-pooling branch[cite: 92].
  - [cite\_start]A discriminator with a PatchGAN structure that classifies local $70\\times70$ image patches[cite: 96].
  - [cite\_start]A combined loss function: $\\mathcal{L}*{Total} = \\mathcal{L}*{GAN} + \\lambda\\mathcal{L}\_{L1}$[cite: 104].
  - [cite\_start]Training is performed using the Adam optimizer with a learning rate of $2\\times10^{-4}$[cite: 108].

## 📊 Results

  - [cite\_start]Achieved a PSNR of 28.6 and SSIM of 0.93 on benchmark datasets[cite: 9].
  - [cite\_start]Outperformed existing methods, including multi-sensor fusion techniques[cite: 9, 10].
  - [cite\_start]The dehazed outputs maintain sharpness and structural definiteness[cite: 9, 33].
  - [cite\_start]Ablation studies confirm that the CSFFB significantly improves performance on segmentation metrics like IoU, F1-Score, and Pixel Accuracy[cite: 145].

## 🛠 Installation

```bash
git clone https://github.com/Aragog540/Sat-dhze
cd satellite-image-dehazing-cgan
pip install -r requirements.txt
```
