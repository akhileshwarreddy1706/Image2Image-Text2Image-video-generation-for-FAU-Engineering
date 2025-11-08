# Image2Image + Text2Image Video Generation for FAU Engineering

**Course:** CAP6415 – Computer Vision (Fall 2025)  
**Team:** Akhileshwar Reddy Bommineni, Manaswini Pasupuleti, Pathri Jaydeep  
**Instructor:** Prof. Vadzim Sokol (vadzic@fau.edu)  
**University:** Florida Atlantic University – College of Engineering and Computer Science  

---

## 🎯 Abstract
Engineering research and education at Florida Atlantic University (FAU) benefit from realistic and creative visualizations.  
This project develops a **hybrid AI video generation pipeline** that combines **Text-to-Image (T2I)** and **Image-to-Image (I2I)** diffusion models to create short, AI-generated video clips depicting **FAU Engineering themes**—such as robotics, ocean engineering, autonomous drones, and smart manufacturing.

Our approach first uses a **Text-to-Image model** (Stable Diffusion / SDXL) to generate an initial frame from a descriptive prompt (e.g., “An FAU robotics engineer calibrating a drone inside a modern lab”).  
Then an **Image-to-Image refinement stage** (using ControlNet or AnimateDiff) evolves that frame into a short sequence of images showing motion or lighting change.  
Finally, the frames are stitched into a smooth video using OpenCV.  

The system is modular, reproducible, and designed for future FAU-specific dataset fine-tuning.  
All code is documented, and results can be replicated using the provided scripts.

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
source .venv/bin/activate     # (on macOS/Linux)
# OR
.venv\Scripts\activate        # (on Windows)
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ (Optional) Create the environment via Conda
```bash
conda env create -f environment.yml
conda activate cap6415-img2vid
```
## Repository Structure


.
├── src/
│   ├── generate_frames.py        # Text-to-Image frame generation
│   ├── refine_frames.py          # Image-to-Image refinement / motion
│   └── frames_to_video.py        # Combine frames into a video
│
├── notebooks/                    # Optional notebooks for experiments
├── results/
│   └── frame_000.png             # Sample FAU Engineering frame
│
├── week1log.txt                  # Weekly progress log (Week 1 example)
├── requirements.txt              # Python dependencies
├── environment.yml               # Conda environment
├── demo_video_script.md          # Video presentation outline
├── .gitignore                    # Ignore rules (Python + outputs)
├── LICENSE                       # MIT License
└── README.md                     # Project description