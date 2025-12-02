
# Image2Image + Text2Image Video Generation for FAU Engineering

**Course:** CAP6415 – Computer Vision (Fall 2025)  
**Team:** Akhileshwar Reddy Bommineni, Manaswini Pasupuleti, Pathri Jaydeep  
**Instructor:** Prof. Velibor Adzic (vadzic@fau.edu)  
**University:** Florida Atlantic University – College of Engineering and Computer Science  

---

## 🎯 Abstract
AI-generated visualizations play an increasingly large role in engineering research, simulations, and educational demonstrations.  
This project covers a **hybrid AI video generation pipeline** based on **Text-to-Image (T2I)** and **Image-to-Image (I2I)** transformation concepts.

The system conceptually follows three major stages:

1. **Text-to-Image Generation:**  
   A frame is generated from a descriptive engineering-themed prompt (e.g., *“FAU engineering drone lab with multiple sensors and LED lighting”*).  
   This is implemented using a **mock diffusion pipeline** to ensure **reproducibility** without needing GPU hardware.

2. **Image-to-Image Refinement:**  
   The generated frame is refined with simulated variations (lighting, angle, color, or sharpness changes).  
   A lightweight placeholder model is used to demonstrate system architecture.

3. **Video Assembly:**  
   Multiple generated frames are stitched into a short engineering-themed video clip.

The repository is fully **portable**, **lightweight**, and **reproducible** on macOS, Windows, and Linux.  
No large downloads, GPUs, or API keys required.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/akhileshwarreddy1706/Image2Image-Text2Image-video-generation-for-FAU-Engineering.git
cd Image2Image-Text2Image-video-generation-for-FAU-Engineering
```

### 2️⃣ (Recommended) Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate     # macOS/Linux
# OR
.venv\Scripts\activate        # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ (Optional) Create environment via Conda
```bash
conda env create -f environment.yml
conda activate cap6415-img2vid
```

---

## 📁 Repository Structure

```bash
├── dataset/
│   └── fau_images/                # 16 curated FAU campus images (Week 4)
│
├── models/
│   └── onnx/                      # Config placeholders (no heavy models)
│
├── notebooks/                     # (Reserved for future expansion)
│
├── results/
│   ├── week2_frames/              # Week 2: Initial pipeline frames
│   ├── week3_frames/              # Week 3: Mock ONNX frames
│   ├── week4_t2i/                 # Week 4: Text-to-Image output
│   └── week4_i2i/                 # Week 4: Image-to-Image output
│
├── scripts/
│   └── rename_fau_images.py       # Dataset renaming script for Week 4
│
├── src/
│   ├── generate_frames.py         # Week 3 T2I mock generator
│   ├── refine_frames.py           # Week 3 I2I mock refinement
│   ├── frames_to_video.py         # Combine frames into a video clip
│   ├── week4_text2image.py        # Week 4: Text-to-Image pipeline
│   └── week4_image2image.py       # Week 4: Image-to-Image pipeline
│
├── week1log.txt
├── week2log.txt
├── week3log.txt
├── week4log.txt                   # NEW – Week 4 work summary
│
├── requirements.txt               # Python dependencies
├── environment.yml                # Conda environment specification
│
├── demo_video_script.md           # Outline for final project presentation
├── LICENSE                        # MIT License
└── README.md                      # Project documentation (this file)
```

---

## 🚀 Running the Project

### Week 3 — Generate mock frames (Text-to-Image)
```bash
python src/generate_frames.py
```

### Week 3 — Refine frames (Image-to-Image)
```bash
python src/refine_frames.py
```

### Convert frames to video
```bash
python src/frames_to_video.py
```

### 🧠 Text-to-Image (T2I)
We used the following prompt:

> **“FAU campus at night, futuristic neon lights, cinematic wide-angle view”**

This produces three generated variations:

```
results/week4_t2i/t2i_0.png
results/week4_t2i/t2i_1.png
results/week4_t2i/t2i_2.png
```

Run using:

```bash
python src/week4_text2image.py
```

---

### 🎨 Image-to-Image (I2I)
The base image used:

```
dataset/fau_images/fau_01.jpg
```

Outputs produced:

```
results/week4_i2i/i2i_0.png
results/week4_i2i/i2i_1.png
results/week4_i2i/i2i_2.png
results/week4_i2i/i2i_base_input.png
```

Run using:

```bash
python src/week4_image2image.py
```

---

## ✔️ Reproducibility
The project fully follows the reproducibility requirement:

- No external API calls  
- No GPU-specific features  
- No random non-deterministic behavior  
- All outputs generated locally  
- TA can run everything using only the provided scripts and dataset  
