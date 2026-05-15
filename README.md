# Image2Image + Text2Image Video Generation for FAU Engineering

**Course:** CAP6415 – Computer Vision (Fall 2025)    
**Instructor:** Prof. Velibor Adzic (vadzic@fau.edu)  
**University:** Florida Atlantic University – College of Engineering & Computer Science  

---

## 🎯 Abstract

This project implements a complete **generative video creation system** that transforms prompts, images, and diffusion-inspired refinements into an AI-generated **promotional-style video for FAU Engineering**.

The pipeline evolves across five structured stages:

- **Week 2:** Mock Image-to-Image refinement  
- **Week 3:** Mock Text-to-Image generation  
- **Week 4:** Deterministic T2I + I2I using curated FAU images  
- **Week 5:** **Real Text-to-Image generation using Stable Diffusion Turbo (offline)**  
- **Final:** Fully automated **promotional video builder**

All components execute **offline**, ensuring full reproducibility.

### Model & Framework Attribution
- Stable Diffusion Turbo © Stability AI  
- HuggingFace Diffusers © HuggingFace Team  
- PyTorch © Meta AI  
- FAU campus images used under academic fair‑use  

---

## 📝 Description

The goal of this course project is to:

“Use generative video tools, and real photos and videos of the FAU campus, to create a promotional video for the College of Engineering.”

Our system meets all requirements:

### ✔ Development  
We progressively built and improved mock diffusion pipelines, dataset tools, real generative models, and a complete video assembly module.

### ✔ Documentation  
Every step is explained in logs (Week1–Week5), and code is clean, modular, and easy to extend.

### ✔ Results  
Outputs for Weeks 2–5 are stored under `results/` and regenerate deterministically.

### ✔ Reproducibility  
All generation runs **offline**, no API keys required. We can reproduce everything using only `requirements.txt`.

### ✔ Demo Video  
A 10–20 minute walkthrough accompanies this project (`demo_video_script.md`).

---

## 📁 Repository Structure

```
src/
│── final_promo_builder.py          # Final official promotional video builder
│── assemble_video.py               # Legacy weekly video assembler
│── t2i_mock_generator.py           # Week 3 – Mock T2I
│── i2i_mock_refiner.py             # Week 2 – Mock I2I
│── t2i_week4_prompt_generator.py   # Week 4 – Deterministic T2I
│── i2i_week4_refiner.py            # Week 4 – Deterministic I2I
│── t2i_week5_real_generator.py     # Week 5 – REAL SD-Turbo T2I

scripts/
│── prepare_fau_dataset.py

dataset/
│── fau_images/                     # 16 selected FAU campus images

results/                             # Empty on repo clone; populated after running scripts
│── (auto‑generated weekly outputs)
│── (auto‑generated final promo video)

run_full_pipeline.sh                      # Full automation script (Weeks 2–5 mock + real)

week1log.txt  
week2log.txt  
week3log.txt  
week4log.txt  
week5log.txt  
requirements.txt  
environment.yml  
README.md  
LICENSE  
demo_video_script.md  
verified_commits_setup.md
```

---

## ▶️ Execution Guide (Reproducible Offline)

### 1️⃣ Create environment
```bash
python3 -m venv fau
source fau/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 2️⃣ Week 2 — Mock Image‑to‑Image
```bash
python src/i2i_mock_refiner.py
```

---

## 3️⃣ Week 3 — Mock Text‑to‑Image
```bash
python src/t2i_mock_generator.py
```

---

## 4️⃣ Week 4 — Deterministic T2I + I2I
```bash
python src/t2i_week4_prompt_generator.py
python src/i2i_week4_refiner.py
```

Outputs:

```
results/week4_t2i/
results/week4_i2i/
```

---

## 5️⃣ Week 5 — Real Text‑to‑Image (SD‑Turbo)
```bash
python src/t2i_week5_real_generator.py
```

Outputs:

```
results/week5_t2i_real/
```

---

## 6️⃣ Final Promotional Video 
```bash
python src/final_promo_builder.py
```

This generates the **official submission video**:

```
results/final_promo_video.mp4
```

This video includes:
- Title slide  
- Week 5 T2I images (1 sec each)  
- Week 4 I2I slideshow (2.5 sec total)  
- Dataset slideshow (6 images × 1 sec)  
- End slide  

---

## 7️⃣ Optional — Run the Entire Pipeline with One Command  
```bash
bash run_full_pipeline.sh
```

---

## 🧪 Reproducibility

Our project is fully reproducible because:

- All scripts run **offline**
- Every weekly output is generated deterministically  
- Week 5 uses Stable Diffusion Turbo locally  
- Full pipeline regenerates from scratch using only:
  ```
  pip install -r requirements.txt
  python src/final_promo_builder.py
  ```

---

## 📊 Results Overview

### Week 5 – Final Real FAU Images  
Stored in:

```
results/week5_t2i_real/
```

These power the promotional video.

### Full Promotional Video  
```
results/final_promo_video.mp4
```

---

## 🎥 Demo Video

The demo video includes:

- Code walkthrough  
- Weekly evolution of models  
- Live execution  
- Analysis  
- Final promotional video  

See: `demo_video_script.md`.

---

## ✔️ Conclusion

This project delivers a fully offline, reproducible, modular generative video pipeline featuring:

- Image‑to‑Image + Text‑to‑Image  
- Mock + deterministic + real diffusion  
- Automated branding  
- Professional video assembly  

---

## 🧩 Limitations & Future Work

- SD‑Turbo favors speed → lower resolution  
- No temporal diffusion → slight frame inconsistency  
- Future improvements:
  - SD‑XL for HQ images  
  - ControlNet for structure control  
  - Real temporal video diffusion  
