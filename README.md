Here’s the **updated README** for your repository, fully aligned with the paper *"Enhanced Satellite Image Dehazing Using a CNN-Based cGAN with Cross-Scale Feature Fusion Block (CSFFB)"*:

---

# 🌫️ Enhanced Satellite Image Dehazing Using a CNN-Based cGAN with Cross-Scale Feature Fusion Block (CSFFB)

This repository implements a robust deep learning model for enhancing hazy satellite images using a **CNN-based conditional Generative Adversarial Network (cGAN)** integrated with a novel **Cross-Scale Feature Fusion Block (CSFFB)**. The model is designed for RGB-only satellite dehazing, removing the need for auxiliary sensor data (e.g., SAR).

## 🛰 Overview

Haze in satellite images leads to degraded clarity and poor performance in critical remote sensing tasks like segmentation, building footprint detection, and disaster assessment. This project introduces a deep learning solution using:

* ✅ **Conditional GAN (cGAN)** for image-to-image translation
* ✅ **Cross-Scale Feature Fusion Blocks (CSFFBs)** to capture multi-scale spatial features
* ✅ **Dilated residual blocks** for context aggregation
* ✅ **Custom loss functions** (L1 + Least Squares GAN Loss)
* ✅ **PatchGAN** discriminator for improved texture learning

## 🔍 Key Features

* 🚀 **Single-sensor solution**: Uses RGB-only images, no SAR needed
* 🧠 **CSFFB with 5-path convolutions**: (1×1, 3×3, 1×3, 3×1, and max-pooling)
* 🎯 **Multi-level haze handling**: Trained on Thin, Moderate, and Thick haze
* 🧪 **Tested on Haze1k dataset** with strong benchmarks
* 📈 **Advanced metrics support**: PSNR, SSIM, IoU, F1-Score, Pixel Accuracy, LPIPS, FID, and VIF

## 🧠 Model Architecture

* **Generator**: U-Net-based encoder-decoder with:

  * Cross-Scale Feature Fusion Blocks (CSFFB)
  * Dilated Residual Blocks
  * Skip connections for spatial consistency
* **Discriminator**: PatchGAN classifies 70×70 patches
* **Loss Functions**:

  * Generator: `L_total = L_GAN + λ * L1` (λ = 100)
  * Discriminator: Binary Cross-Entropy

## 🧪 Dataset

* **Name**: [Haze1k](https://www.kaggle.com/datasets/mohit3430/haze1k)
* **Composition**: 1200 paired hazy and clear satellite images (RGB)
* **Fog Levels**: Thin, Moderate, Thick (400 each)
* **Train/Val/Test**: 80% / 10% / 10% split

## 📊 Results

| Metric       | Our Model |
| ------------ | --------- |
| **PSNR**     | 25.47     |
| **SSIM**     | 0.9493    |
| **IoU**      | 0.342     |
| **F1-Score** | 0.127     |
| **PA**       | 0.963     |
| **LPIPS**    | 0.072     |
| **FID**      | 9.36      |
| **VIF**      | 0.884     |

> 📌 Outperforms DCP, DehazeNet, FFA-Net, and SAR-Opt-cGAN on multiple haze levels.

## 🛠 Installation

```bash
git clone https://github.com/Aragog540/Sat-dhze.git
cd Sat-dhze
pip install -r requirements.txt
```

## 🏗 Training

```bash
python train.py --dataset_dir ./haze1k --epochs 125 --batch_size 4
```

Hyperparameters:

* Image size: 256×256
* Optimizer: Adam (`lr=0.0002`, `β1=0.5`)
* Loss: LSGAN + L1
* Normalization: `[-1, 1]` using `image / 127.5 - 1.0`

## 🖼 Visual Comparison

| Input | Ground Truth | DCP | DehazeNet | FFA-Net | SAR-Opt-cGAN | **Ours** |
| ----- | ------------ | --- | --------- | ------- | ------------ | -------- |
| 🌫️   | 🌄           | ❌   | ❌         | ✅       | ✅            | ✅✅       |


## ⚠️ Limitations & Future Work

* 🚧 High memory usage due to complex model
* 🌃 Not tested on nighttime or extreme weather imagery
* 🔧 Training stability is sensitive to initialization and hyperparameters
* 📦 Requires paired hazy/clear images (currently supervised)

---

Let me know if you'd like the README in a `.md` file or as a downloadable version.
