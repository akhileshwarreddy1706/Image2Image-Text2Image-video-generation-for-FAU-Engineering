# Week 4 – Mock Text2Image Pipeline (CPU-only, deterministic)
# No external models. Just generates synthetic images from a prompt.

import os
from PIL import Image, ImageDraw, ImageFont

def text2image(prompt="FAU campus at night, futuristic neon lights, cinematic wide-angle view",
               output_dir="results/week4_t2i",
               num_images=3,
               size=(512, 512)):

    os.makedirs(output_dir, exist_ok=True)

    print("[Week 4 - T2I] Starting mock Text2Image pipeline...")
    print("[Week 4 - T2I] Prompt:", prompt)

    # Fixed background colors so outputs are deterministic
    colors = [
        (20, 20, 80),    # deep blue
        (40, 5, 60),     # purple-ish
        (5, 40, 40),     # teal-ish
    ]

    for i in range(num_images):
        color = colors[i % len(colors)]
        img = Image.new("RGB", size, color)
        draw = ImageDraw.Draw(img)

        # Simple "neon" style rectangles to hint futuristic look
        margin = 40 + i * 10
        draw.rectangle(
            [margin, margin, size[0] - margin, size[1] - margin],
            outline=(0, 255, 255),
            width=3,
        )

        # Draw short text (ID + prompt)
        text = f"T2I {i}\nFAU campus at night"
        draw.text((20, 20), text, fill=(255, 255, 255))

        out_path = os.path.join(output_dir, f"t2i_{i}.png")
        img.save(out_path)
        print(f"[Week 4 - T2I] Saved:", out_path)

    print("[Week 4 - T2I] Completed mock pipeline.")

if __name__ == "__main__":
    text2image()