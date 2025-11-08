# Image2Image + Text2Image Video Generation for FAU Engineering

**Course:** CAP6415 (Fall 2025)  
**Team:** Akhileshwar Reddy Bommineni, Manaswini Pasupuleti, Pathri Jaydeep  

---

## 🎯 Abstract
Engineering research at Florida Atlantic University (FAU) increasingly benefits from generative AI for visualization.  
This project combines **Text-to-Image (T2I)** and **Image-to-Image (I2I)** diffusion models to create short AI-generated videos representing FAU Engineering themes such as robotics, ocean engineering, and smart manufacturing.  
Text prompts (e.g., “FAU robotics lab assembling a drone”) generate the initial frame via **Stable Diffusion / SDXL**, and **ControlNet / AnimateDiff** evolve subsequent frames to simulate motion.  
Frames are then assembled into a coherent video with OpenCV or ImageIO.  
The pipeline is reproducible, documented, and designed for education and research demonstrations.

---

## 🧰 How to Run (for later weeks)
```bash
# 1 – Install dependencies
pip install -r requirements.txt

# 2 – Generate frames
python src/generate_frames.py --prompt "FAU engineering lab robot assembling a drone"

# 3 – Assemble frames into video
python src/frames_to_video.py --input results/frames --fps 12 --output results/demo.mp4