"""
t2i_mock_generator.py

Week 3 - Mock Text-to-Image Generator
------------------------------------
A lightweight, fully offline placeholder for a Stable Diffusion or ONNX
Text-to-Image model.

Purpose:
- Produce deterministic "fake" images from a prompt.
- Allow the entire project to run WITHOUT internet, GPUs, or large models.
- Ensure reproducibility on any TA machine.

Used in:
- Week 3 assignment
- Week 4 baseline comparisons
- Final project (to show architecture before API or real model is added)
"""

import os
from PIL import Image, ImageDraw


def generate_mock_t2i(
    prompt: str = "FAU Engineering building, futuristic lighting",
    num_frames: int = 3,
    output_dir: str = "results/week3_frames",
) -> None:
    """
    Generate simple placeholder images based on a text prompt.

    Args:
        prompt: Text description (ignored by mock, printed for logging).
        num_frames: Number of mock frames to generate.
        output_dir: Folder to save output PNG frames.
    """

    os.makedirs(output_dir, exist_ok=True)

    print("\n[Mock T2I] Starting simulated Text-to-Image pipeline...")
    print("[Mock T2I] Prompt:", prompt)

    for i in range(num_frames):
        # Each frame is just a colored square with text
        img = Image.new("RGB", (512, 512), (40 * i % 255, 50, 180))
        draw = ImageDraw.Draw(img)

        draw.text((20, 20), f"Mock T2I Frame {i}", fill="white")
        draw.text((20, 60), f"Prompt: {prompt[:25]}...", fill="white")

        filename = os.path.join(output_dir, f"frame_{i}.png")
        img.save(filename)

        print(f"[Mock T2I] Saved: {filename}")

    print("[Mock T2I] Completed mock generation.\n")


if __name__ == "__main__":
    generate_mock_t2i()