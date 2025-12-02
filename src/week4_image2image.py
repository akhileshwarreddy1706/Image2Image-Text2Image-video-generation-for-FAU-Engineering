# Week 4 – Mock Image2Image Pipeline (CPU-only, deterministic)
# Uses a real FAU image (fau_01.jpg) and generates stylized variants.

import os
from pathlib import Path
from PIL import Image, ImageEnhance, ImageFilter

DATASET_IMG = Path("dataset/fau_images/fau_01.jpg")  # put FAU entrance sign here

def image2image(input_image: str | None = None,
                output_dir: str = "results/week4_i2i",
                num_images: int = 3,
                size: tuple[int, int] = (512, 512)) -> None:

    os.makedirs(output_dir, exist_ok=True)

    print("[Week 4 - I2I] Starting mock Image2Image pipeline...")

    # Resolve input image path
    if input_image is not None:
        img_path = Path(input_image)
    else:
        img_path = DATASET_IMG

    if not img_path.exists():
        print(f"[Week 4 - I2I] ERROR: Input image not found at {img_path}")
        print("[Week 4 - I2I] Please place your FAU image as dataset/fau_images/fau_01.jpg")
        return

    # Load image, convert to RGB and resize to a standard size
    img = Image.open(img_path).convert("RGB")
    img = img.resize(size, Image.BICUBIC)

    # Save the base input copy (for README / results)
    base_out = os.path.join(output_dir, "i2i_base_input.png")
    img.save(base_out)
    print("[Week 4 - I2I] Saved base input copy:", base_out)

    # Generate deterministic transformed variants
    for i in range(num_images):
        out = img.copy()

        if i == 0:
            # Brighter, “daytime cleaned” look
            out = ImageEnhance.Brightness(out).enhance(1.25)
        elif i == 1:
            # Higher contrast “poster” style
            out = ImageEnhance.Contrast(out).enhance(1.5)
        elif i == 2:
            # Slight blur + sharpen combo to mimic “glow” effect
            out = out.filter(ImageFilter.GaussianBlur(radius=1.5))
            out = ImageEnhance.Brightness(out).enhance(1.1)

        out_path = os.path.join(output_dir, f"i2i_{i}.png")
        out.save(out_path)
        print(f"[Week 4 - I2I] Saved:", out_path)

    print("[Week 4 - I2I] Completed mock pipeline.")

if __name__ == "__main__":
    image2image()