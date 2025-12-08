"""
i2i_week4_refiner.py

Week 4 - Mock Image-to-Image (I2I) Pipeline
-------------------------------------------
CPU-only, deterministic I2I refinement that:
  - Takes a real FAU image (default: dataset/fau_images/fau_01.jpg)
  - Produces several stylized variants
  - Runs without internet, GPUs, or external models

This module is used as the *Week 4* Image2Image component in the
overall Text2Image + Image2Image → Video pipeline.
"""

import os
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter

# Default FAU image used for Week 4 experiments.
DATASET_IMG = Path("dataset/fau_images/fau_01.jpg")


def image2image(
    input_image=None,
    output_dir="results/week4_i2i",
    num_images=3,
    size=(512, 512),
):
    """
    Generate deterministic stylistic variations of a single image.

    Args:
        input_image: optional path to an input image. If None, uses DATASET_IMG.
        output_dir: directory for refined images.
        num_images: number of variants to create.
        size: final (width, height) for resizing.
    """

    os.makedirs(output_dir, exist_ok=True)
    print("[Week 4 - I2I] Starting mock Image2Image pipeline...")

    img_path = Path(input_image) if input_image is not None else DATASET_IMG

    if not img_path.exists():
        print(f"[Week 4 - I2I] ERROR: Input image not found at {img_path}")
        print("[Week 4 - I2I] Expected image: dataset/fau_images/fau_01.jpg")
        return

    # Load & resize
    img = Image.open(img_path).convert("RGB")
    img = img.resize(size, Image.BICUBIC)

    # Save base reference
    base_out = os.path.join(output_dir, "i2i_base_input.png")
    img.save(base_out)
    print("[Week 4 - I2I] Saved base input copy:", base_out)

    # Generate variants
    for i in range(num_images):
        out = img.copy()

        if i == 0:  # Brightened
            out = ImageEnhance.Brightness(out).enhance(1.25)

        elif i == 1:  # Poster style
            out = ImageEnhance.Contrast(out).enhance(1.5)

        elif i == 2:  # Soft glow
            out = out.filter(ImageFilter.GaussianBlur(radius=1.5))
            out = ImageEnhance.Brightness(out).enhance(1.1)

        out_path = os.path.join(output_dir, f"i2i_{i}.png")
        out.save(out_path)
        print(f"[Week 4 - I2I] Saved:", out_path)

    print("[Week 4 - I2I] Completed mock pipeline.")


if __name__ == "__main__":
    image2image()