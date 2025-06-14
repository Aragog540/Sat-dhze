
# Enhanced Satellite Image Dehazing Using a CNN-Based cGAN with Inception Blocks

This repository contains the implementation of a deep learning framework for enhancing satellite images degraded by haze, using a *CNN-based conditional Generative Adversarial Network (cGAN)* architecture with *Inception blocks*.

## 🛰 Overview

Hazy satellite images can significantly degrade performance in downstream applications like object detection, segmentation, and remote sensing analysis. This project introduces a hybrid deep learning approach that integrates:

- *Conditional GAN (cGAN)* architecture
- *Inception modules* for multi-scale feature extraction
- *Custom loss functions* to enhance perceptual quality
- *Multi-scale SSIM* and *curriculum training* strategies for improved stability and performance

## 🔍 Key Features

- ✅ CNN + cGAN hybrid structure for realistic image generation
- ✅ Inception blocks for better spatial understanding
- ✅ Multi-scale SSIM and perceptual loss to improve dehazing quality
- ✅ Curriculum learning to stabilize adversarial training
- ✅ Benchmarked on satellite imagery datasets (e.g., RESIDE or real-world hazy satellite images)

## 🧠 Model Architecture

The proposed architecture includes:
- Generator with Inception modules and skip connections
- Discriminator with PatchGAN structure
- Combined loss function: SSIM + L1 + Perceptual loss
- Training strategy with curriculum learning

## 📊 Results

- Achieved *PSNR > XX dB* and *SSIM ~ 0.99* on benchmark datasets
- Outperformed traditional and deep learning-based dehazing models
- Realistic, high-resolution dehazed outputs on satellite images

## 🛠 Installation

```bash
git clone https://github.com/yourusername/satellite-image-dehazing-cgan.git
cd satellite-image-dehazing-cgan
pip install -r requirements.txt
