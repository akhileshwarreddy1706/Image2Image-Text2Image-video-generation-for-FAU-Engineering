"""
Week 5 - REAL Text-to-Image Generation + FAU Branding (Offline)
--------------------------------------------------------------
This script:
  • Generates FAU-style images using SD-Turbo (offline)
  • Adds a REAL FAU logo overlay for proper branding
  • Outputs both clean + branded images

Final Output Folder:
    results/week5_t2i_real/
"""

import torch
from pathlib import Path
from diffusers import AutoPipelineForText2Image
from PIL import Image

# Output directory
OUT_DIR = Path("results/week5_t2i_real")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Prompts with stronger FAU branding descriptions
PROMPTS = [
    "Florida Atlantic University College of Engineering building with visible FAU signage on the front wall, palm trees, bright sunny Florida sky, realistic promotional photo, high detail",
    "FAU Engineering building at sunset with FAU logo sign on the entrance, cinematic lighting, palm trees, 4k promotional image",
    "Aerial view of Florida Atlantic University campus with FAU red-blue color themes, palm trees, modern academic buildings, professional drone shot",
    "FAU Engineering building at night with glowing lights, FAU owl emblem near the entrance, motion blur of students walking, vibrant promotional image",
]

MODEL_ID = "stabilityai/sd-turbo"

# Device selection
if torch.backends.mps.is_available():
    device = "mps"
    dtype = torch.float16
elif torch.cuda.is_available():
    device = "cuda"
    dtype = torch.float16
else:
    device = "cpu"
    dtype = torch.float32

print(f"[Week5] Using device: {device}")

# Load model
pipe = AutoPipelineForText2Image.from_pretrained(
    MODEL_ID,
    torch_dtype=dtype
)
pipe.to(device)

# Load FAU Logo
FAU_LOGO_PATH = "fau_logo.png"   # put logo file in project root
fau_logo = Image.open(FAU_LOGO_PATH).convert("RGBA")

# Resize logo (feel free to adjust)
LOGO_SIZE = (80, 80)
fau_logo = fau_logo.resize(LOGO_SIZE)

# Generation Loop
for i, prompt in enumerate(PROMPTS, start=1):
    print(f"[Week5] Generating FAU image {i}/{len(PROMPTS)}")

    result = pipe(
        prompt=prompt,
        num_inference_steps=4,
        guidance_scale=0.0
    )

    img = result.images[0]

    # Add FAU Logo Overlay
    branded = img.copy()
    branded = branded.convert("RGBA")

    logo_x = branded.width - LOGO_SIZE[0] - 20
    logo_y = branded.height - LOGO_SIZE[1] - 20

    branded.paste(fau_logo, (logo_x, logo_y), fau_logo)
    branded = branded.convert("RGB")

    out_branded = OUT_DIR / f"fau_week5_real_{i:02d}.png"   
    branded.save(out_branded)

    print(f"[Week5] Saved FAU-branded image → {out_branded}")

print("\n[Week5] COMPLETED — Real FAU images + Logo Branding generated!")