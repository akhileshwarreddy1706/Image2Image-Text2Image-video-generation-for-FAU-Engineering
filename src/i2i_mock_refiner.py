"""
i2i_mock_refiner.py

Week 2/3 - Mock Image-to-Image Refinement Pipeline
--------------------------------------------------
This lightweight, offline-only component simulates the behavior of an
Image-to-Image (I2I) model such as:
    - Stable Diffusion I2I
    - ControlNet
    - SD Image Variation models

Purpose:
- Provide deterministic transformations for debugging and demonstration.
- Ensure 100% reproducibility for TA evaluation.
- No GPU, internet, or large ML models required.

Used in:
- Early pipeline testing (Week 2 & 3)
- Week 4 as a stable baseline
- Week 5 as the fallback refinement method if API is not used
"""

import os
from PIL import Image, ImageEnhance, ImageFilter


def refine_mock_i2i(
    input_dir: str = "results/week2_frames",
    output_dir: str = "results/week2_refined",
    strength: float = 1.2,
) -> None:
    """
    Perform simple deterministic "refinement" operations on images.

    Args:
        input_dir: Directory containing source images.
        output_dir: Directory to save refined images.
        strength: Level of sharpening/contrast applied.

    Simulated refinement stack:
        - Slight sharpening
        - Slight contrast enhancement
        - Very light Gaussian blur (mimics denoising)
    """

    print("\n[Mock I2I] Starting simulated refinement pipeline...")
    print(f"[Mock I2I] Input directory:  {input_dir}")
    print(f"[Mock I2I] Output directory: {output_dir}\n")

    os.makedirs(output_dir, exist_ok=True)

    # Collect images
    images = [
        f for f in sorted(os.listdir(input_dir))
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    if not images:
        print("[Mock I2I] No images found. Refinement skipped.\n")
        return

    for idx, img_name in enumerate(images):
        src_path = os.path.join(input_dir, img_name)
        dst_path = os.path.join(output_dir, img_name)

        img = Image.open(src_path)

        # 1) Sharpening
        img = img.filter(ImageFilter.SHARPEN)

        # 2) Contrast enhancement
        img = ImageEnhance.Contrast(img).enhance(strength)

        # 3) Light denoising (blur)
        img = img.filter(ImageFilter.GaussianBlur(radius=0.4))

        # Save refined version
        img.save(dst_path)

        print(f"[Mock I2I] Refined: {src_path} → {dst_path}")

    print("\n[Mock I2I] Completed simulated refinement pipeline.\n")


if __name__ == "__main__":
    refine_mock_i2i()