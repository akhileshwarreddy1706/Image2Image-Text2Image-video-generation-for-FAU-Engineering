"""
t2i_week4_prompt_generator.py

Week 4 - Mock Text-to-Image (T2I) Prompt-Based Generator
--------------------------------------------------------
A deterministic, CPU-only simulation of a Text-to-Image model.

Purpose:
- Produce synthetic "AI-style" images themed around an FAU prompt.
- Demonstrate how prompt-based generation fits into the project pipeline.
- Replace the simple Week 3 mock generator with a more stylized version.

Outputs:
- Saves 3 synthetic 512x512 images into results/week4_t2i/
- Each image contains geometric highlights and short text overlays

This module is used as the Week 4 official T2I component.
"""

import os
from PIL import Image, ImageDraw


def generate_prompt_t2i(
    prompt: str = "FAU campus at night, futuristic neon lights, cinematic wide-angle view",
    output_dir: str = "results/week4_t2i",
    num_images: int = 3,
    size: tuple[int, int] = (512, 512),
) -> None:
    """
    Generate deterministic synthetic images based on an FAU-themed prompt.

    Args:
        prompt:
            Text prompt describing the scene. Not used by a real model,
            but displayed and logged for clarity.
        output_dir:
            Folder where generated images will be saved.
        num_images:
            Number of output frames to generate.
        size:
            (Width, height) in pixels for each output image.
    """
    os.makedirs(output_dir, exist_ok=True)

    print("\n[Week 4 - T2I] Starting mock Text-to-Image pipeline...")
    print("[Week 4 - T2I] Prompt:", prompt)

    # Predefined deterministic background colors
    colors = [
        (20, 20, 80),     # Deep blue
        (40, 5, 60),      # Purple-ish
        (5, 40, 40),      # Teal-ish
    ]

    for i in range(num_images):
        color = colors[i % len(colors)]

        # Base image
        img = Image.new("RGB", size, color)
        draw = ImageDraw.Draw(img)

        # Stylized neon rectangle motif
        margin = 40 + i * 10
        draw.rectangle(
            [margin, margin, size[0] - margin, size[1] - margin],
            outline=(0, 255, 255),
            width=3,
        )

        # Add short text: ID + brief prompt keyword
        draw.text(
            (20, 20),
            f"T2I Frame {i}\nFAU campus (mock)",
            fill=(255, 255, 255)
        )

        out_path = os.path.join(output_dir, f"t2i_{i}.png")
        img.save(out_path)

        print(f"[Week 4 - T2I] Saved: {out_path}")

    print("[Week 4 - T2I] Completed mock pipeline.\n")


if __name__ == "__main__":
    generate_prompt_t2i()